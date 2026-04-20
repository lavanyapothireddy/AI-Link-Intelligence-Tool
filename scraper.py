import requests
from bs4 import BeautifulSoup
from readability import Document

def extract_text(url):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    response = requests.get(url, headers=headers, timeout=10)
    html = response.text

    doc = Document(html)
    clean_html = doc.summary()

    soup = BeautifulSoup(clean_html, "html.parser")
    text = soup.get_text(separator=" ", strip=True)

    return text[:3000]