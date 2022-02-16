from pyrogram import Client, filters

BOT_TOKEN = "5245470448:AAHJ0UqCVnuehEREuBqorI9NkzcQVU1K9KU" # your bot token from telegram.me/BotFather. Sample :- "12345:abcdefghijklmnop"
API_ID = "17356724" # your api id from my.telegram.org. Sample :- int("123456")
API_HASH = "1c41113550cbfb972d1b95721addf200" # your api hash from my.telegram.org Sample :- "fayasnoushad123"

Bot = Client(
    "Simple-Pyrogram-Bot",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)

@Bot.on_message(filters.command(["start"]) & filters.private)
async def start(bot, update):
    await update.reply_text(
        text=f"Hi {update.from_user.mention}"
    )
Bot.run()
