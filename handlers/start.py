from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(
    filters.command("trv")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b> Hi {message.from_user.first_name}!</b>
I am an open-source bot that lets you play music in your Telegram groups.
Use /help to know more about me.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ð Sourceð ", url=""
                    )
                ],
                [
                    InlineKeyboardButton(
                        "ð¬ Group", url="https://t.me/trvpn"
                    ),
                    InlineKeyboardButton(
                        "Channel ð", url="https://t.me/trvpn"
                    )
                ]
            ]
        )
    )


@Client.on_message(
    filters.command("trv")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "<b>Click The Yes Button For Searching a Video</b>",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "â Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No â", callback_data="close"
                    )
                ]
            ]
        )
    )
