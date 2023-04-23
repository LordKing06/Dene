import os, logging, asyncio
from Plugins import Maho
from telethon import events, Button
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from Config import *
from asyncio import sleep
import time, random 

# Silmeyiniz. 
anlik_calisan = []
rxyzdev_tagTot = {}
rxyzdev_initT = {}

@Maho.on(events.NewMessage(pattern="^/cancel$"))
async def cancel_spam(event):
  if not event.chat_id in anlik_calisan:
    return
  else:
    try:
      anlik_calisan.remove(event.chat_id)
    except:
      pass
    return await event.respond('**✅ Etiket işlemi başarıyla durduruldu.**')

# Emoji tag komutu. 
@Maho.on(events.NewMessage(pattern="^/kart ?(.*)"))
async def mentionall(event):
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("**Bu komutu sadece grup veya kanallarda kullanabilirsiniz.**")
  
  admins = []
  async for admin in Maho.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu komutu sadece yöneticiler kullanabilir.**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Eski Mesajlar için Üyelerden Bahsedemem! (gruba eklemeden önce gönderilen mesajlar)**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**Bana bir metin verin.**")
  else:
    return await event.respond("**Etikete Başlamak için sebep yazın... ✋\n\n(Örnek: `/kart Selamlar gibi!`**)**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond("**✅ Etiket işlemi başladı.**")
        
    async for x in Maho.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"⌯ [{random.choice(kart)}](tg://user?id={x.id})\n"
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await Maho.send_message(event.chat_id, f"**⌯ 📢 {msg}**\n\n{usrtxt}")
        await asyncio.sleep(3)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"{sender.first_name}"      
    if event.chat_id in rxyzdev_tagTot:
           a = await event.respond(f"**✅ Etiket işlemi başarıyla durduruldu.**\n\n**Etiketlenen Kişi Sayısı:** {rxyzdev_tagTot[event.chat_id]}")
           await sleep(10)
           await a.delete()

  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for x in Maho.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"⌯ [{random.choice(kart)}](tg://user?id={x.id})\n"
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await Maho.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(3)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"{sender.first_name}"      
    if event.chat_id in rxyzdev_tagTot:
           a = await event.respond(f"**✅ Etiket işlemi başarıyla durduruldu.**\n\n**Etiketlenen Kişi Sayısı:** {rxyzdev_tagTot[event.chat_id]}")
           await sleep(10)
           await a.delete()


kart = "♤ ♡ ♢ ♧ 🂱 🂲 🂳 🂴 🂵 🂶 🂷 🂸 🂹 🂺 🂻 🂼 🂽 🂾 🂡 🂢 🂣 🂤 🂥 🂦 🂧 🂨 🂩 🂪 🂫 🂬 🂭 🂮 🃁 🃂 🃃 🃄 🃅 🃆 🃇 🃈 🃉 🃊 🃋 🃌 🃍 🃎 🃑 🃒 🃓 🃔 🃕 🃖 🃗 🃘 🃙 🃚 🃛 🃜 🃝 🃞 🂠  🃟 " .split(" ")
