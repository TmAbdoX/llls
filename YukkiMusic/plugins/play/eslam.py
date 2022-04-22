import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
     command(["هكر السورس","اسلام","سوسو"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://i.postimg.cc/MTFRpbcv/IMG-20220422-053359-808.jpg",
        caption=f"""- مبرمج سورس مكس .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◜ 𝙀𝙨 𝙎𝙡 𝘼𝙖𝙈 ◞", url=f"https://t.me/S_D_H_A"),
                ],
            ]
        ),
    )
