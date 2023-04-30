from telethon import TelegramClient, events
from Plugins import Maho
from Config import *

@Maho.on(events.NewMessage(pattern='^!eros (.*)'))
async def handle(event):
    name = event.pattern_match.group(1)
    users = await Maho.get_entity(name)
    if not users:
        await event.reply(f"No user found with the name {name}")
        return
    user1 = users[0].user.full_name
    user2 = event.sender.first_name
    await event.reply(f"{user1} and {user2} sitting in a tree, K-I-S-S-I-N-G!")
