# generate_cover_letter.py
import ollama

def generate_cover_letter(job_text, resume_text, model="mistral"):
    prompt = (
        "Write a professional, tailored cover letter for the following job using the provided resume.\n\n"
        f"Job Description:\n{job_text}\n\n"
        f"My Resume:\n{resume_text}\n\n"
        "Tailored Cover Letter:"
    )

    response = ollama.chat(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )

    return response['message']['content']
