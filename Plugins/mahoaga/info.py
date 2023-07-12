from telethon import events
import asyncio
import random
from telethon import events
from Plugins.mode.config import Maho

@Maho.on(events.NewMessage(pattern="^/id ?(.*)"))
async def id(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        user_id = previous_message.sender_id
        chat_id = event.chat_id
        if event.is_private:
            return await event.reply(f"**Kullanıcı Telegram id:** `{user_id}`")
        else:
            return await event.reply(f"**kullanıcı  id:** `{user_id}`\n**grup id:** `{chat_id}`")

#Tag_0605 
    else:
        user_id = event.sender_id
        chat_id = event.chat_id
        if event.is_private:
            return await event.reply(f"**Kullanıcı Telegram id:** `{user_id}`")
        else:
            return await event.reply(f"**Kullanıcı id:** `{user_id}`\n**grup id:** `{chat_id}`")

print("Kimlik bilgileri")
