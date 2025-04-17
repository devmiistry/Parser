# app.py
import streamlit as st
import docx
import fitz  # PyMuPDF
from generate_cover_letter import generate_cover_letter

st.set_page_config(page_title="AI Cover Letter Generator", layout="centered")

st.title("📄 Tailored Cover Letter Generator")
st.write("Upload your resume (PDF or Word) and paste a job description.")

# Upload resume
uploaded_resume = st.file_uploader("Upload your resume (PDF or DOCX)", type=["pdf", "docx"])
job_description = st.text_area("Paste the job description here")

# Helper to extract resume text
def extract_text(file):
    if file.type == "application/pdf":
        doc = fitz.open(stream=file.read(), filetype="pdf")
        return "\n".join([page.get_text() for page in doc])
    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = docx.Document(file)
        return "\n".join([para.text for para in doc.paragraphs])
    return ""

# Generate
if uploaded_resume and job_description:
    resume_text = extract_text(uploaded_resume)

    if st.button("Generate Cover Letter 💌"):
        with st.spinner("Thinking..."):
            cover_letter = generate_cover_letter(job_description, resume_text)
        st.subheader("📬 Your Tailored Cover Letter")
        st.text_area("Cover Letter", cover_letter, height=400)
