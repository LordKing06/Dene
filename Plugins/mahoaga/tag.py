import asyncio
from telethon import Button, events
from telethon.tl.types import ChannelParticipantsAdmins
from Plugins.mode.config import Maho

anlik_calisan = {}
rxyzdev_tagTot = {}

@Maho.on(events.NewMessage(pattern="^/cancel$"))
async def cancel_spam(event):
    chat_id = event.chat_id
    if chat_id not in anlik_calisan:
        return
    anlik_calisan.pop(chat_id, None)
    await event.respond('**✅ Etiket işlemi başarıyla durduruldu.**')
    await show_output(chat_id)
    await asyncio.sleep(15)  # 15 saniye bekleme süresi
    await delete_output(chat_id)

@Maho.on(events.NewMessage(pattern="^/tag ?(.*)"))
async def mentionall(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond("**Bu komutu sadece grup veya kanallarda kullanabilirsiniz.**")

    async for admin in Maho.iter_participants(chat_id, filter=ChannelParticipantsAdmins):
        if admin.id == event.sender_id:
            break
    else:
        return await event.respond("**Bu komutu yalnızca yöneticiler kullanabilir.**")

    rxyzdev_tagTot[chat_id] = 0

    if event.pattern_match.group(1):
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
    elif event.reply_to_msg_id:
        mode = "text_on_reply"
        msg = await event.get_reply_message()
        if not msg:
            return await event.respond("**Eski Mesajlar için Üyelerden Bahsedemem! (gruba eklemeden önce gönderilen mesajlar)**")
    else:
        return await event.respond("**Geçerli bir mesaj belirtmelisiniz. /tag Merhaba**")

    group_participants = await Maho.get_participants(chat_id, filter=ChannelParticipantsAdmins)

    if mode == "text_on_cmd":
        anlik_calisan[chat_id] = True
        usrnum = 0
        usrtxt = ""
        rxyzdev_tagTot[chat_id] = 0
        await event.respond(f"**✅ Etiket işlemi başarıyla başlatıldı.**\n**Etiketleme işlemi için kullanılan ifade:** {msg}")

        for usr in group_participants:
            if usr.deleted or usr.bot:
                continue

            usrnum += 1
            usrtxt += f"⌯ [{usr.first_name}](tg://user?id={usr.id})\n"

            if chat_id not in anlik_calisan:
                return

            if usrnum == 5:
                await Maho.send_message(chat_id, f"⌯ 📢 {msg}\n\n{usrtxt}")
                await asyncio.sleep(3)
                usrnum = 0
                usrtxt = ""

            rxyzdev_tagTot[chat_id] += 1

        sender = await event.get_sender()
        rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"

        if chat_id in rxyzdev_tagTot:
            member_count = await Maho.get_participants(chat_id, filter=ChannelParticipantsAdmins)
            tag_count = rxyzdev_tagTot[chat_id]

            output = f"✅ Etiket işlemi başarıyla durduruldu.\n\n👥 Genel üye sayısı: {len(member_count)}\n📢 Etiketlenen toplam üye sayısı: {tag_count}\n⛔ Silinen hesaplar ve botlara etiket atılmadı."
            await Maho.send_message(chat_id, output)
            await asyncio.sleep(20)  # 20 saniye bekleme süresi
            await Maho.send_message(chat_id, "🔒 Etiket çıktısı süresi sona erdi. Etiket işlemi tamamlandı.")
            await show_output(chat_id)

    if mode == "text_on_reply":
        anlik_calisan[chat_id] = True
        usrnum = 0
        usrtxt = ""
        rxyzdev_tagTot[chat_id] = 0

        for usr in group_participants:
            usrnum += 1
            usrtxt += f"⌯ [{usr.first_name}](tg://user?id={usr.id})\n"

            if chat_id not in anlik_calisan:
                return

            if usrnum == 5:
                await Maho.send_message(chat_id, usrtxt, reply_to=msg)
                await asyncio.sleep(5)
                usrnum = 0
                usrtxt = ""

            rxyzdev_tagTot[chat_id] += 1

        sender = await event.get_sender()
        rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"

        if chat_id in rxyzdev_tagTot:
            member_count = await Maho.get_participants(chat_id, filter=ChannelParticipantsAdmins)
            tag_count = rxyzdev_tagTot[chat_id]

            output = f"✅ Etiket işlemi başarıyla durduruldu.\n\n👥 Genel üye sayısı: {len(member_count)}\n📢 Etiketlenen toplam üye sayısı: {tag_count}\n⛔ Silinen hesaplar ve botlara etiket atılmadı."
            await Maho.send_message(chat_id, output)
            await asyncio.sleep(20)  # 20 saniye bekleme süresi
            await Maho.send_message(chat_id, "🔒 Etiket çıktısı süresi sona erdi. Etiket işlemi tamamlandı.")
            await show_output(chat_id)

async def show_output(chat_id):
    member_count = await Maho.get_participants(chat_id, filter=ChannelParticipantsAdmins)
    tag_count = rxyzdev_tagTot[chat_id]

    output = f"👥 Genel üye sayısı: {len(member_count)}\n📢 Etiketlenen toplam üye sayısı: {tag_count}\n⛔ Silinen hesaplar ve botlara etiket atılmadı."
    await Maho.send_message(chat_id, output)

async def delete_output(chat_id):
    async for msg in Maho.iter_messages(chat_id, reverse=True):
        try:
            await msg.delete()
        except Exception as e:
            print(f"Hata: {e}")

    
