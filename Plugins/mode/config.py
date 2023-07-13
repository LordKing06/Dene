# Telethon kütüphanesi config gereksinimleri.

from telethon import TelegramClient

# Telegram Client (Telethon)
API_ID = 28496124
API_HASH = "dcadf01f9a76befff2eccc932c6eabd1"
bot_token = "6388548380:AAGKi84pNLf-HmeAuNWo36XuTr7lvblL-g4"

# test projesi.. 
noadmin = "**🚫 Sen admin değilsin\n\n Yöneticilerle görüşebilirsin.**"
nomesaj = "**Etiket işlemine başlamam için bana bir metin ver**"
#

Maho = TelegramClient('Maho', API_ID, API_HASH).start(bot_token=bot_token)
