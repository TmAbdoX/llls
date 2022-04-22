import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from pyrogram import filters
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,
                            InlineKeyboardMarkup, Message)
from youtubesearchpython.future import VideosSearch
from typing import Union

from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app
import config
from config import BANNED_USERS
from config.config import OWNER_ID
from strings import get_command, get_string
from YukkiMusic import Telegram, YouTube, app
from YukkiMusic.misc import SUDOERS
from YukkiMusic.plugins.play.playlist import del_plist_msg
from YukkiMusic.plugins.sudo.sudoers import sudoers_list
from YukkiMusic.utils.database import (add_served_chat,
                                       add_served_user,
                                       blacklisted_chats,
                                       get_assistant, get_lang,
                                       get_userss, is_on_off,
                                       is_served_private_chat)
from YukkiMusic.utils.decorators.language import LanguageStart
from YukkiMusic.utils.inline import (help_pannel, private_panel,
                                     start_pannel)



@app.on_message(
    command(["سورس مكس","سورس","السورس","يا سورس"])
    & filters.group
    & ~filters.edited
)
@LanguageStart
async def hilo(client, message: Message, _):
    out = start_pannel(_)
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
