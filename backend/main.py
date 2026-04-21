from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

from scraper import extract_text
from ai_engine import summarize_text, classify_text, scam_check

app = FastAPI()

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def home():
    return {
        "message": "🧠 AI Link Intelligence Tool is running",
        "usage": "/analyze?url=YOUR_URL"
    }
@app.get("/analyze")
def analyze(url: str = Query(..., description="URL to analyze")):
    try:
        # 1. Extract content
        text = extract_text(url)

        # 2. AI processing
        summary = summarize_text(text)
        category = classify_text(text)

        # 3. Safety check (URL-based is better)
        safety = scam_check(url)

        return {
            "url": url,
            "summary": summary,
            "category": category,
            "url_safety": safety
        }

    except Exception as e:
        return {
            "error": str(e),
            "url": url
        }
