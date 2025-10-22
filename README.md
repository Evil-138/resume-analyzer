# 💼 AI Resume Analyzer

An intelligent web application that helps users optimize their resumes automatically by analyzing key sections and keywords.

## ✨ Features

- 📤 **Upload Resume**: Support for PDF and TXT formats
- 🧠 **Smart Analysis**: Automatically extracts and analyzes resume content
- 🔍 **Section Detection**: Checks for essential resume sections (Objective, Education, Skills, Experience, Projects, Certifications)
- 🧩 **Keyword Matching**: Identifies important keywords and suggests missing ones
- 📊 **Detailed Report**: Generates comprehensive feedback with actionable insights
- 🎨 **Beautiful UI**: Modern dark-neon theme with responsive design
- ☁️ **Cloud Ready**: Easy deployment on Render or other platforms

## 🧩 Tech Stack

- **Frontend**: HTML, CSS (with Google Fonts)
- **Backend**: Flask (Python)
- **PDF Processing**: PyPDF2
- **Text Analysis**: Python regex and keyword matching
- **Hosting**: Render (or any platform supporting Flask)

## 📁 Project Structure

```
ai-resume-analyzer/
│
├── app.py                 # Flask backend application
├── templates/
│   ├── index.html        # Upload page
│   └── result.html       # Analysis results page
│
├── static/
│   └── style.css         # Styling with dark-neon theme
│
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## 🚀 Installation & Setup

### 1. Clone the repository

```bash
cd "d:\resume analyzer"
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

The application will be available at `http://localhost:5000`

## 🌐 Deployment on Render

1. Create a new Web Service on [Render](https://render.com)
2. Connect your GitHub repository
3. Use the following settings:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
4. Deploy!

## 📝 How It Works

1. **Upload**: User uploads a resume (PDF or TXT)
2. **Extract**: Text is extracted from the document
3. **Analyze**: The system checks for:
   - Essential sections (Objective, Education, Skills, etc.)
   - Important keywords (Python, Data Science, Leadership, etc.)
4. **Report**: User receives detailed feedback:
   - ✅ Sections that are present
   - ❌ Missing sections
   - ✨ Found keywords
   - 💡 Suggested keywords to add

## 🎯 Analyzed Sections

- Objective / Summary
- Education
- Skills
- Experience
- Projects
- Certifications

## 🔑 Important Keywords

The analyzer looks for relevant keywords including:
- Technical: Python, Data, Machine Learning, SQL, AI, Flask, HTML, CSS
- Soft Skills: Communication, Leadership

## 🛠️ Customization

You can easily customize the analyzer by modifying the lists in `app.py`:

```python
SECTIONS = ["objective", "summary", "education", "skills", "experience", "projects", "certifications"]
KEYWORDS = ["python", "data", "machine learning", "sql", "communication", "leadership", "ai", "flask", "html", "css"]
```

## 📄 License

This project is open source and available for educational purposes.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 💡 Future Enhancements

- AI-powered suggestions using NLP
- Resume scoring system
- Multiple language support
- Export analysis reports as PDF
- Resume templates library
- ATS (Applicant Tracking System) compatibility check

---

Made with ❤️ and ☕
