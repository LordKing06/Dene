# Değişiklikleri ekle belirtilen yerlere ...
import os
class Config(object):
    API_ID = int(os.environ.get("API_ID", "28496124"))
    API_HASH = os.environ.get("API_HASH", "dcadf01f9a76befff2eccc932c6eabd1")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6301074895:AAEDy48YMXe8JmCcjK1A9VKWp_YvU7PThbo")


# test projesi..
BOT_NAME = 'TestTagger_bot'
sahib = 'Mahoaga' 
kanal = 'TaliaSupport'
startmesaj = "**\n\n➣ Grubundaki tüm üyeleri etiketleyebilirim...\n\n➣ Komutlar butonuna tıklayarak tüm komutları öğrenebilirsin.**" 
qrupstart = "➥ Şuan aktif bir şekide çalışmaktayım...\n\n➥ Komutları görmek için aşağıdaki komutlar butonuna tıklayın. "
noadmin = "**🚫 Sen admin değilsin\n\n Yöneticilerle görüşebilirsin.**"
nogroup = "**Üzgünüm, bu komutu sadece gruplarda kullanabilirsin.**"
nomesaj = "**Etiket işlemine başlamam için bana bir metin ver**"

