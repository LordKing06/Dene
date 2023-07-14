import asyncio
from telethon import events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.tl.types import PeerChannel, ChannelParticipantsRecent, ChannelParticipantsBots
from asyncio import sleep
import time
from telethon.sync import TelegramClient
from Plugins.mode.config import Maho 

anlik_calisan = {}
etiketlenen_uyeler = {}


@Maho.on(events.NewMessage(pattern="^/tag ?(.*)"))
async def mentionall(event):
    global anlik_calisan, etiketlenen_uyeler
    if event.is_private:
        return await event.respond("**Bu komut gruplar ve kanallar için geçerlidir❗️**")
    admins = []
    async for admin in Maho.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
        admins.append(admin.id)
    if event.sender_id not in admins:
        return await event.respond("**Bu komutu sadece yöneticiler kullanabilir. 👮‍♂️**")
    if event.pattern_match.group(1):
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
    elif event.reply_to_msg_id:
        mode = "text_on_reply"
        msg = event.reply_to_msg_id
        if msg is None:
            return await event.respond("Önceki mesajları etiket işlemi için kullanamıyorum.")
    else:
        return await event.respond("İşleme başlamak için ifade yazınız. 💡")
    if mode == "text_on_cmd":
        anlik_calisan[event.chat_id] = True
        etiketlenen_uyeler[event.chat_id] = 0
        usrnum = 0
        usrtxt = ""
        async for usr in Maho.iter_participants(event.chat_id):
            if usr.bot or usr.deleted:
                continue
            usrnum += 1
            usrtxt += f"📣  [{usr.first_name}](tg://user?id={usr.id}) ,"
            if event.chat_id not in anlik_calisan:
                return
            if usrnum == 5:
                await Maho.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
                etiketlenen_uyeler[event.chat_id] += usrnum
                await asyncio.sleep(10)
                usrnum = 0
                usrtxt = ""
        genel_uye_sayisi = 0
        async for _ in Maho.iter_participants(event.chat_id):
            genel_uye_sayisi += 1
        await event.respond(f"Etiketlenen Gerçek Üye Sayısı: {etiketlenen_uyeler[event.chat_id]}\nGrubun Şuanki Genel Üye Sayısı: {genel_uye_sayisi}\n\nSilinmiş hesaplar ve botlara etiket atılmamıştır.")
        del anlik_calisan[event.chat_id]
        del etiketlenen_uyeler[event.chat_id]
    if mode == "text_on_reply":
        anlik_calisan[event.chat_id] = True
        etiketlenen_uyeler[event.chat_id] = 0
        usrnum = 0
        usrtxt = ""
        async for usr in Maho.iter_participants(event.chat_id):
            if usr.bot or usr.deleted:
                continue
            usrnum += 1
            usrtxt += f"📣  [{usr.first_name}](tg://user?id={usr.id}) ,"
            if event.chat_id not in anlik_calisan:
                return
            if usrnum == 5:
                await Maho.send_message(event.chat_id, usrtxt, reply_to=msg)
                etiketlenen_uyeler[event.chat_id] += usrnum
                await asyncio.sleep(10)
                usrnum = 0
                usrtxt = ""
        genel_uye_sayisi = 0
        async for _ in Maho.iter_participants(event.chat_id):
            genel_uye_sayisi += 1
        await event.respond(f"Etiketlenen Gerçek Üye Sayısı: {etiketlenen_uyeler[event.chat_id]}\nGrubun Şuanki Genel Üye Sayısı: {genel_uye_sayisi}\n\nSilinmiş hesaplar ve botlara etiket atılmamıştır.")

