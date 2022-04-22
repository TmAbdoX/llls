import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)



@app.on_message(
    command(["الاوامر","اوامر"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://i.postimg.cc/Wbr5zF53/IMG-20220422-033946-869.jpg",
        caption=f"""[ٓ❍ | 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐓𝐨 𝐒𝐨𝐮𝐫𝐜𝐞 𝐌𝐢𝐱 .](https://t.me/me_xec_o)\n\n[❍ | 𝐌𝐢𝐱 𝐓𝐡𝐞 𝐁𝐞𝐬𝐭 𝐒𝐨𝐮𝐫𝐜𝐞 𝐎𝐧 𝐓𝐞𝐥𝐞 .](https://t.me/me_xec_o)\n\n[❍ | 𝐅𝐨𝐥𝐥𝐨𝐰 𝐓𝐡𝐞 𝐁𝐮𝐭𝐭𝐨𝐧𝐬 𝐁𝐞𝐥𝐨𝐰 .](https://t.me/me_xec_o)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◜ 𝙈َ𝙖 𝘿ِ𝙞 𝙎ُ𝙤𝙉 ◞", url=f"https://t.me/MaDyY_y"),
                    InlineKeyboardButton(
                        "◜ 𝙈𝙞 𝙄𝙭 𝙓 ◞", url=f"https://t.me/l_Mix_1")
                ],[
                    InlineKeyboardButton(
                        "- 𝐒𝐨𝐮𝐫𝐜𝐞 𝐌𝐢𝐱 .", url=f"https://t.me/me_xec_o"),
                ],

            ]

        ),

    )
