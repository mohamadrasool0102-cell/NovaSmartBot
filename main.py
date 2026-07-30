from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

from config import BOT_TOKEN


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام 👋\n"
        "به NovaSmartBot خوش اومدی 🤖\n\n"
        "من آماده‌ام کمکت کنم."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "راهنما 📌\n\n"
        "/start - شروع ربات\n"
        "/help - راهنما\n\n"
        "پیامت رو بفرست تا جواب بدم."
    )


async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    text = update.message.text.lower()

    if "سلام" in text or "درود" in text:
        answer = "سلام 👋 خوش اومدی، چطور می‌تونم کمکت کنم؟"

    elif "خوبی" in text or "چطوری" in text:
        answer = "خوبم 😎 آماده‌ام کمک کنم."

    elif "اسم" in text:
        answer = "من NovaSmartBot هستم 🤖"

    elif "سازنده" in text:
        answer = "من توسط یک برنامه‌نویس ساخته شدم 🚀"

    elif "خداحافظ" in text:
        answer = "موفق باشی 👋 هر وقت خواستی برگرد."

    else:
        answer = (
            "پیامت رو دریافت کردم ✅\n\n"
            "فعلاً در حال یادگیری هستم 🤖"
        )

    await update.message.reply_text(answer)


def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN تنظیم نشده")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, chat)
    )

    print("NovaSmartBot is running...")

    app.run_polling()


if __name__ == "__main__":
    main()