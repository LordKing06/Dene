import os
import logging
import asyncio
from telethon import Button, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.tl.types import PeerChannel, ChannelParticipantsRecent, ChannelParticipantsBots
from asyncio import sleep
from Plugins.mode.config import Maho
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
        await event.respond('**✅ Etiket işlemi başarıyla durduruldu.**')
        await show_output(event.chat_id)
        await sleep(20)  # 20 saniye bekleme süresi
        await delete_output(event.chat_id)


@Maho.on(events.NewMessage(pattern="^/tag$"))
async def mentionall(event):
    global anlik_calisan
    rxyzdev_tagTot[event.chat_id] = 0
    if event.is_private:
        return await event.respond("**Bu komutu sadece grup veya kanallarda kullanabilirsiniz.**")

    admins = []
    async for admin in Maho.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
        admins.append(admin.id)
    if event.sender_id not in admins:
        return await event.respond(f"{noadmin}")

    group_participants = await Maho.get_participants(event.chat_id)
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    rxyzdev_tagTot[event.chat_id] = 0

    await event.respond('**✅ Etiket işlemi başarıyla başlatıldı.**')

    async def tag_users():
        while event.chat_id in anlik_calisan:
            for usr in group_participants:
                if usr.bot:
                    continue
                if usr.deleted:
                    continue

                usrnum += 1
                cleaned_name = ''.join(char for char in usr.first_name if char.lower() != ' ') if usr.first_name else ''
                username = f"🔘 @{usr.username}" if usr.username else cleaned_name
                usrtxt += f"↪ {event.pattern_match.group(1)[:-1]} [{username}](tg://user?id={usr.id})\n"

                if usrnum == 5:
                    await Maho.send_message(event.chat_id, usrtxt)
                    await asyncio.sleep(10)
                    usrnum = 0
                    usrtxt = ""

                rxyzdev_tagTot[event.chat_id] += 1

            await asyncio.sleep(10)

    asyncio.ensure_future(tag_users())

async def show_output(chat_id):
    member_count = await Maho.get_participants(chat_id, filter=ChannelParticipantsRecent())
    tag_count = rxyzdev_tagTot[chat_id]
    total_count = len(member_count)

    output = f"👥 Genel üye sayısı: {len(member_count)}\n📢 Etiketlenen toplam üye sayısı: {tag_count}\n⛔ Silinen hesaplar ve botlara Etiket atılmadı."
    await Maho.send_message(chat_id, output)


async def delete_output(chat_id):
    messages = await Maho.get_messages(chat_id)
    for msg in messages:
        await msg.delete()
