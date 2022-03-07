from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import asyncio

BOT_TOKEN = "" # your bot token from telegram.me/BotFather. Sample :- "12345:abcdefghijklmnop"
API_ID = "" # your api id from my.telegram.org. Sample :- int("123456")
API_HASH = "" # your api hash from my.telegram.org Sample :- "fayasnoushad123"

Bot = Client(
    "Simple-Pyrogram-Bot",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)

@Bot.on_message(filters.command(["start"]) & filters.private)
async def start(bot, update):
    await update.reply_chat_action("typing")
    await asyncio.sleep(2)
    await update.reply_text(
        text=f"Hi {update.from_user.mention}"
    )

@Bot.on_message(filters.command(["f"]) & filters.private)
async def start(bot, update):
    await update.reply_text(
                        text=f"`Syntax Error: noSuchPageNumber 🥴`"
                    )


@Bot.on_message(filters.command(["love"]) & filters.private)
async def start(bot, update):
    await update.reply_text(
        text=f"Hi {update.from_user.mention}",
reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton(
                        "Channel 💔", url="https://t.me/Animemusicarchive6"),
                    InlineKeyboardButton(
                        "Support 📚", url="https://t.me/Yeageristbots")],
                [InlineKeyboardButton(
                        "Amazing", url="https://github.com/Achu2234")]]))

START_TEXT = """Hello {},
I am an under 5MB media or file to telegra.ph link uploader bot.

Made by @FayasNoushad"""

HELP_TEXT = """**About Me**

- Just give me a media under 5MB
- Then I will download it
- I will then upload it to the telegra.ph link

Made by @FayasNoushad"""

ABOUT_TEXT = """**About Me**

- **Bot :** `Telegraph Uploader`
- **Creator :** [Fayas](https://telegram.me/TheFayas)
- **Channel :** [Fayas Noushad](https://telegram.me/FayasNoushad)
- **Source :** [Click here](https://github.com/FayasNoushad/Telegraph-Uploader-Bot)
- **Language :** [Python3](https://python.org)
- **Library :** [Pyrogram](https://pyrogram.org)"""

START_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('Help', callback_data='help'),
            InlineKeyboardButton('About', callback_data='about'),
            InlineKeyboardButton('Close', callback_data='close')
        ]
    ]
)

HELP_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('Home', callback_data='home'),
            InlineKeyboardButton('About', callback_data='about'),
            InlineKeyboardButton('Close', callback_data='close')
        ]
    ]
)

ABOUT_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('Channel', url='https://telegram.me/FayasNoushad'),
            InlineKeyboardButton('Feedback', url='https://telegram.me/TheFayas')
        ],
        [
            InlineKeyboardButton('Home', callback_data='home'),
            InlineKeyboardButton('Help', callback_data='help'),
            InlineKeyboardButton('Close', callback_data='close')
        ]
    ]
)


@Bot.on_callback_query()
async def start(bot, update):
    
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=ABOUT_BUTTONS
        )
    
    else:
        await update.message.delete()
    

@Bot.on_message(filters.command(["startt"]))
async def start(bot, update):
    
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        quote=True,
        reply_markup=START_BUTTONS
    )



Bot.run()
