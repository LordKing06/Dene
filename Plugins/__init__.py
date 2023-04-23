from telethon import TelegramClient
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
