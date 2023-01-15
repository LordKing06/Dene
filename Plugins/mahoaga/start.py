# Botunu aşağıdaki link'e belirt veya configs e BOT_USERNAME şeklinde belirt keyfine göre yeğenim :) 
# Sadece hobi amaçlı yapılan bir deneme projesidir. 

from Plugins import Maho
from telethon import events, Button
from telethon.tl.types import ChannelParticipantsAdmins

@Maho.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  if event.is_private:
    async for usr in Maho.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
     await Maho.send_message(-1001825159916, f"ℹ️ **Start Veren Kullanıcı :** {ad}")
     return await event.reply(f"**⌯ Merhaba 👻\n\n⌯ Benim Görevim Üyeleri Etiketlemektir.\n⌯ Komutlar için Komutlar butonuna basınız.**", buttons=(
                      [
                       Button.inline("🗄 Komutlar", data="komutlar")
                      ],
                      [
                       Button.url('↘️ Gruba Ekle', 'http://t.me/CasperTagger_Bot?startgroup=a'),
                       Button.url('📣 Kanal', 'https://t.me/BioCasper')
                      ],
                      [
                       Button.url('👻 Sahibim', 'https://t.me/Suphi_Casper')
                      ],
                    ),
                    link_preview=False)


  if event.is_group:
    return await Maho.send_message(event.chat_id, f"**⌯ Merhaba 👻\n\n⌯ Benim Görevim Üyeleri Etiketlemektir.\n⌯ Komutlar için Komutlar butonuna basınız.**", buttons=(
                      [
                       Button.inline("🗄 Komutlar", data="komutlar")
                      ],
                      [
                       Button.url('↘️ Gruba Ekle', 'http://t.me/CasperTagger_Bot?startgroup=a'),
                       Button.url('📣 Kanal', 'https://t.me/BioCasper')
                      ],
                      [
                       Button.url('👻 Sahibim', 'https://t.me/Suphi_Casper')
                      ],
                    ),
                    link_preview=False)

# Başlanğıc Button
@Maho.on(events.callbackquery.CallbackQuery(data="start"))
async def handler(event):
    async for usr in Maho.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
     await event.edit(f"**⌯ Merhaba 👻\n\n⌯ Benim Görevim Üyeleri Etiketlemek\n⌯ Komutlar için Komutlar Düğmesine Basın.**", buttons=(
                      [
                       Button.inline("🗄 Komutlar", data="komutlar")
                      ],
                      [
                       Button.url('↘️ Gruba Ekle', 'http://t.me/CasperTagger_Bot?startgroup=a'),
                       Button.url('📣 Kanal', 'https://t.me/BioCasper')
                      ],
                      [
                       Button.url('👻 Sahibim', 'https://t.me/Suphi_Casper')
                      ],
                    ),
                    link_preview=False)

# Maho aga
@Maho.on(events.callbackquery.CallbackQuery(data="komutlar"))
async def handler(event):
    await event.edit(f"**⌯              𝑲𝒐𝒎𝒖𝒕𝒍𝒂𝒓              ⌯**\n\n**🕹 Komut :** `/tag`\n**📄 Açıklama :** `Toplu etiket atar.`\n\n**🕹 Komut :** `/ttag`\n**📄 Açıklama :** `Tek tek etiketleme işlemi yapar.`\n\n**🕹 Komut :** `/yt`\n**📄 Açıklama :** `Sadece adminleri etiketler.`\n\n**🕹 Komut :** `/btag`\n**📄 Açıklama :** `Bayraklar ile etiketleme işlemini yapar.`\n\n**🕹 Komut :** `/stag`\n**📄 Açıklama :** `Söz ile etiketleme işlemini yapar.`\n\n**🕹 Komut :** `/itag`\n**📄 Açıklama :** `İsimler ile etiketleme işlemini yapar.`\n\n**🕹 Komut :** `/futbol`\n**📄 Açıklama :** `Futbolcu isimleri ile etiketleme işlemini yapar.`\n\n**🕹 Komut :** `/etag`\n**📄 Açıklama :** `Emojiler ile etiketleme işlemini yapar.`\n\n**🕹 Komut :** `/cancel`\n**📄 Açıklama :** `Etiketleme işlemini sonlandırır...`\n\n**❗ Yalnızca yöneticiler bu komutları kullanabilir.**", buttons=(
                      [
                      Button.inline("◀️ Geri", data="start")
                      ]
                    ),
                    link_preview=False)
