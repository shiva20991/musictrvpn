from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.utils.helpers import escape_markdown
from telegram import ParseMode 

PM_START_TEXT = "Hi *{}* I'm *{}* \n I Can Play Songs On Voice chats With The Given YouTube link \n But I'll Only Work On @movielinks_only \n Do /help for more Details" 

@Client.on_message(filters.command(["start"]))
async def start(client, message):
    await message.reply_text(
     PM_START_TEXT.format(escape_markdown(first_name), escape_markdown(bot.first_name),
     parse_mode=ParseMode.MARKDOWN, 
     reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        '✅ Yes', switch_inline_query_current_chat=''
                    ),
                    InlineKeyboardButton(
                        'No ❌', callback_data='close'
                    ),
                    InlineKeyboardButton(
                        'Song Plays On', url='https://t.me/movielinks_only'
                    ),
                    InlineKeyboardButton(
                        'Support Channel', url='https://t.me/Mai_bOTs'
                    )
                ]
            ]
        )
