import json
import os

ANSWERS_FILE = "answers.json"


def load_answers():
    if not os.path.exists(ANSWERS_FILE):
        return {}

    try:
        with open(ANSWERS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, dict) else {}

    except Exception:
        return {}


def ai_response(message):
    text = message.lower().strip()

    answers = load_answers()

    # جواب‌های ذخیره شده
    if text in answers:
        return answers[text]

    # جواب‌های پایه
    if any(x in text for x in ["سلام", "درود", "hello", "hi"]):
        return "سلام 👋 من NovaAI هستم 🤖\nچطور می‌تونم کمکت کنم؟"

    if "اسمت" in text or "اسم تو" in text or "name" in text:
        return "من NovaAI هستم 🤖"

    if "خوبی" in text or "حالت" in text:
        return "خوبم 😄 آماده کمک هستم."

    if "چه کار" in text or "کمک" in text:
        return "می‌تونم به سوالاتت جواب بدم و کمکت کنم 🚀"

    if "خداحافظ" in text or "bye" in text:
        return "خداحافظ 👋 دوباره برگرد."

    return (
        "🤖 هنوز جواب این سوال رو یاد نگرفتم.\n"
        "به مرور بهتر می‌شم."
    )
