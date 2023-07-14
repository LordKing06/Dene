import asyncio
from telethon import Button, events
from telethon.tl.types import ChannelParticipantsAdmins, ChannelParticipantsRecent
from asyncio import sleep
from Plugins.mode.config import Maho

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
        await asyncio.sleep(15)  # 15 saniye bekleme süresi
        await delete_output(event.chat_id)

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
        return await event.respond("**Bu komutu yalnızca yöneticiler kullanabilir.**")

    if event.pattern_match.group(1):
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
    elif event.reply_to_msg_id:
        mode = "text_on_reply"
        msg = await event.get_reply_message()
        if msg == None:
            return await event.respond("**Eski Mesajlar için Üyelerden Bahsedemem! (gruba eklemeden önce gönderilen mesajlar)**")
    else:
        return await event.respond("**Geçerli bir mesaj belirtmelisiniz. /tag Merhaba**")

    group_participants = await Maho.get_participants(event.chat_id)

    if mode == "text_on_cmd":
        anlik_calisan.append(event.chat_id)
        usrnum = 0
        usrtxt = ""
        rxyzdev_tagTot[event.chat_id] = 0
        await event.respond("**✅ Etiket işlemi başarıyla başlatıldı.**")
        await event.respond(f"**Etiketleme işlemi için kullanılan ifade:** {msg}")

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

            rxyzdev_tagTot[event.chat_id] += 1

        sender = await event.get_sender()
        rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"

        if event.chat_id in rxyzdev_tagTot:
            member_count = await Maho.get_participants(event.chat_id, filter=ChannelParticipantsRecent())
            tag_count = rxyzdev_tagTot[event.chat_id]
            total_count = len(member_count)

            output = f"✅ Etiket işlemi başarıyla durduruldu.\n\n👥 Genel üye sayısı: {len(member_count)}\n📢 Etiketlenen toplam üye sayısı: {tag_count}\n⛔ Silinen hesaplar ve botlara Etiket atılmadı."
            await Maho.send_message(event.chat_id, output)
            await sleep(20)  # 20 saniye bekleme süresi
            await Maho.send_message(event.chat_id, "🔒 Etiket çıktısı süresi sona erdi. Etiket işlemi tamamlandı.")
            await show_output(event.chat_id)

    if mode == "text_on_reply":
        anlik_calisan.append(event.chat_id)
        usrnum = 0
        usrtxt = ""
        rxyzdev_tagTot[event.chat_id] = 0

        for usr in group_participants:
            usrnum += 1
            usrtxt += f"⌯ [{usr.first_name}](tg://user?id={usr.id})\n"

            if event.chat_id not in anlik_calisan:
                return

            if usrnum == 5:
                await Maho.send_message(event.chat_id, usrtxt, reply_to=msg)
                await asyncio.sleep(5)
                usrnum = 0
                usrtxt = ""

            rxyzdev_tagTot[event.chat_id] += 1

        sender = await event.get_sender()
        rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"

        if event.chat_id in rxyzdev_tagTot:
            member_count = await Maho.get_participants(event.chat_id, filter=ChannelParticipantsRecent())
            tag_count = rxyzdev_tagTot[event.chat_id]
            total_count = len(member_count)

            output = f"✅ Etiket işlemi başarıyla durduruldu.\n\n👥 Genel üye sayısı: {len(member_count)}\n📢 Etiketlenen toplam üye sayısı: {tag_count}\n⛔ Silinen hesaplar ve botlara Etiket atılmadı."
            await Maho.send_message(event.chat_id, output)
            await sleep(20)  # 20 saniye bekleme süresi
            await Maho.send_message(event.chat_id, "🔒 Etiket çıktısı süresi sona erdi. Etiket işlemi tamamlandı.")
            await show_output(event.chat_id)


async def show_output(chat_id):
    member_count = await Maho.get_participants(chat_id, filter=ChannelParticipantsRecent())
    tag_count = rxyzdev_tagTot[chat_id]
    total_count = len(member_count)

    output = f"👥 Genel üye sayısı: {len(member_count)}\n📢 Etiketlenen toplam üye sayısı: {tag_count}\n⛔ Silinen hesaplar ve botlara Etiket atılmadı."
    await Maho.send_message(chat_id, output)


async def delete_output(chat_id):
    messages = await Maho.get_messages(chat_id, limit=None)  # Tüm mesajları almak için limit=None olarak günc

  
    output = f"👥 Genel üye sayısı: {len(member_count)}\n📢 Etiketlenen toplam üye sayısı: {tag_count}\n⛔ Silinen hesaplar ve botlara Etiket atılmadı."
    await Maho.send_message(chat_id, output)



async def delete_output(chat_id):
    messages = await Maho.get_messages(chat_id)
    for msg in messages:
        await msg.delete()



