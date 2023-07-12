# Telethon kütüphanesi config gereksinimleri.

from telethon import TelegramClient

# Telegram Client (Telethon)
API_ID = 28496124
API_HASH = "dcadf01f9a76befff2eccc932c6eabd1"
bot_token = "6301074895:AAEDy48YMXe8JmCcjK1A9VKWp_YvU7PThbo"

edalet = TelegramClient('edalet', API_ID, API_HASH).start(bot_token=bot_token)
