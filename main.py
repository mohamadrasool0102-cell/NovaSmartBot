from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from ai import ai_response

import os
import json
import asyncio


TOKEN = os.getenv("BOT_TOKEN")

USERS_FILE = "users.json"


def load_users():
    if not os.path.exists(USERS_FILE):
        return {}

    with open(USERS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_user(user):
    users = load_users()

    users[str(user.id)] = {
        "id": user.id,
        "name": user.first_name,
        "username": user.username
    }

    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(
            users,
            f,
            ensure_ascii=False,
            indent=4
        )


def menu():
    buttons = [
        ["🧠 هوش مصنوعی"],
        ["👤 پروفایل", "🌍 ترجمه"],
        ["☁️ آب‌وهوا"]
    ]

    return ReplyKeyboardMarkup(
        buttons,
        resize_keyboard=True
    )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    save_user(user)

    await update.message.reply_text(
        f"سلام {user.first_name} 👋\n"
        "به NovaAI خوش آمدید 🤖\n\n"
        "یک گزینه را انتخاب کن:",
        reply_markup=menu()
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - شروع\n/help - راهنما"
    )


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "👤 پروفایل":
        user = update.effective_user

        await update.message.reply_text(
            f"👤 پروفایل شما\n\n"
            f"نام: {user.first_name}\n"
            f"شناسه: {user.id}\n"
            f"وضعیت: رایگان"
        )

    elif text == "🧠 هوش مصنوعی":
        await update.message.reply_text(
            "🧠 NovaAI فعال است.\n"
            "سوالت را بپرس 🤖"
        )

    elif text == "🌍 ترجمه":
        await update.message.reply_text(
            "🌍 بخش ترجمه به زودی فعال می‌شود."
        )

    elif text == "☁️ آب‌وهوا":
        await update.message.reply_text(
            "☁️ بخش آب‌وهوا به زودی فعال می‌شود."
        )

    else:
        answer = ai_response(text)

        await update.message.reply_text(answer)


async def run_bot():

    if not TOKEN:
        raise RuntimeError(
            "BOT_TOKEN environment variable is not set."
        )

    app = Application.builder().token(TOKEN).build()

    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        CommandHandler("help", help_command)
    )

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            message_handler
        )
    )

    print("NovaAI is running...")

    await app.initialize()
    await app.start()
    await app.updater.start_polling()

    try:
        while True:
            await asyncio.sleep(3600)

    finally:
        await app.updater.stop()
        await app.stop()
        await app.shutdown()


if __name__ == "__main__":
    asyncio.run(run_bot())
