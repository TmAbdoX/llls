import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
     command(["مبرمج ييبتثنمبثبىمثبىببيببيمىبثثالسورس","مابيببيؤيبدييثبتبنرةرةرةررسون","احمد مثبثبثبمةثمةؤمؤ يويؤمؤةيم ؤيؤ مؤؤ ياديسون"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/02ff5eed4dc2a34cbc1f7.jpg",
        caption=f"""- مبرمج سورس مكس .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◜ 𝙈َ𝙖 𝘿ِ𝙞 𝙎ُ𝙤𝙉 ◞", url=f"https://t.me/MaDyY_y"),
                ],
            ]
        ),
    )
