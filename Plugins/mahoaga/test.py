from telethon import TelegramClient, events, Button
from telethon.tl.types import ChannelParticipantsAdmins
from Config import *

client = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)

async def is_bot(event, user_id):
    """
    Kullanıcının bot olup olmadığını kontrol eden yardımcı bir fonksiyondur.
    """
    user = await event.client.get_entity(user_id)
    return user.bot

@client.on(events.NewMessage)
async def handle_new_message(event):
    """
    Yeni mesajları dinleyen bir fonksiyondur.
    """
    # Botlar mesajları işleme almamalıdır.
    if event.is_private and not await is_bot(event, event.sender_id):
        chat_id = event.chat_id
        # Mesajın içeriğindeki botları etiketleme.
        async for user in event.client.iter_participants(chat_id, filter=ChannelParticipantsAdmins):
            if not user.bot:
                await event.respond(f'@{user.username}')

client.start()
client.run_until_disconnected()
