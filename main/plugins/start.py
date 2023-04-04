#Github.com/Vasusen-code

import os
from .. import bot as Drone
from telethon import events, Button
    
S = '/' + 's' + 't' + 'a' + 'r' + 't'

st = "**- HELLO SIR 🫂,\n\n- I AM SAVE RESTRICTED CONTENT BOT.**\n**- Send me the link of the post from the channel, whether it is public or private.**\n**- PRESS /help FOR HELP.**"

@Drone.on(events.callbackquery.CallbackQuery(data="set"))
async def sett(event):    
    Drone = event.client                    
    button = await event.get_message()
    msg = await button.get_reply_message() 
    await event.delete()
    async with Drone.conversation(event.chat_id) as conv: 
        xx = await conv.send_message("Send me any image for thumbnail as a `reply` to this message.")
        x = await conv.get_reply()
        if not x.media:
            xx.edit("No media found.")
        mime = x.file.mime_type
        if not 'png' in mime:
            if not 'jpg' in mime:
                if not 'jpeg' in mime:
                    return await xx.edit("No image found.")
        await xx.delete()
        t = await event.client.send_message(event.chat_id, 'Trying.')
        path = await event.client.download_media(x.media)
        if os.path.exists(f'{event.sender_id}.jpg'):
            os.remove(f'{event.sender_id}.jpg')
        os.rename(path, f'./{event.sender_id}.jpg')
        await t.edit("Temporary thumbnail saved!")
        
@Drone.on(events.callbackquery.CallbackQuery(data="rem"))
async def remt(event):  
    Drone = event.client            
    await event.edit('Trying.')
    try:
        os.remove(f'{event.sender_id}.jpg')
        await event.edit('Removed!')
    except Exception:
        await event.edit("No thumbnail saved.")                        
    


@Drone.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply(f'{st}', 
                      buttons=[
                        [Button.url("CHANNEL LINK", url="https://t.me/mittalbots")],
                        [Button.url("OWNER ID", url="https://t.me/soonbotmaker0")],
                    ])
    try:
        await Bot.start()
        await idle()
    except Exception as e:
        if 'Client is already connected' in str(e):
            pass
        else:
            return
    
       # start help Message
@Drone.on(events.NewMessage(pattern="^/help$"))
async def search(event):
    await event.reply('<b><u>- وات العامـه المقيـدة :</b></u>\nفقط ارسل لي رابط المنشور وسأقوم بجلبه في الحال.\n\n<b><u>- للقنـوات الخاصـه المقيـدة :</b></u>\nاولاً ارسل لي رابط القناة حتى استطيع الانضمام اليهـا ثم بعد ذلك ارسل لي رابط المنشور وسأقوم بجلبه في الحال.', parse_mode="HTML")
    #end help Message




