from flask import Flask, render_template, request
import PyPDF2
import re
import os

app = Flask(__name__)

# Important sections and keywords to check
SECTIONS = ["objective", "summary", "education", "skills", "experience", "projects", "certifications"]
KEYWORDS = ["python", "data", "machine learning", "sql", "communication", "leadership", "ai", "flask", "html", "css"]

def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text.lower()

def analyze_resume(text):
    missing_sections = [sec for sec in SECTIONS if sec not in text]
    found_keywords = [kw for kw in KEYWORDS if kw in text]
    missing_keywords = [kw for kw in KEYWORDS if kw not in text]
    return missing_sections, found_keywords, missing_keywords

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["resume"]
        if not file:
            return render_template("index.html", error="Please upload a file.")
        
        ext = os.path.splitext(file.filename)[1].lower()
        if ext == ".pdf":
            text = extract_text_from_pdf(file)
        else:
            text = file.read().decode("utf-8").lower()

        missing_sections, found_keywords, missing_keywords = analyze_resume(text)
        
        return render_template("result.html",
                               missing_sections=missing_sections,
                               found_keywords=found_keywords,
                               missing_keywords=missing_keywords)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
