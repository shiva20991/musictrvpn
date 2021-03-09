from telegram import Message, Chat, Update, Bot, User
from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.error import Unauthorized, BadRequest, TimedOut, NetworkError, ChatMigrated, TelegramError
from telegram.ext import CommandHandler, Filters, MessageHandler, CallbackQueryHandler
from telegram.ext.dispatcher import run_async, DispatcherHandlerStop
from telegram.utils.helpers import escape_markdown
import pyrogram 
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

START_TEXT= "hey Test1" 
STARTIMG = "https://telegra.ph/file/b3b965f9f77a4346d9df5.jpg"

@run_async
@pyrogram.Client.on_message(pyrogram.filters.command(["start"]))
async def start(message: Message, update: Update):
   await client.send_photo(
        STARTIMG,
        START_TEXT,
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
