import pdfplumber
import OpenAIHelper
def extract_text_from_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        all_text = ""
        for page in pdf.pages:
            all_text += page.extract_text()
    return all_text
# resume_text=extract_text_from_pdf(r"C:\Users\dhruv\OneDrive\Desktop\dhruv_creds\resume.pdf")
# prompt = f"""
#     I am an Applicant Tracking System (ATS). Please review the following resume and decide if the candidate qualifies for the job based on the following criteria:
#     1. Experience with Python and JavaScript
#     2. Minimum 2 Internships
#     3. A degree in Computer Science or a related field.

#     Resume:
#     {resume_text}

#     Respond with "ACCEPT" if the resume meets the criteria, otherwise respond with "REJECT".
#     """
# response = OpenAIHelper.call_openai_api(prompt)
# if response and "choices" in response:
#     answer = response["choices"][0]["message"]["content"]
#     answer = answer.replace('#', '')
#     print(answer)
