from Plugins import Maho
from telethon import events, Button
from telethon.tl.types import ChannelParticipantsAdmins
from Config import *

@Maho.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  if event.is_private:
    async for usr in Maho.iter_participants(event.chat_id):
     ad = f"**➣ 𝖬𝖾𝗋𝗁𝖺𝖻𝖺 [{usr.first_name}](tg://user?id={usr.id}) benim adım Etiket botu merhaba...**"
  await event.reply(f"{ad} {startmesaj}", buttons=(
                      [
                       Button.url('➕ Beni0 Gruba Ekle', f'https://t.me/{BOT_USERNAME}?startgroup=a')
                      ],
                      [
                       Button.inline("📚 Komutlar", data="komutlar"),
                       Button.url('👨‍💻 Sahip', f'https://t.me/{sahib}')
                      ],
                      [
                      Button.url('🛡 Kanal ', f'https://t.me/BotDuyuru')
                      ]
                    ),
                    link_preview=False)
  if event.is_group:
    return await Maho.send_message(event.chat_id, f"{qrupstart}", buttons=( 
                                                    [
                                                    Button.url('🎉  Tıkla', f'https://t.me/{BOT_USERNAME}?start')
                                                    ]
                                                  ),
                                                  link_preview=False)
@Maho.on(events.callbackquery.CallbackQuery(data="start"))
async def handler(event):
    async for usr in Maho.iter_participants(event.chat_id):
     ad = f"**➣ 𝖬𝖾𝗋𝗁𝖺𝖻𝖺 [{usr.first_name}](tg://user?id={usr.id}) benim adım Etiket botu merhaba...**"
    await event.edit(f"{ad} {startmesaj}", buttons=(
                      [
                       Button.url('➕ Beni Gruba Ekle', f'https://t.me/{BOT_USERNAME}?startgroup=a')
                      ],
                      [
                       Button.inline("📚 Komutlar", data="komutlar"),
                       Button.url('👨‍💻 Sahip', f'https://t.me/{sahib}')
                      ],
                      [
                       Button.url('🛡 Kanal ', f'https://t.me/BotDuyuru')
                      ]
                    ),
                    link_preview=False)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ KOMUTLAR ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@Maho.on(events.callbackquery.CallbackQuery(data="komutlar"))
async def handler(event):
    await event.edit("**➢ Tüm komutlar aşağıda yer almaktadır:\n\n➢ Hadi herhangi bir komuta tıkla ve ne işe yaradığını öğren.**", buttons=(
                      [
                      Button.inline(" Sade ", data="tag1"), 
                      Button.inline(" Tek Tek ", data="tag2"), 
                      Button.inline(" Admin ", data="tag3")
                      ], 
                      [
                      Button.inline(" Emoji ", data="tag4"), 
                      Button.inline(" Sözlerle ", data="tag5"), 
                      Button.inline(" Sorularla ", data="tag6") 
                      ],
                      [
                      Button.inline(" Kartlarla ", data="tag7"), 
                      Button.inline(" Bayraklarla ", data="tag8"), 
                      Button.inline(" Eros oku ", data="tag9")
                      ],
                      [
                      Button.inline(" İptal etmek ", data="tag10")
                      ], 
                      [
                      Button.inline(" ⬅️ Geri ", data="start")
                      ]
                    ),
                    link_preview=False)
                                                    
                                                    
@Maho.on(events.callbackquery.CallbackQuery(data="tag1"))
async def tag1(event):
    await event.edit("**» /utag   < Mesaj >\n   - Üyeleri 5'li etiketler.**", buttons=(
                      [
                      Button.inline(" ⬅️ Geri ", data="komutlar")
                      ]
                    ),
                    link_preview=False)
@client.on(events.callbackquery.CallbackQuery(data="tag2"))
async def tag2(event):
    await event.edit("**» /tektag   < Mesaj >\n   - Üyeleri teker teker etiketler.**", buttons=(
                      [
                      Button.inline(" ⬅️ Geri ", data="komutlar")
                      ]
                    ),
                    link_preview=False)
