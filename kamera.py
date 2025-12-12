import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# --- SOZLAMALAR ---
# DIQQAT: Tokeningizni birovga bermang. Hozirgi tokeningiz internetga chiqib ketdi,
# imkon bo'lsa BotFather'dan yangilab olishni maslahat beraman.
API_TOKEN = '8395077251:AAFcjcN9wk03NF02FV08atn2bCL3N8xNKEI'
WEB_SITE_URL = 'https://abdurazoqov606.github.io/Video/'

# Har doim chiqadigan reklama matni
FOOTER_TEXT = (
    "\n\n📢 Bizning kanal: @abdurazoqov606"
    "\n👨‍💻 Bot yaratuvchisi: @abdurozoqov_edits"
)
# ------------------

# Loglarni sozlash
logging.basicConfig(level=logging.INFO)

# Botni ishga tushirish
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_name = message.from_user.first_name
    
    # Tugmani yaratish
    markup = InlineKeyboardMarkup()
    
    # 1-tugma: WebApp (Saytga kirish)
    btn_video = InlineKeyboardButton("🔥 BOOM (Saytga kirish)", web_app=WebAppInfo(url=WEB_SITE_URL))
    markup.add(btn_video)
    
    # 2-tugma: Kanalga o'tish
    btn_channel = InlineKeyboardButton("📢 Kanalimiz", url="https://t.me/abdurazoqov606")
    markup.add(btn_channel)

    # Xabar matni (Siz aytgandek o'zgartirildi)
    text = (
        f"👋 Salom, {user_name}!\n\n"
        f"Mana sizning linkingiz, buni boshqalarga tashlang va BOOM! 👇\n"
        f"{FOOTER_TEXT}"
    )
    
    await message.answer(text, reply_markup=markup)

@dp.message_handler(content_types=['text'])
async def echo_message(message: types.Message):
    # Foydalanuvchi nima yozsa ham javob qaytarish
    await message.answer(f"Bot ishlamoqda... {FOOTER_TEXT}")

if __name__ == '__main__':
    print("Bot 24/7 rejimida ishga tushdi...")
    executor.start_polling(dp, skip_updates=True)
