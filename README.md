📇 CardSense AI
Local AI-Powered Business Card Scanner & CRM
CardSense AI is a local AI-powered business card digitization and CRM application built with Streamlit.
It allows users to capture or upload business card images, extract text using EasyOCR, and use Phi-3 through Ollama to intelligently convert the extracted text into structured contact information.

Before saving the information, users can review and manually correct the AI-generated details. The finalized contact information and original card images are then stored in a local SQLite database.

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
🧠 How It Works
The application follows this pipeline:
Business Card Image
        │
        ▼
   OpenCV / NumPy
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

1. Capture or Upload
The user can either capture a card using the camera or upload an existing image.
The application supports both:

One-sided business cards
Two-sided business cards
2. OCR Text Extraction
EasyOCR reads the text present on the business card.
For example:

Rahul Sharma
Senior Software Engineer
ABC Technologies Pvt Ltd
+91 XXXXX XXXXX
rahul@example.com
Gurugram, Haryana

3. AI Processing
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

4. Human Verification
The extracted information is shown in an editable form.
The user can correct inaccurate OCR or AI results before saving them.

This creates a human-in-the-loop verification process.

5. Database Storage
After verification, the application stores the contact information and original card images in SQLite.
🛠️ Tech Stack
Technology	Purpose
Python	Application development
Streamlit	Web interface
EasyOCR	Text extraction from card images
OpenCV	Image processing
Ollama	Local LLM runtime
Phi-3	AI-based information extraction
SQLite	Local contact database
NumPy	Image byte processing
Pillow	Image handling and display
Requests	Communication with Ollama API

📂 Project Structure
card-sense-ai/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE

The SQLite database is generated locally when the application runs and should not be committed to GitHub.
⚙️ Installation
Prerequisites
Make sure you have:
Python 3.9+
Ollama
Git
1. Clone the repository
git clone https://github.com/YOUR_USERNAME/card-sense-ai.git
cd card-sense-ai

2. Create a virtual environment
python -m venv venv

Windows
venv\Scripts\activate

macOS / Linux
source venv/bin/activate

3. Install Python dependencies
pip install -r requirements.txt

4. Install the Phi-3 model
Make sure Ollama is installed and running.
Then run:

ollama pull phi3

Verify that the model is available:
ollama list

5. Run the application
streamlit run app.py

The application will open in your browser.
🔒 Privacy
CardSense AI is designed with a local-first approach.
The application uses:

Local EasyOCR processing
Local Phi-3 inference through Ollama
Local SQLite storage
No external AI API is required for the core extraction workflow.
However, users should protect the local database because it may contain personal contact information.

🎯 Project Objective
The objective of this project is to automate the process of converting physical business cards into digital contact records.
Instead of manually entering information from every card, CardSense AI combines OCR, local LLM processing, structured JSON extraction, and database storage into a single workflow.

The project also demonstrates how AI can be combined with human verification rather than automatically trusting every generated result.

🔮 Future Improvements
🔎 Search and filter contacts
✏️ Edit existing contacts
🗑️ Delete contacts
📊 Contact analytics dashboard
📤 Export contacts to CSV/Excel
📇 Export contacts as vCard
🔄 Duplicate contact detection
🏷️ Advanced contact tagging
🌐 Multi-language OCR
🧠 Improved image preprocessing
🔐 User authentication
🔒 Database encryption
📱 Improved mobile UI
📚 Key Concepts Demonstrated
This project demonstrates practical implementation of:
Optical Character Recognition (OCR)
Local Large Language Models (LLMs)
Prompt Engineering
Structured JSON generation
REST API integration
Streamlit application development
SQLite database management
Image BLOB storage
Human-in-the-loop AI
Session state management
Local AI inference
👨‍💻 Author
Sanskar Aman
GitHub: https://github.com/heysanskar

LinkedIn: https://www.linkedin.com/in/sanskar-a-881719248/

⭐ If you find this project useful, consider giving it a star!