@Maho.on(events.callbackquery.CallbackQuery(data="tag3"))
async def tag3(event):
    await event.edit("**» @admin, /admin\n   - Bildirmek istediğiniz kullanıcının mesajına @admin yazmanız yeterli.**", buttons=(
                      [
                      Button.inline(" ⬅️ Geri ", data="komutlar")
                      ]
                    ),
                    link_preview=False)
@Maho.on(events.callbackquery.CallbackQuery(data="tag4"))
async def tag4(event):
    await event.edit("**» /etag   < Mesaj >\n   - Üyeleri emoji ile etiketler.**", buttons=(
                      [
                      Button.inline(" ⬅️ Geri ", data="komutlar")
                      ]
                    ),
                    link_preview=False)
@Maho.on(events.callbackquery.CallbackQuery(data="tag5"))
async def tag5(event):
    await event.edit("**» /stag   < Mesaj >\n   - Üyeleri güzel sözlerle etiketler.**", buttons=(
                      [
                      Button.inline(" ⬅️ Geri ", data="komutlar")
                      ]
                    ),
                    link_preview=False)
@Maho.on(events.callbackquery.CallbackQuery(data="tag6"))
async def tag6(event):
    await event.edit("**» /vtag < Mesaj >\n   - Üyeleri sorularla etiketler.**", buttons=(
                      [
                      Button.inline(" ⬅️ Geri ", data="komutlar")
                      ]
                    ),
                    link_preview=False)
@Maho.on(events.callbackquery.CallbackQuery(data="tag7"))
async def tag7(event):
    await event.edit("**» /ktag < Mesaj >\n   - Üyeleri iskambil kağıtları ile etiketler.**", buttons=(
                      [
                      Button.inline(" ⬅️ Geri ", data="komutlar")
                      ]
                    ),
                    link_preview=False)
@client.on(events.callbackquery.CallbackQuery(data="tag8"))
async def tag8(event):
    await event.edit("**» /btag < Mesaj >\n   - Üyeleri bayraklar ile etiketler.**", buttons=(
                      [
                      Button.inline(" ⬅️ Geri ", data="komutlar")
                      ]
                    ),
                    link_preview=False)
@Maho.on(events.callbackquery.CallbackQuery(data="tag9"))
async def tag9(event):
    await event.edit("»/eros =>\n   - Grup içerisinde eros oku atar.", buttons=(
                      [
                      Button.inline(" ⬅️ Geri ", data="komutlar")
                      ]
                    ),
                    link_preview=False)
@Maho.on(events.callbackquery.CallbackQuery(data="tag10"))
async def tag10(event):
    await event.edit("»/cancel =>\n   - 𝖤𝗍𝗂𝗄𝖾𝗍𝗅𝖾𝗆𝖾 𝗂𝗌𝗅𝖾𝗆𝗂𝗇𝗂 𝖽𝗎𝗋𝖽𝗎𝗋𝗎𝗋 .", buttons=(
                      [
                      Button.inline(" ⬅️ Geri ", data="komutlar")
                      ]
                    ),
                    link_preview=False)
@Maho.on(events.callbackquery.CallbackQuery(data="gece"))
async def gece(event):
    await event.edit("»ᴜ̈ᴄʀᴇᴛsɪᴢ ɢʀᴜᴘ ᴠᴇʏᴀ ᴋᴀɴᴀʟ ʟɪɴᴋɪ ᴇᴋʟᴇᴍᴇᴋ ɪᴄ̧ɪɴ [gє¢є кυѕ̧υ](tg://openmessage?user_id=5576614947) ᴜʟᴀşıɴıᴢ .", buttons=(
                      [
                      Button.inline(" ⬅️ Geri ", data="grup")
                      ]
                    ),
                    link_preview=False)
