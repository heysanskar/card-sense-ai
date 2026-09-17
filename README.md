📇 CardSense AI
<br>
Local AI-Powered Business Card Scanner & CRM
CardSense AI is a local AI-powered business card digitization and CRM application built with Streamlit.
It allows users to capture or upload business card images, extract text using EasyOCR, and use Phi-3 through Ollama to intelligently convert the extracted text into structured contact information.

Before saving the information, users can review and manually correct the AI-generated details. The finalized contact information and original card images are then stored in a local SQLite database.

<br>
🚀 Features
📸 Capture business cards using a camera
📁 Upload business card images
🔄 Support for one-sided and two-sided cards
🔍 Extract text using EasyOCR
🤖 Extract structured information using Phi-3
🏠 Run AI locally using Ollama
👤 Extract:
Name
Job Title
Company
Phone Number
Email
Address
Business Sector
Remarks
✏️ Review and edit AI-generated information
💾 Store contact information in SQLite
🖼️ Store front and back card images
🗄️ View saved contacts in a CRM-style dashboard
🔐 Local-first processing without requiring an external AI API
<br>
🧠 How It Works
The application follows this pipeline:
Business Card Image
        │
        ▼
   Image Decoding
        │
        ▼
      EasyOCR
        │
        ▼
   Extracted Text
        │
        ▼
   Phi-3 via Ollama
        │
        ▼
   Structured JSON
        │
        ▼
 Human Verification
        │
        ▼
      SQLite

1. 📸 Capture or Upload
The user can either capture a card using the camera or upload an existing image.
The application supports both:

One-sided business cards
Two-sided business cards
2. 🔍 OCR Text Extraction
EasyOCR reads the text present on the business card.
Example:

Rahul Sharma
Senior Software Engineer
ABC Technologies Pvt Ltd
+91 XXXXX XXXXX
rahul@example.com
Gurugram, Haryana

3. 🤖 AI Processing
The extracted OCR text is sent to Phi-3 running locally through Ollama.
The model identifies the different pieces of information and returns structured JSON.

Example:

{
  "Name": "Rahul Sharma",
  "Job_Title": "Senior Software Engineer",
  "Company": "ABC Technologies Pvt Ltd",
  "Phone": "+91 XXXXX XXXXX",
  "Email": "rahul@example.com",
  "Address": "Gurugram, Haryana",
  "Sector": "Software",
  "Remarks": "Works in the software technology sector."
}

4. ✏️ Human Verification
The extracted information is displayed in an editable form.
The user can correct inaccurate OCR or AI-generated information before saving it.

This creates a human-in-the-loop verification process, ensuring that the user has control over the final contact information.

5. 💾 Database Storage
After verification, the application stores the finalized contact information and original front/back card images in a local SQLite database.
<br>
🛠️ Tech Stack<br>
Technology	Purpose<br>
Python	Application development<br>
Streamlit	Web interface<br>
EasyOCR	Text extraction from card images
OpenCV	Image decoding and processing<br>
Ollama	Local LLM runtime<br>
Phi-3	AI-based information extraction<br>
SQLite	Local contact database<br>
NumPy	Image byte processing<br>
Pillow	Image handling and display<br>
Requests	Communication with Ollama API<br>

<br>
📂 Project Structure<br>
card-sense-ai/<br>
│
├── app.py<br>
├── requirements.txt<br>
├── README.md<br>
├── .gitignore<br>
└── LICENSE<br>

The SQLite database is generated locally when the application runs and should not be committed to GitHub.
<br>
⚙️ Installation<br>
📋 Prerequisites<br>
Make sure you have:<br>
Python 3.9+<br>
Ollama<br>
Git<br>
1. Clone the Repository<br>
git clone https://github.com/YOUR_USERNAME/card-sense-ai.git<br>
cd card-sense-ai<br>

2. Create a Virtual Environment<br>
python -m venv venv<br>

