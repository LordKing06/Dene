from telethon import TelegramClient, events
from gtts import gTTS
from Plugins import Maho 
import os
from Config import *

@Maho.on(events.NewMessage(pattern='^!seslendir (.*)'))
async def handle(event):
    text = event.pattern_match.group(1)
    language = 'tr' # Dil kodunu burada belirtin
    tts = gTTS(text=text, lang=language)
    tts.save('ses.mp3')
    await event.reply(file='ses.mp3')
    
# Sanki oldu he yaparız ya...
