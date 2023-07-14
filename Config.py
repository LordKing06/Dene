# Değişiklikleri ekle belirtilen yerlere ...
import os
class Config(object):
    API_ID = int(os.environ.get("API_ID", "28496124"))
    API_HASH = os.environ.get("API_HASH", "dcadf01f9a76befff2eccc932c6eabd1")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5946035154:AAHV9lOQKz4VL3iNhwp4ovsEWR9GKM6ux34")


# test projesi..
BOT_NAME = 'Videoizle_bot'
sahib = 'Mahoaga' 
kanal = 'TaliaSupport'
startmesaj = "**\n\n➣ Grubundaki tüm üyeleri etiketleyebilirim...\n\n➣ Komutlar butonuna tıklayarak tüm komutları öğrenebilirsin.**" 
qrupstart = "➥ Şuan aktif bir şekide çalışmaktayım...\n\n➥ Komutları görmek için aşağıdaki komutlar butonuna tıklayın. "
nogroup = "**Üzgünüm, bu komutu sadece gruplarda kullanabilirsin.**"
