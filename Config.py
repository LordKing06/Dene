# Zorunlu gereklidir. Eklemek istediğin bilgileri burda belirt çekinme 😏

import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "28496124"))
    API_HASH = os.environ.get("API_HASH", "dcadf01f9a76befff2eccc932c6eabd1")
    BOT_TOKEN = os.environ.get("BOT_TOKEN",)
    
    
# test projesi..
BOT_USERNAME = 'TestTagger_bot' 
GROUP_SUPPORT = 'TaliaSupport'
sahib = 'Mahoaga'
startmesaj = "**\n\n➣ Grubundaki tüm üyeleri etiketleyebilirim...\n\n➣ Komutlar butonuna tıklayarak tüm komutları öğrenebilirsin.**" 
qrupstart = "➥ Şuan aktif bir şekide çalışmaktayım...\n\n➥ Komutları görmek için aşağıdaki komutlar butonuna tıklayın. "
noadmin = "**🚫 Sen admin değilsin\n\n Yöneticilerle görüşebilirsin.**"
nogroup = "**Üzgünüm, bu komutu sadece gruplarda kullanabilirsin.**"
