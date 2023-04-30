import os
import logging
import asyncio
from telethon import Button, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.tl.types import ChannelParticipantsRecent
from asyncio import sleep
from Config import *
from Plugins import Maho
import time
import random

anlik_calisan = []
rxyzdev_tagTot = {}
rxyzdev_initT = {}

# Komutlar
@Maho.on(events.NewMessage(pattern="^/cancel$"))
async def cancel_spam(event):
    if event.chat_id not in anlik_calisan:
        return
    else:
        try:
            anlik_calisan.remove(event.chat_id)
        except:
            pass
        return await event.respond('**✅ Etiket işlemi başarıyla durduruldu.**')

@Maho.on(events.NewMessage(pattern="^/tag ?(.*)"))
async def mentionall(event):
    global anlik_calisan 
    rxyzdev_tagTot[event.chat_id] = 0
    if event.is_private:
        return await event.respond("**Bu komutu sadece grup veya kanallarda kullanabilirsiniz.**")
  
    admins = []
    async for admin in Maho.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
        admins.append(admin.id)
    if event.sender_id not in admins:
        return await event.respond("**Bu komutu sadece yöneticiler kullanabilir. ✋**")
  
    if event.pattern_match.group(1):
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
    elif event.reply_to_msg_id:
        mode = "text_on_reply"
        msg = await event.get_reply_message()
        if msg == None:
            return await event.respond("**Eski Mesajlar için Üyelerden Bahsedemem! (gruba eklemeden önce gönderilen mesajlar)**")
    else:
        return await event.respond("**Etikete başlamak için sebep yazın.\n\n(Örnek:** `/tag Herkese Merhaba!`**)**")
  
    group_participants = await Maho.get_participants(event.chat_id)

    if mode == "text_on_cmd":
        anlik_calisan.append(event.chat_id)
        usrnum = 0
        usrtxt = ""
        rxyzdev_tagTot[event.chat_id] = len(group_participants)
        await event.respond("✅ Etiket işlemi başladı.")

        for usr in group_participants:
            if usr.deleted or usr.bot:
                continue 

            usrnum += 1
            usrtxt += f"⌯ [{usr.first_name}](tg://user?id={usr.id})\n"

            if event.chat_id not in anlik_calisan:
                return

            if usrnum == 5:
                await Maho.send_message(event.chat_id, f"⌯ 📢 {msg}\n\n{usrtxt}")
                await asyncio.sleep(3)
                usrnum = 0
                usrtxt = ""

        sender = await event.get_sender()
        rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"

        if event.chat_id in rxyzdev_tagTot:
           member_count = await event.client.get_participants(event.chat_id, filter=ChannelParticipantsRecent())
           bot_count = await event.client.get_participants(event.chat_id, filter=ChannelParticipantsBots())
           tag_count = rxyzdev_tagTot[event.chat_id]
           a = await event.respond(f"✅ Etiket işlemi başarıyla durduruldu.\n\nEtiketlenen kişi sayısı: {tag_count}\nToplam üye sayısı: {len(member_count)}\nToplam bot sayısı: {len(bot_count)}")
           await sleep(10)
           await a.delete()

    if mode == "text_on_reply":
        anlik_calisan.append(event.chat_id)
        usrnum = 0
        usrtxt = ""
        rxyzdev_tagTot[event.chat_id] = len(group_participants)

        for usr in group_participants:
            usrnum += 1
            usrtxt += f"⌯ [{usr.first_name}](tg://user?id={usr.id})\n"

            if event.chat_id not in anlik_calisan:
                return

            if usrnum == 5:
                await Maho.send_message(event.chat_id, usrtxt, reply_to=msg)
                await asyncio.sleep(3)
                usrnum = 0
                usrtxt = ""

        sender = await event.get_sender()
        rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"

        
        if event.chat_id in rxyzdev_tagTot:
           member_count = await event.client.get_participants(event.chat_id, filter=ChannelParticipantsRecent())
           bot_count = await event.client.get_participants(event.chat_id, filter=ChannelParticipantsBots())
           tag_count = rxyzdev_tagTot[event.chat_id]
           a = await event.respond(f"✅ Etiket işlemi başarıyla durduruldu.\n\nEtiketlenen kişi sayısı: {tag_count}\nToplam üye sayısı: {len(member_count)}\nToplam bot sayısı: {len(bot_count)}")
           await sleep(10)
           await a.delete()

#Bu şekilde, `get_participants()` fonksiyonuna `filter` parametresi eklenerek yalnızca insan kullanıcıları alınırken, botları da hesaplayabilirsiniz.
                                    
                                    
