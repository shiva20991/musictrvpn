from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

PM_HELP_TEXT = "Sorry You can't Use This Bot In Your Group" 

@Client.on_message(filters.command(["help"]))
async def help(client, message):
    await message.reply_text(
     PM_HELP_TEXT, 
     reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Support Channel', url='https://t.me/Mai_bOTs'),
                    InlineKeyboardButton('Owner', url='https://t.me/No_OnE_Kn0wS_Me')
                ],
                [
                    InlineKeyboardButton('Song Plays On', url='https://t.me/movielinks_only'),
                    InlineKeyboardButton('Source', url='https://github.com/No-OnE-Kn0wS-Me/MusicPlayer-Heroku')
                ]
            ]
        )
    ) 
