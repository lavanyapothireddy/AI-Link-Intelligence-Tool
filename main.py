from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from scraper import extract_text
from ai_engine import summarize_text, classify_text, scam_check

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/analyze")
def analyze(url: str):

    text = extract_text(url)

    summary = summarize_text(text)

    return {
        "url": url,
        "summary": summary,
        "category": classify_text(text),
        "url_safety": scam_check(text)
    }