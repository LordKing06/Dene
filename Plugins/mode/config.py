# Telethon kütüphanesi config gereksinimleri.

from telethon import TelegramClient

# Telegram Client (Telethon)
API_ID = 
API_HASH = ""
bot_token = "6301074895:AAEDy48YMXe8JmCcjK1A9VKWp_YvU7PThbo"

edalet = TelegramClient('edalet', API_ID, API_HASH).start(bot_token=bot_token)
