from telethon import TelegramClient
from pyrogram import Client
import logging
from Config import *
import asyncio
import logging
import os
import time 



logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

bot = TelegramClient('Maho', api_id=Config.APP_ID, api_hash=Config.API_HASH)
Maho = bot.start(bot_token=Config.TOKEN)

# pyrogram 
app = Client(
    "Tags",
    Config.APP_ID,
    Config.API_HASH,
    bot_token=Config.TOKEN,
)
