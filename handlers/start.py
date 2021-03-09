from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.utils.helpers import escape_markdown
from telegram import ParseMode 

PM_START_TEXT = "Hi **{}** I'm **{}** \n I Used to Play Songs On Voice Chats\n Especially Created For @movielinks_only \n Do /help for more Details".format(escape_markdown(first_name), escape_markdown(bot.first_name) 

@Client.on_message(filters.command(["start"]))
async def start(client, message):
    await message.reply_text(
     PM_START_TEXT, 
     reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("✅ Yes", switch_inline_query_current_chat=""),
                    InlineKeyboardButton('Owner', url='https://t.me/No_OnE_Kn0wS_Me')
                ],
                [
                    InlineKeyboardButton('Song Plays On', url='https://t.me/movielinks_only'),
                    InlineKeyboardButton('Support Channel', url='https://t.me/Mai_bOTs')
                ]
            ]
        )
    ) 
