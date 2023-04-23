import os, logging, asyncio
from Plugins import Maho
from telethon import events, Button
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from Config import *
from asyncio import sleep 
import time, random

# Gerekli silmeyiniz. 
anlik_calisan = []
rxyzdev_tagTot = {}
rxyzdev_initT = {}

# Sonlandırma komutu
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




Maho.on(events.NewMessage(pattern="^/vtag$"))
def rtag(event):
  global gece_tag
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond(f"{nogroup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Eski mesajları göremem.**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Etiketleme Mesajı Yazmadın!")
  else:
    ##return await event.respond(f"{nomesaj}")
    
    ##if mode == "text_on_cmd":
    await client.send_message(event.chat_id, "✅ Etiket işlemi başlatıldı...",
                    buttons=(
                      [
                       Button.inline(" ⛔ Durdur ", data="cancel")
                      ]
                    )
                  ) 
    gece_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(soru)}](tg://user?id={usr.id}) "
      if event.chat_id not in gece_tag:
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt}")
        await asyncio.sleep(20)
        usrnum = 0
        usrtxt = ""

    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"✅ Etiket işlemi tamamlandı !\n\n📊 Toplam etiket: {rxyzdev_tagTot[event.chat_id]}\n👤Etiket işlemini başlatan: {rxyzdev_initT}")