Windows<br>
venv\Scripts\activate<br>

macOS / Linux<br>
source venv/bin/activate<br>

3. Install Python Dependencies<br>
pip install -r requirements.txt<br>

4. Install the Phi-3 Model<br>
Make sure Ollama is installed and running.<br>
Download the Phi-3 model:<br>

ollama pull phi3<br>

Verify that the model is available:<br>
ollama list<br>

5. Run the Application<br>
streamlit run app.py<br>

The application will open in your browser.<br>
<br>
🔒 Privacy<br>
CardSense AI follows a local-first approach.<br>
The application uses:<br>

🔍 Local EasyOCR processing<br>
🤖 Local Phi-3 inference through Ollama<br>
💾 Local SQLite storage<br>
🏠 Local application processing<br>
No external AI API is required for the core extraction workflow.<br>
⚠️ Users should protect the local SQLite database because it may contain personal contact information. Do not commit real contact data or business-card images to a public repository.<br>
<br>
🎯 Project Objective<br>
The objective of CardSense AI is to automate the process of converting physical business cards into digital contact records.<br>
Instead of manually entering information from every card, CardSense AI combines:

OCR → Local LLM → Structured JSON → Human Verification → Database Storage<br>

The project demonstrates how AI can be integrated into a practical application while keeping the user involved in verifying AI-generated information.<br>

<br>
⭐ Key Highlights<br>
🔍 OCR-based text extraction using EasyOCR<br>
🤖 Local LLM integration using Phi-3 and Ollama<br>
🧠 Prompt engineering for structured information extraction<br>
📋 Conversion of unstructured OCR text into JSON<br>
✏️ Human verification before database insertion<br>
💾 SQLite-based persistent contact storage<br>
🖼️ Storage of original front and back card images<br>
📸 Camera and file-upload workflows<br>
🗄️ CRM-style contact management interface<br>
🔐 Local-first AI processing<br>
<br>
🔮 Future Improvements
🔎 Search & Filter Contacts — Search contacts by name, company, email, phone, or business sector.<br>
✏️ Edit Existing Contacts — Update contact information directly from the CRM vault.<br>
🗑️ Delete Contacts — Remove outdated or unwanted contacts.<br>
🔄 Duplicate Detection — Identify potential duplicate contacts using name, company, email, and phone number.<br>
📤 Export Contacts — Export contact information to CSV or Excel.<br>
📇 vCard Export — Generate .vcf files for importing contacts into phone address books.<br>
🏷️ Advanced Contact Tagging — Add custom tags and categories for better organization.<br>
📊 CRM Analytics Dashboard — Display statistics such as contacts by sector and recently added contacts.<br>
🌐 Multi-language OCR — Support business cards containing multiple languages.<br>
🧠 Improved Image Preprocessing — Add image enhancement, perspective correction, noise reduction, and automatic card cropping.<br>
🤖 Improved AI Validation — Add stronger validation for incomplete or ambiguous OCR results.<br>
🔐 User Authentication — Add user accounts and user-specific contact databases.<br>
🔒 Database Security — Add encryption and stronger protection for locally stored contact information.<br>
📱 Mobile UI Optimization — Improve the camera workflow and layout for mobile devices.<br>
<br>
📚 Key Concepts Demonstrated
This project demonstrates practical implementation of:<br>
Optical Character Recognition (OCR)<br>
Local Large Language Models (LLMs)<br>
Prompt Engineering<br>
Structured JSON Generation<br>
REST API Integration<br>
Streamlit Application Development<br>
SQLite Database Management<br>
Image BLOB Storage<br>
Human-in-the-Loop AI<br>
Session State Management<br>
Local AI Inference<br>
Image Processing<br>
<br>

👨‍💻 Author

Sanskar Aman

GitHub: https://github.com/heysanskar

LinkedIn: https://www.linkedin.com/in/sanskar-a-881719248/

<br>
⭐ If you find this project useful, consider giving it a star!
