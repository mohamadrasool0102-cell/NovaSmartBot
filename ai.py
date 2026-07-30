import json
import os

ANSWERS_FILE = "answers.json"


def load_answers():
    if not os.path.exists(ANSWERS_FILE):
        return {}

    with open(ANSWERS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def ai_response(message):
    text = message.lower()

    answers = load_answers()

    if text in answers:
        return answers[text]

    if "سلام" in text or "hello" in text:
        return "سلام 👋 من NovaAI هستم، چطور کمکت کنم؟"

    if "اسم" in text or "name" in text:
        return "من NovaAI هستم 🤖"

    if "خوبی" in text or "how are you" in text:
        return "خوبم، آماده کمک هستم 🚀"

    return "هنوز جواب این سوال رو یاد نگرفتم 🤔"
