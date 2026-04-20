def summarize_text(text):
    return text[:300] + "..."


def classify_text(text):
    text = text.lower()

    if any(word in text for word in ["ai", "machine learning", "neural"]):
        return "🤖 Tech Content"
    elif any(word in text for word in ["news", "report"]):
        return "📰 News"
    elif any(word in text for word in ["buy", "shop", "price"]):
        return "🛒 Shopping"
    else:
        return "📄 General"


def scam_check(text):
    text = text.lower()

    scam_words = [
        "win money", "lottery", "urgent payment",
        "bank details", "password", "click here"
    ]

    for word in scam_words:
        if word in text:
            return "⚠️ Suspicious URL"

    return "✅ Safe URL"