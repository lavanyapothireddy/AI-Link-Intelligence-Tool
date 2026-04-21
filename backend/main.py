from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from scraper import extract_text
from ai_engine import summarize_text, classify_text, scam_check

app = FastAPI()

# Allow frontend calls
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "🧠 AI Link Intelligence Tool is running"}

@app.get("/analyze")
def analyze(url: str):
    try:
        text = extract_text(url)

        summary = summarize_text(text)
        category = classify_text(text)
        safety = scam_check(text)

        return {
            "url": url,
            "summary": summary,
            "category": category,
            "url_safety": safety
        }

    except Exception as e:
        return {
            "error": str(e)
        }
