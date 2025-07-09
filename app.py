from flask import Flask, render_template, request, jsonify
from flask import send_from_directory, url_for
import os
import pdf_text_extraction
import OpenAIHelper

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Internship Data (you can replace this with database or API calls)
internships = [
    {"title": "Software Developer Intern", "company": "TechCorp", "duration": "3 months", "location": "Remote"},
    {"title": "Data Scientist Intern", "company": "DataLab", "duration": "6 months", "location": "On-site"},
    {"title": "UX/UI Designer Intern", "company": "Design Studios", "duration": "4 months", "location": "Remote"}
]

# Home route serving the internship portal
@app.route('/')
def index():
    return render_template('index.html', internships=internships)

@app.route('/ats')
def ats():
    return render_template('aws_frontend.html', internships=internships)

# Upload Resume Route
@app.route('/upload_resume', methods=['POST'])
def upload_resume():
    # Get the file from the request
    resume = request.files['resume']
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], resume.filename)
    resume.save(file_path)

    # Extract text from the uploaded PDF
    resume_text = pdf_text_extraction.extract_text_from_pdf(file_path)

    prompt = f"""
    I am an Applicant Tracking System (ATS). Please review the following resume and decide if the candidate qualifies for the job based on the following criteria:
    1. Experience with DBMS and JavaScript
    2. Minimum 2 Internships
    3. A degree in Computer Science or a related field.

    Resume:
    {resume_text}

    Respond with "ACCEPT" if the resume meets the criteria, otherwise respond with "REJECT".
    """
    response = OpenAIHelper.call_openai_api(prompt)
    if response and "choices" in response:
        answer = response["choices"][0]["message"]["content"]
        answer = answer.replace('#', '')

    # Return the decision along with the file URL in JSON format
    pdf_url = url_for('uploaded_file', filename=resume.filename)
    return jsonify({"decision": answer, "file_url": pdf_url})

# Route to serve the uploaded PDF file
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
