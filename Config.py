# Zorunlu gereklidir. Eklemek istediğin bilgileri burda belirt çekinme 😏

import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "28496124"))
    API_HASH = os.environ.get("API_HASH", "dcadf01f9a76befff2eccc932c6eabd1")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6284961220:AAGQUCkEh_xQS3TCgSmR0Oq2hE--o3vQXVE")
