# Telethon kütüphanesi config gereksinimleri.

from telethon import TelegramClient

# Telegram Client (Telethon)
API_ID = 28496124
API_HASH = "dcadf01f9a76befff2eccc932c6eabd1"
bot_token = "6394394743:AAGoZqkgViLwUZWW8xvn6dHsEOecrQBv1mU"

Maho = TelegramClient('Maho', API_ID, API_HASH).start(bot_token=bot_token)
