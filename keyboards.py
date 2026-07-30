from telegram import ReplyKeyboardMarkup

main_keyboard = ReplyKeyboardMarkup(
    [
        ["🤖 هوش مصنوعی", "🌍 ترجمه"],
        ["🌤️ آب‌وهوا", "👤 پروفایل"],
        ["ℹ️ درباره ربات", "❓ راهنما"]
    ],
    resize_keyboard=True,
    one_time_keyboard=False
)# NovaSmartBot