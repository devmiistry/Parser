import ollama

def generate_cover_letter(job_text, resume_text):
    print("🧠 Sending request to local model...")

    prompt = (
        "Write a professional, tailored cover letter for the job below using the provided resume.\n\n"
        f"Job Description:\n{job_text}\n\n"
        f"My Resume:\n{resume_text}\n\n"
        "Cover Letter:"
    )

    try:
        response = ollama.chat(
            model="mistral",  # Try 'phi3' if this feels slow
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        print("✅ Response received!")
        return response['message']['content']

    except Exception as e:
        print("❌ Error from model:", e)
        return "Error: Could not generate cover letter."
