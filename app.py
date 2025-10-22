from flask import Flask, render_template, request
import PyPDF2
import re
import os

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Important sections and keywords to check
SECTIONS = ["objective", "summary", "education", "skills", "experience", "projects", "certifications"]
KEYWORDS = ["python", "data", "machine learning", "sql", "communication", "leadership", "ai", "flask", "html", "css"]

def extract_text_from_pdf(pdf_file):
    try:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text.lower()
    except Exception as e:
        print(f"Error extracting PDF: {e}")
        return ""

def analyze_resume(text):
    missing_sections = [sec for sec in SECTIONS if sec not in text]
    found_keywords = [kw for kw in KEYWORDS if kw in text]
    missing_keywords = [kw for kw in KEYWORDS if kw not in text]
    return missing_sections, found_keywords, missing_keywords

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            file = request.files.get("resume")
            if not file or file.filename == '':
                return render_template("index.html", error="Please upload a file.")
            
            ext = os.path.splitext(file.filename)[1].lower()
            if ext not in ['.pdf', '.txt']:
                return render_template("index.html", error="Only PDF and TXT files are supported.")
            
            if ext == ".pdf":
                text = extract_text_from_pdf(file)
            else:
                text = file.read().decode("utf-8", errors='ignore').lower()

            if not text or len(text.strip()) < 10:
                return render_template("index.html", error="Could not extract text from the file. Please ensure it's a valid resume.")

            missing_sections, found_keywords, missing_keywords = analyze_resume(text)
            
            return render_template("result.html",
                                   missing_sections=missing_sections,
                                   found_keywords=found_keywords,
                                   missing_keywords=missing_keywords)
        except Exception as e:
            print(f"Error processing file: {e}")
            return render_template("index.html", error="An error occurred while processing your resume. Please try again.")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
