from telegram import Update
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
from datetime import datetime


TOKEN = os.getenv("BOT_TOKEN")

USERS_FILE = "users.json"


def load_users():
    try:
        with open(USERS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}


def save_users(users):
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=4)


def save_user(user):
    users = load_users()
    uid = str(user.id)

    if uid not in users:
        users[uid] = {
            "name": user.first_name,
            "username": user.username or "ندارد",
            "joined": str(datetime.now())
        }
        save_users(users)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    save_user(update.effective_user)

    await update.message.reply_text(
        "سلام 👋\n"
        "به NovaSmartBot خوش آمدید 🤖\n\n"
        "برای دیدن پروفایل خودت بزن:\n"
        "/profile"
    )


async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    users = load_users()
    uid = str(update.effective_user.id)

    if uid in users:
        user = users[uid]

        await update.message.reply_text(
            f"👤 پروفایل شما\n\n"
            f"نام: {user['name']}\n"
            f"یوزرنیم: @{user['username']}\n"
            f"تاریخ ورود: {user['joined']}"
        )
    else:
        await update.message.reply_text(
            "اول /start رو بزن 👋"
        )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - شروع\n"
        "/profile - پروفایل\n"
        "/help - راهنما"
    )


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:

        text = update.message.text

        answer = ai_response(text)

        await update.message.reply_text(answer)


async def run_bot():

    if not TOKEN:
        raise RuntimeError(
            "BOT_TOKEN environment variable is not set."
        )

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("profile", profile))
    app.add_handler(CommandHandler("help", help_command))

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            message_handler
        )
    )

    print("NovaSmartBot is running...")

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