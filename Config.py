# Zorunlu gereklidir. Eklemek istediğin bilgileri burda belirt çekinme 😏
import os
class Config(object):
    API_ID = int(os.environ.get("API_ID", "28496124"))
    API_HASH = os.environ.get("API_HASH", "dcadf01f9a76befff2eccc932c6eabd1")
    BOT_TOKEN = os.environ.get("BOT_TOKEN",)
    
    
############## DEĞİŞKENLER ##############
DATABASE_URL = "mongodb+srv://lok:lok31@cluster0.lgjlurr.mongodb.net/?retryWrites=true&w=majority"
LOG_CHANNEL = -1001930738807
GONDERME_TURU = False
OWNER_ID = [1957316197]
LANGAUGE = "TR"

# test projesi..
BOT_USERNAME = "TestTagger_bot"
GROUP_SUPPORT = "TaliaSupport"
sahib = 'Mahoaga'
startmesaj = "**\n\n➣ Grubundaki tüm üyeleri etiketleyebilirim...\n\n➣ Komutlar butonuna tıklayarak tüm komutları öğrenebilirsin.**" 
qrupstart = "➥ Şuan aktif bir şekide çalışmaktayım...\n\n➥ Komutları görmek için aşağıdaki komutlar butonuna tıklayın. "
noadmin = "**🚫 Sen admin değilsin\n\n Yöneticilerle görüşebilirsin.**"
nogroup = "**Üzgünüm, bu komutu sadece gruplarda kullanabilirsin.**"
