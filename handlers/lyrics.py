# Module by https://github.com/tofikdn
# Copyright (C) 2021 TdMusic

import requests
import re
import lyricsgenius

from config import BOT_USERNAME
from pyrogram import Client, filters
from helpers.filters import command
from youtubesearchpython import VideosSearch
from pyrogram.types import Message

@Client.on_message(filters.command("lirik"))
async def lrsearch(_, message: Message):  
    m = await message.reply_text("🔎 Mencari lirik yang anda inginkan")
    query = message.text.split(None, 1)[1]
    x = "OXaVabSRKQLqwpiYOn-E4Y7k3wj-TNdL5RfDPXlnXhCErbcqVvdCF-WnMR5TBctI"
    y = lyricsgenius.Genius(x)
    y.verbose = False
    S = y.search_song(query, get_full_info=False)
    if S is None:
        return await m.edit("❌ Lirik tidak ditemukan, mohon periksa tulisan anda")
    xxx = f"""
**Lyrics Search Powered By Rio Music**

**Searched Song:-** __{query}__

**Found Lyrics For:-** __{S.title}__
**Artist:-** {S.artist}

**__Lyrics:__**

{S.lyrics}"""
    await m.edit(xxx)
