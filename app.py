import streamlit as st
import cv2
import easyocr
import requests
import json
import sqlite3
import numpy as np
import io
from PIL import Image

# Configure Streamlit page layout
st.set_page_config(page_title="Advanced Card Scanner CRM", page_icon="📇", layout="wide")

# Cache the EasyOCR reader so it loads into your RAM exactly once (saves time)
@st.cache_resource
def load_ocr():
    return easyocr.Reader(['en'], gpu=False)

reader = load_ocr()

# -------------------------------------------------------------
# DATABASE INITIALIZATION
# -------------------------------------------------------------
def init_db():
    conn = sqlite3.connect('local_crm_cards.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS crm_cards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT, job_title TEXT, company TEXT, phone TEXT, email TEXT, address TEXT,
            sector TEXT, remarks TEXT, image_front BLOB, image_back BLOB
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# -------------------------------------------------------------
# CORE BACKEND LOGIC (OCR, AI PARSING, DATABASE EXECUTION)
# -------------------------------------------------------------
def process_ocr(image_bytes):
    if not image_bytes:
        return ""
    # Convert raw image bytes into a format OpenCV understands
    file_bytes = np.asarray(bytearray(image_bytes), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    
    # Run CRAFT + CRNN text extraction
    result = reader.readtext(image, detail=0)
    return "\n".join(result)

def parse_with_local_llm(raw_text):
    prompt = f"""
    You are an intelligent data extraction tool. Analyze this text extracted from one or both sides of a business card.
    Extract the contact details, address, and analyze the text to determine the business sector (e.g., Hardware, Software, Printer, Finance, Medical, Consulting, Real Estate, etc.).
    Also generate a brief 1-sentence summary for 'Remarks' based on their job title or company.

    Extracted Text:
    {raw_text}
    
    Respond ONLY with a valid JSON object. Do not include introductory text like "Here is your JSON". 
    Use this exact format:
    {{
        "Name": "extracted name or Unknown",
        "Job_Title": "extracted title or Unknown",
        "Company": "extracted company or Unknown",
        "Phone": "extracted phone or Unknown",
        "Email": "extracted email or Unknown",
        "Address": "extracted physical address or Unknown",
        "Sector": "Choose a relevant sector like Software, Hardware, Printer, etc., or Unknown",
        "Remarks": "Generated automated remark based on text or Unknown"
    }}
    """
    
    url = "http://localhost:11434/api/generate"
    payload = {"model": "phi3", "prompt": prompt, "stream": False, "format": "json"}
    
    try:
        response = requests.post(url, json=payload)
        return json.loads(response.json()['response'])
    except Exception as e:
        st.error(f"Error connecting to local Ollama server: {e}")
        return None

def save_to_db(data, img_front, img_back):
    conn = sqlite3.connect('local_crm_cards.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO crm_cards (name, job_title, company, phone, email, address, sector, remarks, image_front, image_back)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (data["Name"], data["Job_Title"], data["Company"], data["Phone"], data["Email"], data["Address"], data["Sector"], data["Remarks"], img_front, img_back))
    conn.commit()
    conn.close()

def get_all_cards():
    conn = sqlite3.connect('local_crm_cards.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, job_title, company, phone, email, address, sector, remarks, image_front, image_back FROM crm_cards ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows

# -------------------------------------------------------------
# USER INTERFACE LAYOUT (STREAMLIT)
# -------------------------------------------------------------
st.title("📇 Advanced Local Visiting Card Scanner & CRM")
st.write("Scan physical cards using your phone camera, parse data locally using AI, and manage your network safely.")

tab1, tab2 = st.tabs(["📸 Scan & Process Card", "🗄️ View Contact Vault"])

with tab1:
    st.subheader("Step 1: Capture Card Photos")
    
    # Check for 1 or 2 sided input configurations
    card_sides = st.radio("How many sides does this business card have?", ["1-Side Only", "2-Sided Card"], horizontal=True)
    
    # ANALYSIS UPDATE 1: Input method switcher built cleanly alongside your choices
    input_method = st.radio("Choose Input Method:", ["📁 Upload / Snap Photo File", "📸 Use Live Camera Widget"], horizontal=True)
    
    col1, col2 = st.columns(2)
    img_front_bytes = None
    img_back_bytes = None
    
    if input_method == "📸 Use Live Camera Widget":
        with col1:
            front_photo = st.camera_input("📸 Capture Front Side")
            if front_photo:
                img_front_bytes = front_photo.getvalue()
                
        with col2:
            if card_sides == "2-Sided Card":
                back_photo = st.camera_input("📸 Capture Back Side")
                if back_photo:
                    img_back_bytes = back_photo.getvalue()
    else:
        with col1:
            front_file = st.file_uploader("📁 Front Side Image (Click to snap/upload)", type=["jpg", "jpeg", "png"])
            if front_file:
                img_front_bytes = front_file.read()
                st.image(img_front_bytes, caption="Front Side Photo Loaded", use_container_width=True)
                
        with col2:
            if card_sides == "2-Sided Card":
                back_file = st.file_uploader("📁 Back Side Image (Click to snap/upload)", type=["jpg", "jpeg", "png"])
                if back_file:
                    img_back_bytes = back_file.read()
                    st.image(img_back_bytes, caption="Back Side Photo Loaded", use_container_width=True)

    # ANALYSIS UPDATE 2: Changed logical evaluations to process unified bytes from camera OR file uploader
    if img_front_bytes and (card_sides == "1-Side Only" or img_back_bytes is not None):
        if st.button("⚡ Step 2: Analyze with Local AI"):
            with st.spinner("OCR reading text strings and Local AI parsing layout..."):
                # Extract text from whatever images are provided
                text_front = process_ocr(img_front_bytes)
                text_back = process_ocr(img_back_bytes) if img_back_bytes else ""
                combined_text = f"{text_front}\n{text_back}"
                
                # Pass strings to local model
                ai_results = parse_with_local_llm(combined_text)
                if ai_results:
                    # Save results in temporary app state memory for editing stage
                    st.session_state['temp_ai_data'] = ai_results
                    st.session_state['front_bytes'] = img_front_bytes
                    st.session_state['back_bytes'] = img_back_bytes
                    st.success("AI Analysis Complete! Review details below.")

    # STEP 3: INTERMEDIATE VERIFICATION STAGE (Manual Override Fields)
    if 'temp_ai_data' in st.session_state:
        st.markdown("---")
        st.subheader("📝 Step 3: Review & Edit Details (Manual Override)")
        st.caption("Feel free to correct any spelling mistakes or adjust categorization tags below.")
        
        saved_data = st.session_state['temp_ai_data']
        
        # ANALYSIS UPDATE 3: Structured inside a form block to prevent mobile app refresh lockups
        with st.form("review_form"):
            edit_name = st.text_input("Name", value=saved_data.get("Name"))
            edit_title = st.text_input("Job Title", value=saved_data.get("Job_Title"))
            edit_company = st.text_input("Company Name", value=saved_data.get("Company"))
            edit_phone = st.text_input("Phone Number", value=saved_data.get("Phone"))
            edit_email = st.text_input("Email Address", value=saved_data.get("Email"))
            edit_address = st.text_area("Physical Address", value=saved_data.get("Address"))
            
            # Sector drop-down selections
            sectors_list = ["Hardware", "Software", "Printer", "Finance", "Medical", "Consulting", "Real Estate", "Other"]
            ai_sector = saved_data.get("Sector")
            default_index = sectors_list.index(ai_sector) if ai_sector in sectors_list else len(sectors_list)-1
            
            edit_sector = st.selectbox("Business Sector", sectors_list, index=default_index)
            
            # Allow manual override for custom sector names if "Other" is picked
            custom_sector = st.text_input("If 'Other', type custom sector here:")
                
            edit_remarks = st.text_area("Remarks / Custom Networking Notes", value=saved_data.get("Remarks"))
            
            # Form submission action button
            submit_button = st.form_submit_button("💾 Save Finalized Data to CRM Database")

        if submit_button:
            final_sector = custom_sector if edit_sector == "Other" and custom_sector else edit_sector
            final_payload = {
                "Name": edit_name, "Job_Title": edit_title, "Company": edit_company,
                "Phone": edit_phone, "Email": edit_email, "Address": edit_address,
                "Sector": final_sector, "Remarks": edit_remarks
            }
            # Inject data + raw binary image blobs straight into storage
            save_to_db(final_payload, st.session_state['front_bytes'], st.session_state['back_bytes'])
            st.balloons()
            st.success(f"Successfully added {edit_name} from {edit_company} to your Local CRM Vault!")
            
            # Wipe temporary memory to clear out form view and refresh dashboard state
            del st.session_state['temp_ai_data']
            st.rerun()

with tab2:
    st.subheader("📂 Contact Vault Dashboard")
    records = get_all_cards()
    
    if records:
        for row in records:
            id_val, name, title, company, phone, email, address, sector, remarks, img_f, img_b = row
            
            # Group every card inside an expandable dashboard layout card
            with st.expander(f"👤 {name} | 🏢 {company} | 🏷️ {sector}"):
                c1, c2, c3 = st.columns([1, 1, 1])
                with c1:
                    st.markdown(f"**Title:** {title}")
                    st.markdown(f"**Phone:** {phone}")
                    st.markdown(f"**Email:** {email}")
                    st.markdown(f"**Address:** {address}")
                with c2:
                    st.markdown(f"**Sector:** `{sector}`")
                    st.markdown(f"**Your Remarks:** *{remarks}*")
                with c3:
                    sub_col1, sub_col2 = st.columns(2)
                    with sub_col1:
                        if img_f:
                            st.image(Image.open(io.BytesIO(img_f)), caption="Front Side Photo", use_container_width=True)
                    with sub_col2:
                        if img_b:
                            st.image(Image.open(io.BytesIO(img_b)), caption="Back Side Photo", use_container_width=True)
    else:
        st.info("The CRM Vault is empty. Head over to the first tab and scan a business card!")