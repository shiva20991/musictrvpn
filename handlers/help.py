from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

PM_HELP_TEXT = "Hi I Can Play Songs On Voice Chats But I Only works On @movielinks_only \n How I Works? \n You Can Send A YouTube Video In [This](https://t.me/movielinks_only) Group Then Reply /play On That Link \n or You Can Send */play <Ytlink>* \n I also Works On Inline Too.. \n Bot Made By @mai_bots ♥️" 

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
