import pyrogram 
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

START_TEXT= "hey Test" 
STARTIMG = "https://telegra.ph/file/b3b965f9f77a4346d9df5.jpg"

@pyrogram.Client.on_message(pyrogram.filters.command(["start"]))
async def start(bot, update):
    await bot.send_message.reply_photo(
        STARTIMG,
        chat_id=update.chat.id,
        text=START_TEXT,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("✅ Yes", switch_inline_query_current_chat=""),
                    InlineKeyboardButton("No ❌", callback_data="close")
                ],
                [
                    InlineKeyboardButton('Song Plays On', url='https://t.me/movielinks_only'),
                    InlineKeyboardButton('Channel', url='https://t.me/Mai_bOTs')
                ]
            ]
        ),
        reply_to_message_id=update.message_id
    )
