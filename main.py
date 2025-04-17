from parser import extract_keywords
from resume import load_resume, find_matches
from ai_helper import generate_cover_letter

def main():
    job_text = open("data/job_description.txt", "r", encoding="utf-8").read()
    resume_text = open("data/resume.txt", "r", encoding="utf-8").read()

    keywords = extract_keywords(job_text)
    matches = find_matches(resume_text, keywords)

    print("\n🎯 Extracted Keywords:")
    print(", ".join(keywords))

    print("\n✅ Keywords Found in Resume:")
    print(", ".join(matches))

    print("\n✍️ Generating tailored cover letter...")
    cover_letter = generate_cover_letter(job_text, resume_text)
    print("\n📄 Tailored Cover Letter:\n")
    print(cover_letter)

if __name__ == "__main__":
    main()
