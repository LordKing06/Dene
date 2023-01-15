from telethon import events

import asyncio

from Plugins.events import register



@register(outgoing=True, pattern="^/sstag ?(.*)")

async def sstag(event):

    if not event.is_reply:

        return await event.edit('```Lütfen bir mesaja yanıt verin!```')

    

    sure = event.pattern_match.group(1)

    if (sure == ''):

        sure = 1.5

    else:

        try:

            sure = float(sure)

        except:

            sure = 1.5

    await event.edit(f'```{sure} saniye baz alınıyor...```')

    mesaj = await event.get_reply_message()

    await event.edit('```Gruplar getiriliyor...```')

    gruplar = await event.client.get_dialogs()

    await event.edit(f'```{len(gruplar)} adet sohbet bulundu! Gruplar seçiliyor...```')

    

    i = 0

    for grup in gruplar:

        if grup.is_group:

            await event.edit(f'```{grup.name} grubuna mesajınız gönderiliyor...```')

            try:

                await grup.send_message(mesaj)

            except:

                await event.edit(f'```❌ {grup.name} grubuna mesajınız gönderilemedi!```')

                await asyncio.sleep(sure)

                continue

            i += 1

            await event.edit(f'```✅ {grup.name} grubuna mesajınız gönderildi!```')

            await asyncio.sleep(sure)

    await event.edit(f'```✅ {i} adet gruba mesajınız gönderildi!```')

