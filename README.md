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
🛠️ Tech Stack
Technology	Purpose
Python	Application development
Streamlit	Web interface
EasyOCR	Text extraction from card images
OpenCV	Image decoding and processing
Ollama	Local LLM runtime
Phi-3	AI-based information extraction
SQLite	Local contact database
NumPy	Image byte processing
Pillow	Image handling and display
Requests	Communication with Ollama API

<br>
📂 Project Structure
card-sense-ai/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE

The SQLite database is generated locally when the application runs and should not be committed to GitHub.
<br>
⚙️ Installation
📋 Prerequisites
Make sure you have:
Python 3.9+
Ollama
Git
1. Clone the Repository
git clone https://github.com/YOUR_USERNAME/card-sense-ai.git
cd card-sense-ai

2. Create a Virtual Environment
python -m venv venv

Windows
venv\Scripts\activate

macOS / Linux
source venv/bin/activate

3. Install Python Dependencies
pip install -r requirements.txt

4. Install the Phi-3 Model
Make sure Ollama is installed and running.
Download the Phi-3 model:

ollama pull phi3

Verify that the model is available:
ollama list

5. Run the Application
streamlit run app.py

The application will open in your browser.
<br>
🔒 Privacy
CardSense AI follows a local-first approach.
The application uses:

🔍 Local EasyOCR processing
🤖 Local Phi-3 inference through Ollama
💾 Local SQLite storage
🏠 Local application processing
No external AI API is required for the core extraction workflow.
⚠️ Users should protect the local SQLite database because it may contain personal contact information. Do not commit real contact data or business-card images to a public repository.
<br>
🎯 Project Objective
The objective of CardSense AI is to automate the process of converting physical business cards into digital contact records.
Instead of manually entering information from every card, CardSense AI combines:

OCR → Local LLM → Structured JSON → Human Verification → Database Storage

The project demonstrates how AI can be integrated into a practical application while keeping the user involved in verifying AI-generated information.

<br>
⭐ Key Highlights
🔍 OCR-based text extraction using EasyOCR
🤖 Local LLM integration using Phi-3 and Ollama
🧠 Prompt engineering for structured information extraction
📋 Conversion of unstructured OCR text into JSON
✏️ Human verification before database insertion
💾 SQLite-based persistent contact storage
🖼️ Storage of original front and back card images
📸 Camera and file-upload workflows
🗄️ CRM-style contact management interface
🔐 Local-first AI processing
<br>
🔮 Future Improvements
🔎 Search & Filter Contacts — Search contacts by name, company, email, phone, or business sector.
✏️ Edit Existing Contacts — Update contact information directly from the CRM vault.
🗑️ Delete Contacts — Remove outdated or unwanted contacts.
🔄 Duplicate Detection — Identify potential duplicate contacts using name, company, email, and phone number.
📤 Export Contacts — Export contact information to CSV or Excel.
📇 vCard Export — Generate .vcf files for importing contacts into phone address books.
🏷️ Advanced Contact Tagging — Add custom tags and categories for better organization.
📊 CRM Analytics Dashboard — Display statistics such as contacts by sector and recently added contacts.
🌐 Multi-language OCR — Support business cards containing multiple languages.
🧠 Improved Image Preprocessing — Add image enhancement, perspective correction, noise reduction, and automatic card cropping.
🤖 Improved AI Validation — Add stronger validation for incomplete or ambiguous OCR results.
🔐 User Authentication — Add user accounts and user-specific contact databases.
🔒 Database Security — Add encryption and stronger protection for locally stored contact information.
📱 Mobile UI Optimization — Improve the camera workflow and layout for mobile devices.
<br>
📚 Key Concepts Demonstrated
This project demonstrates practical implementation of:
Optical Character Recognition (OCR)
Local Large Language Models (LLMs)
Prompt Engineering
Structured JSON Generation
REST API Integration
Streamlit Application Development
SQLite Database Management
Image BLOB Storage
Human-in-the-Loop AI
Session State Management
Local AI Inference
Image Processing
<br>
👨‍💻 Author
Sanskar Aman
GitHub: https://github.com/heysanskar
LinkedIn: https://www.linkedin.com/in/sanskar-a-881719248/

<br>
⭐ If you find this project useful, consider giving it a star!
