# Zorunlu gereklidir. Eklemek istediğin bilgileri burda belirt çekinme 😏

import os

class Config(object):
    APP_ID = int(os.environ.get("APP_ID", 6))
    API_HASH = os.environ.get("API_HASH", "dcadf01f9a76befff2eccc932c6eabd1")
    TOKEN = os.environ.get("TOKEN", "5978809708:AAFqCi8ZjBEU35lTemP4O1Xd7_iuWPxiajA")
