def load_resume(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def find_matches(resume_text, keywords):
    return [kw for kw in keywords if kw.lower() in resume_text.lower()]
