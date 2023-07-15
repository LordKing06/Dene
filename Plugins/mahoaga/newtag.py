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
async def mentionall(event):
    global anlik_calisan, etiketlenen_uyeler

    if event.is_private:
        return await event.respond("**Bu komut gruplar ve kanallar için geçerlidir❗️**")

    chat_id = event.chat_id
    user_id = event.sender_id

    admins = []
    async for admin in Maho.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
        admins.append(admin.id)
    if event.sender_id not in admins:
        return await event.respond("**Bu komutu sadece yöneticiler kullanabilir. 👮‍♂️**")

    async def get_admins():
        admins = []
        async for admin in Maho.iter_participants(chat_id, filter=ChannelParticipantsAdmins):
            admins.append(admin.id)
        return admins

    if user_id not in await get_admins():
        return await event.respond("**Bu komutu yalnızca yöneticiler kullanabilir. 👮‍♂️**")

    mode = "text_on_cmd"
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

    if msg is None:
        return await event.respond("Önceki mesajları etiketlemek için kullanamıyorum.")

    if mode == "text_on_cmd":
        anlik_calisan[chat_id] = True
        etiketlenen_uyeler[chat_id] = 0
        usrnum = 0
        usrtxt = ""
        async for usr in Maho.iter_participants(chat_id):
            if usr.bot or usr.deleted:
                continue
            usrnum += 1
            usrtxt += f" [{usr.first_name}](tg://user?id={usr.id}) ,"
            if chat_id not in anlik_calisan:
                await event.respond()
                return
            if usrnum == 5:
                await Maho.send_message(chat_id, f"💡 {usrtxt}\n\n{msg}")
                etiketlenen_uyeler[chat_id] += usrnum
                await asyncio.sleep(10)
                usrnum = 0
                usrtxt = ""
        
        # Etiketleme işlemi bittiğinde toplam etiketlenen üye sayısını belirt
        genel_uye_sayisi = 0
        async for _ in Maho.iter_participants(chat_id):
            genel_uye_sayisi += 1
        await event.respond(f"Etiketlenen Üye Sayısı: {etiketlenen_uyeler[chat_id]}\nGenel Üye Sayısı: {genel_uye_sayisi}")

    if mode == "text_on_reply":
        anlik_calisan[chat_id] = True
        etiketlenen_uyeler[chat_id] = 0
        usrnum = 0
        usrtxt = ""
        async for usr in Maho.iter_participants(chat_id):
            if usr.bot or usr.deleted:
                continue
            usrnum += 1
            usrtxt += f" [{usr.first_name}](tg://user?id={usr.id}) ,"
            if chat_id not in anlik_calisan:
                await event.respond("İşlem başarıyla durduruldu. ✅")
                return
            if usrnum == 5:
                await Maho.send_message(chat_id, usrtxt, reply_to=msg)
                etiketlenen_uyeler[chat_id] += usrnum
                await asyncio.sleep(10)
                usrnum = 0
                usrtxt = ""
        
        # Etiketleme işlemi bittiğinde toplam etiketlenen üye sayısını belirt
        genel_uye_sayisi = 0
        async for _ in Maho.iter_participants(chat_id):
            genel_uye_sayisi += 1
        await event.respond(f"Etiketlenen Üye Sayısı: {etiketlenen_uyeler[chat_id]}\nGenel Üye Sayısı: {genel_uye_sayisi}")

    # 5 saniye sonra mesajı sil
    await asyncio.sleep(5)
    await event.delete()

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
        
        # Otomatik etiketleme durduğunda çıktı mesajı gönder
        await Maho.send_message(chat_id, "Otomatik etiketleme işlemi durduruldu. ✅")

@Maho.on(events.NewMessage(pattern='^/info'))
async def stats(event):
    global etiketlenen_uyeler
    chat_id = event.chat_id

    if chat_id in etiketlenen_uyeler:
        genel_uye_sayisi = 0
        async for _ in Maho.iter_participants(chat_id):
            genel_uye

