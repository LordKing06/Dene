```python
from telethon import TelegramClient, events, types
from telethon.sessions import StringSession
from asyncio import sleep
from Config import *

# StringSession ile bir Telegram istemcisini başlatıyoruz
client = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)

# etiketi çalıştıran kullanıcıları kaydetmek için değişken oluşturuyoruz
etiket_calisan = []

# ChatAction handler, silinen hesaplar ve botları görmez
@client.on(events.ChatAction())
async def chat_action_handler(event):
    # kullanıcı ayrıldıysa
    if isinstance(event.action, types.ChatActionUserLeft):
        user = await event.client.get_entity(event.action.user_id)
        # kullanıcı hesabı silinmişse, mesajı atla
        if user.deleted:
            return
        else:
            print(f"Kullanıcı {user.first_name} sohbetten ayrıldı")
    # kullanıcı katıldıysa
    elif isinstance(event.action, types.ChatActionUserJoined):
        user = await event.client.get_entity(event.action.user_id)
        # kullanıcı bot ise, mesajı atla
        if user.bot:
            return
        else:
            print(f"Kullanıcı {user.first_name} sohbete katıldı")
    return

# etiket atmak için komut işleyicisi
@client.on(events.NewMessage(pattern="/etiket"))
async def etiket_handler(event):
    # etiket işlemi zaten başlatılmışsa, mesajı atla
    if event.chat_id in etiket_calisan:
        await event.respond("Etiketleme işlemi zaten başlatılmış.")
        return

    # toplam üye sayısını alın
    try:
        chat = await client.get_entity(event.chat_id)
        chat_members = await client.get_participants(event.chat_id, aggressive=True)
        total_members = chat_members.total
    except:
        total_members = 0

    # etiketleme işlemini başlat
    etiket_calisan.append(event.chat_id)
    await event.respond(f"Etiketleme işlemi başlatıldı. Toplam üye sayısı: {total_members}. Lütfen bekleyin...")

    async for user in client.iter_participants(event.chat_id, filter=types.ChannelParticipantsRecent):
        # kullanıcı hesabı silinmiş veya bot ise, etiket yapma
        if user.deleted or user.bot:
            continue

        # kullanıcının adını etiketle
        await client.send_message(event.chat_id, f"@{user.username or user.first_name}")
        await sleep(1) # her kullanıcıdan sonra 1 saniye bekleyin

        # etiketleme işlemi durdurulduysa, işlemi sonlandırın
        if event.chat_id not in etiket_calisan:
            await event.respond("Etiketleme işlemi durduruldu.")
            return

    # etiketleme işlemi bitti, kullanıcı listesinden chat id'yi kaldırın
    etiket_calisan.remove(event.chat_id)
    await event.respond("Etiketleme işlemi tamamlandı.")

# etiketleme işlemi durdurmak için komut işleyicisi
@client.on(events.NewMessage(pattern="/durdur"))
async def durdur_handler(event):
    # etiket işlemi zaten başlatılmamışsa, mesajı atla
    if event.chat_id not in etiket_calisan:
        await event.respond("Etiketleme işlemi zaten başlatılmamış.")
        return

    # etiketleme işlemi durduruldu mesajı gönderin ve kullanıcı listesinden chat id'yi kaldırın
    etiket_calisan.remove(event.chat_id)
    await event.respond("Etiketleme işlemi durduruldu.")

# istemciyi çalıştırın
client.start()
client.run_until_disconnected()
```

Yukarıdaki kodda, `events.ChatAction()` handler aracılığıyla silinen hesapları ve botları görmez. `etiket` komutunu kullanarak etiketleme işlemi yapar ve `durdur` komutu kullanarak işlemi durdurabilirsiniz. Ayrıca, `etiket` komutu çağrılırken, toplam üye sayısını alır ve mesaj olarak belirtir.
