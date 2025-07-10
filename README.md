# Internship Job Portal

A simple and scalable web portal that allows students to browse internship openings and apply using their resumes. The platform includes a built-in ATS Checker to evaluate whether a candidate’s resume is likely to be shortlisted for a specific role.

Deployed on AWS EC2 and equipped with a CI/CD pipeline using AWS CodePipeline, this project ensures quick deployment and a smooth user experience.

---

## Project Overview

- Students can view and apply to internships
- Candidates can upload resumes
- A built-in ATS Checker evaluates resume-job fit and gives a match score
- Recruiters can post internship openings
- Hosted on AWS with CI/CD using AWS CodePipeline

---

## Tech Stack

### Backend & Logic
- Python
- Flask
- SQLite

### Cloud Infrastructure
- AWS EC2
- AWS Lambda
- AWS CodePipeline

---

## ATS Checker Functionality

Before applying, candidates can upload their resume and the platform will:

- Extract text and skills from the resume
- Compare it with job description keywords
- Return a match score out of 100
- Help users improve resume relevance
