import asyncio
from telethon import events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.tl.types import PeerChannel, ChannelParticipantsRecent, ChannelParticipantsBots 
from asyncio import sleep
import time
from Plugins.mode.config import Maho 

anlik_calisan = {}
etiketlenen_uyeler = {}

@Maho.on(events.NewMessage(pattern="^/tag ?(.*)"))
async def mention_all(event):
    global anlik_calisan, etiketlenen_uyeler

    if event.is_private:
        return await event.respond("**Bu komut yalnızca gruplar ve kanallar için geçerlidir.❗️**")

    chat_id = event.chat_id
    user_id = event.sender_id

    async def get_admins():
        admins = []
        async for admin in Maho.iter_participants(chat_id, filter=ChannelParticipantsAdmins):
            admins.append(admin.id)
        return admins

    if user_id not in await get_admins():
        return await event.respond("**Bu komutu yalnızca yöneticiler kullanabilir. 👮‍♂️**")

    mode = "text_on_cmd"
    if event.pattern_match.group(1):
        msg = event.pattern_match.group(1)
    elif event.reply_to_msg_id:
        mode = "text_on_reply"
        msg = event.reply_to_msg_id
        if msg is None:
            return await event.respond("Önceki mesajları etiketlemek için kullanamıyorum.")

    if mode == "text_on_cmd":
        anlik_calisan[chat_id] = True
        etiketlenen_uyeler[chat_id] = 0
        usrnum = 0
        usrtxt = ""
        async for user in Maho.iter_participants(chat_id):
            if user.bot or user.deleted:
                continue
            usrnum += 1
            usrtxt += f"📢  [{user.first_name}](tg://user?id={user.id}) ,"
            if chat_id not in anlik_calisan:
                await event.respond()
                return
            if usrnum == 5:
                await Maho.send_message(chat_id, f"{usrtxt}\n\n{msg}")
                etiketlenen_uyeler[chat_id] += usrnum
                await asyncio.sleep(10)
                usrnum = 0
                usrtxt = ""

    if mode == "text_on_reply":
        anlik_calisan[chat_id] = True
        etiketlenen_uyeler[chat_id] = 0
        usrnum = 0
        usrtxt = ""
        async for user in Maho.iter_participants(chat_id):
            if user.bot or user.deleted:
                continue
            usrnum += 1
            usrtxt += f"📢  [{user.first_name}](tg://user?id={user.id}) ,"
            if chat_id not in anlik_calisan:
                await event.respond("İşlem başarıyla durduruldu. ✅")
                return
            if usrnum == 5:
                await Maho.send_message(chat_id, usrtxt, reply_to=msg)
                etiketlenen_uyeler[chat_id] += usrnum
                await asyncio.sleep(10)
                usrnum = 0
                usrtxt = ""

@Maho.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
    global anlik_calisan, etiketlenen_uyeler
    chat_id = event.chat_id

    if chat_id in anlik_calisan:
        genel_uye_sayisi = 0
        async for _ in Maho.iter_participants(chat_id):
            genel_uye_sayisi += 1
        await event.respond(f"Etiketlenen Gerçek Üye Sayısı: {etiketlenen_uyeler[chat_id]}\nGrubun Şuanki Genel Üye Sayısı: {genel_uye_sayisi}\n\nSilinmiş hesaplar ve botlara etiket atılmamıştır.")
        del anlik_calisan[chat_id]
        del etiketlenen_uyeler[chat_id]

@Maho.on(events.NewMessage(pattern='^/stats'))
async def stats(event):
    global etiketlenen_uyeler
    chat_id = event.chat_id

    if chat_id in etiketlenen_uyeler:
        genel_uye_sayisi = 0
        async for _ in Maho.iter_participants(chat_id):
            genel_uye_sayisi += 1
        etiketlenen_gercek_uye_sayisi = etiketlenen_uyeler[chat_id]
        await event.respond(f"Genel Üye Sayısı: {genel_uye_sayisi}\nEtiketlenen Gerçek Üye Sayısı: {etiketlenen_gercek_uye_sayisi}")

@Maho.on(events.NewMessage(pattern='^/clearoutput'))
async def clear_output(event):
    await asyncio.sleep(15)
    await event.delete()

