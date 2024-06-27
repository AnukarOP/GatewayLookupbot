from telethon import TelegramClient, events, types, Button
from telethon.tl import functions
from telethon.tl.types import Channel, Chat, User
import webbrowser
webbrowser.open('')
import time
import random
import re
import os
import requests
import json
import string
import urllib.parse
from bs4 import BeautifulSoup
from collections import defaultdict
from datetime import datetime, timedelta
api_id = 'API_ID_HERE' # Keep this as it is 
api_hash = 'API_HASH_HERE' # same heree
client_token = 'BOT_TOKEN_HERE'

#coded by @AnukarOP 

admin_ids = [ADMIN_ID_1, ADMIN_ID_2, ADMIN_ID_3]  # Example admin IDs

def is_user_admin(user_id):
    return user_id in admin_ids

message_counts = defaultdict(lambda: 0)
last_message_time = defaultdict(lambda: datetime.min)
global time_window
time_window = timedelta(seconds=15)
pre_window = timedelta(seconds=10)
site_checking = {}
credits = {}
global credit
credit = {}
generated_codes = []
vip = [VIP_ID_1,VIP_ID_2,VIP_ID_3]
def normalize_url(url):
    parsed_url = urllib.parse.urlparse(url)
    normalized_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
    return normalized_url
def generate_redeem_code():
    code = '-'.join(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4)) for _ in range(4))
    cod=(f"`{code}`")
    return code

premium = "premium.txt"
if not os.path.exists(premium):
    open(premium, 'a').close()
        

def readprem():
    with open(premium, 'r') as file:
        premium_ids = file.readlines()
        premium_ids = [int(user_id.strip()) for user_id in premium_ids if user_id.strip().isdigit()]
        return premium_ids


pre = readprem()
pre_id = []
r_us=[]

def add_to_premium(user_id):
    with open(premium, 'a') as file:
        file.write(str(user_id) + "\n")
client = TelegramClient('session_name', api_id, api_hash).start(bot_token=client_token)
site_checking = {}
def read_user_credit(user_id):
    user_credit_file = f"{user_id}_credit.txt"
    if os.path.exists(user_credit_file):
        with open(user_credit_file, "r") as file:
            return int(file.read())
    return 0
@client.on(events.NewMessage(pattern='/refresh'))
async def handle_create(event):
    user_id = event.sender_id

    # Read user's credit from file
    user_credit_file = f"{user_id}_credit.txt"
    if os.path.exists(user_credit_file):
        with open(user_credit_file, "r") as file:
            global credit_value
            credit_value = int(file.read())
    else:
        credit_value = 0


    if user_id in pre:
        if user_id in r_us:
            await event.respond('𝗔𝗹𝗿𝗲𝗮𝗱𝘆 𝗿𝗲𝗳𝗿𝗲𝘀𝗵𝗶𝗻𝗴 𝗱𝗼𝗻𝗲!')
        else:
            credit_value += 25
            await event.respond('💫')
            r_us.append(user_id)
            
    elif user_id in vip:
        if user_id in r_us:
            await event.respond('𝗔𝗹𝗿𝗲𝗮𝗱𝘆 𝗿𝗲𝗳𝗿𝗲𝘀𝗵𝗶𝗻𝗴 𝗱𝗼𝗻𝗲!')
        else:
            credit_value += 50000
            await event.respond('💫')
    else:
        if user_id in r_us:
            await event.respond('𝗔𝗹𝗿𝗲𝗮𝗱𝘆 𝗿𝗲𝗳𝗿𝗲𝘀𝗵𝗶𝗻𝗴 𝗱𝗼𝗻𝗲!')
        else:
            credit_value += 5
        await event.respond('💫')
        r_us.append(user_id)
    with open(user_credit_file, "w") as file:
        file.write(str(credit_value))
@client.on(events.NewMessage(pattern='/info'))
async def handle_create(event):
    user_id = event.sender_id
    user_credit_file = f"{user_id}_credit.txt"
    if os.path.exists(user_credit_file):
        with open(user_credit_file, "r") as file:
            user_credit = int(file.read())
    else:
        user_credit = 0
    if user_id in vip:
        user = event.sender
        user_id = event.sender.id
        creditz = credit.get(user_id,0)
        fn = f"[{user.first_name}](tg://user?id={user.id})"
        ai = f"[{user.id}!](tg://user?id={user.id})"
        await event.respond(f"""**Your Details** 🔐
𝙒𝙚𝙡𝙘𝙤𝙢𝙚 {fn}
**See your account status:**

👨🏻‍💼 Plan: `VIP 👑`
💳 Credits: `♾️`

🔥 Status:
⊛ Account ID: `{event.sender.id}`
⊛ Name: {fn}""", reply_to=event)
    elif user_id in pre:
        user = event.sender
        user_id = event.sender.id
        creditx = credit.get(user_id,0)
        fn = f"[{user.first_name}](tg://user?id={user.id})"
        ai = f"[{user.id}!](tg://user?id={user.id})"
        await event.respond(f"""**Your Details** 🔐
𝙒𝙚𝙡𝙘𝙤𝙢𝙚 {fn}
**See your account status:**

👨🏻‍💼 Plan: `Premium`
💳 Credits: `{user_credit}`

🔥 Status:
⊛ Account ID: `{event.sender.id}`
⊛ Name: {fn}""", reply_to=event)
    else:
        user = event.sender
        user_id = event.sender.id
        creditz = credit.get(user_id)
        fn = f"[{user.first_name}](tg://user?id={user.id})"
        ai = f"[{user.id}!](tg://user?id={user.id})"
        
        await event.respond(f"""**Your Details** 🔐
𝙒𝙚𝙡𝙘𝙤𝙢𝙚 {fn}
**See your account status:**

👨🏻‍💼 Plan: `Free`
💳 Credits: `{user_credit}`

🔥 Status:
⊛ Account ID: `{event.sender.id}`
⊛ Name: {fn}""", reply_to=event)
@client.on(events.NewMessage(pattern='/codes'))
async def handle_create(event):
    user_id = event.sender_id
    if user_id in vip:
        await event.respond('🔹𝗧𝗵𝗲𝘀𝗲 𝗮𝗿𝗲 𝘁𝗵𝗲 𝗖𝗼𝗱𝗲𝘀 𝘄𝗵𝗶𝗰𝗵 𝘄𝗲𝗿𝗲 𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 𝗮𝗻𝗱 𝗻𝗼𝘁 𝘂𝘀𝗲𝗱 𝘆𝗲𝘁. \n\n'+str(generated_codes))
@client.on(events.NewMessage(pattern='/create'))
async def handle_create(event):
    user_id = event.sender_id
    if user_id in vip:
        try:
            _, num_codes = event.raw_text.split()
            num_codes = int(num_codes)
            codes = [generate_redeem_code() for _ in range(num_codes)]
            generated_codes.extend(codes)
            code_message = ' ┏━━━━━━━⍟\n┃ 𝗛𝗲𝗿𝗲 𝗶𝘀 𝘆𝗼𝘂𝗿 𝗥𝗲𝗱𝗲𝗲𝗺 𝗰𝗼𝗱𝗲𝘀 ✅\n┗━━━━━━━━━━━⊛\n\n⊙ ' + '\n⊙ '.join(f'`{code}`' for code in codes) + ' \n\n━━━━━━━━━━━━━━━━\nPlease note that `02` credits each. You can redeem them using the command \n`/redeem` (@GatewayLookupbot)'
            await event.respond(code_message, parse_mode='Markdown')
        except (ValueError, TypeError):
            pass

def generate_redeem_code():
    code = '-'.join(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4)) for _ in range(4))
    return code


@client.on(events.NewMessage(pattern='/redeem'))
async def handle_redeem(event):
    redeem_code = event.raw_text.split()[-1].strip()
    if redeem_code in generated_codes:
        generated_codes.remove(redeem_code)
        user_id = event.sender.id
        global creditz
        
        user_credit_file = f"{user_id}_credit.txt"
        if os.path.exists(user_credit_file):
            with open(user_credit_file, "r") as file:
                credit_value = int(file.read())
        else:
            credit_value = 0
        new_credit_value = credit_value + 2
        
        with open(user_credit_file, "w") as file:
            file.write(str(new_credit_value))
        msg = (f"""𝑵𝒆𝒘 𝒖𝒔𝒆𝒓 𝑹𝒆𝒅𝒆𝒆𝒎𝒆𝒅 ✅

__𝐔𝐬𝐞𝐫 𝐃𝐞𝐭𝐚𝐢𝐥𝐬__ :
⊛ **Username** : @{event.sender.username}
⊛ **Userid** : `{event.sender.id}`
⊛ **Code** : `{redeem_code}`
⊛ **Bot** : @GatewayLookupbot""")
        await client.send_message(LOG_GROUP_ID,msg)
        
        
        await event.respond(f"𝗥𝗲𝗱𝗲𝗲𝗺𝗲𝗱 𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 ✅\n\n__𝗗𝗲𝘁𝗮𝗶𝗹𝘀__ :  \n**⊛ Credits Added** : `02` \n**[⊙](https://i.ibb.co/CMcdMjf/Blue-Tosca-Geometric-Technology-Linkedln-Banner.png) User ID** : `{event.sender_id}`\n\n❛ ━━━━･━━━━･━━━━ ❜", parse_mode='Markdown', reply_to=event)
    else:
        await event.respond('⚠️ 𝗧𝗵𝗲 𝗽𝗿𝗼𝘃𝗶𝗱𝗲𝗱 𝗿𝗲𝗱𝗲𝗲𝗺 𝗰𝗼𝗱𝗲 𝗶𝘀 𝗶𝗻𝘃𝗮𝗹𝗶𝗱 𝗼𝗿 𝗵𝗮𝘀 𝗮𝗹𝗿𝗲𝗮𝗱𝘆 𝗯𝗲𝗲𝗻 𝗿𝗲𝗱𝗲𝗲𝗺𝗲𝗱. \n𝗣𝗹𝗲𝗮𝘀𝗲 𝗽𝗿𝗼𝘃𝗶𝗱𝗲 𝗮 𝘃𝗮𝗹𝗶𝗱 𝗰𝗼𝗱𝗲...', reply_to=event)
@client.on(events.NewMessage(pattern='/approve'))
async def approve_user(event):
    global premium_file_path
    if event.sender_id in vip:
        try:
            user_id = int(event.text.split(" ")[1])
            add_to_premium(user_id)
            pre_id.append(user_id)
            
            await event.respond(f"**Added** {user_id} to **Premium** list. ✅")
        except (IndexError, ValueError):
            await event.respond("Invalid usage. The correct format is: /approve <user_id>")
def find_payment_gateways(response_text):
    detected_gateways = []

    if "paypal" in response_text.lower():
        detected_gateways.append("PayPal")
    if "stripe" in response_text.lower():
        detected_gateways.append("Stripe")
    if "braintree" in response_text.lower():
        detected_gateways.append("Braintree")
    if "square" in response_text.lower():
        detected_gateways.append("Square")
    if "cybersource" in response_text.lower():
        detected_gateways.append("Cybersource")    
    if "authorize.net" in response_text.lower():
        detected_gateways.append("Authorize.Net")
    if "2checkout" in response_text.lower():
        detected_gateways.append("2Checkout")
    if "adyen" in response_text.lower():
        detected_gateways.append("Adyen")
    if "worldpay" in response_text.lower():
        detected_gateways.append("Worldpay")
    if "sagepay" in response_text.lower():
        detected_gateways.append("SagePay")
    if "checkout.com" in response_text.lower():
        detected_gateways.append("Checkout.com")
    if "shopify" in response_text.lower():
        detected_gateways.append("Shopify")
    if "razorpay" in response_text.lower():
        detected_gateways.append("Razorpay") 
    if "bolt" in response_text.lower():
        detected_gateways.append("Bolt")  
    if "paytm" in response_text.lower():
        detected_gateways.append("Paytm")    
    if "venmo" in response_text.lower():
        detected_gateways.append("Venmo")    
    if "pay.google.com" in response_text.lower():
        detected_gateways.append("Google pay")    
    if "revolut" in response_text.lower():
        detected_gateways.append("Revolut")    
    if "eway" in response_text.lower():
        detected_gateways.append("Eway")
    if "woocommerce" in response_text.lower():
        detected_gateways.append("Woocommerce")  
    if "upi" in response_text.lower():
        detected_gateways.append("UPI")
    if "apple.com" in response_text.lower():
        detected_gateways.append("Apple pay")  
    if "payflow" in response_text.lower():
        detected_gateways.append("PayFlow") 
    if "payeezy" in response_text.lower():
        detected_gateways.append("Payeezy")  
    if "paddle" in response_text.lower():
        detected_gateways.append("Paddle")  
    if "payoneer" in response_text.lower():
        detected_gateways.append("Payoneer")  
    if "recurly" in response_text.lower():
        detected_gateways.append("Recurly")  
    if "klarna" in response_text.lower():
        detected_gateways.append("Klarna")  
    if "paysafe" in response_text.lower():
        detected_gateways.append("Paysafe")  
    if "webmoney" in response_text.lower():
        detected_gateways.append("WebMoney")  
    if "payeer" in response_text.lower():
        detected_gateways.append("Payeer")  
    if "payu" in response_text.lower():
        detected_gateways.append("Payu")    
    if "skrill" in response_text.lower():
        detected_gateways.append("Skrill")     
    # Add more checks for other payment gateways

    # If no specific patterns are found, return "Unknown"
    if not detected_gateways:
        detected_gateways.append("Unknown")

    return detected_gateways
    

def find_payment_gateway(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        # Pass the response text to the find_payment_gateways function
        detected_gateways = find_payment_gateways(response.text)

        return detected_gateways

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return ["Error"]
async def is_user_in_channel(user_id, channel_id):
    try:
        participants = await client.get_participants(channel_id)
        members_ids = [participant.id for participant in participants]
        return user_id in members_ids
    except Exception as e:
        print(f"Error checking channel membership: {e}")
        return False

@client.on(events.NewMessage(pattern='/broadcast'))
async def handle_broadcast(event):
    if not is_user_admin(event.sender_id):
        await event.reply("🛑 𝗬𝗼𝘂'𝗿𝗲 𝗻𝗼𝘁 𝗮𝘂𝘁𝗵𝗼𝗿𝗶𝘇𝗲𝗱 𝘁𝗼 𝘂𝘀𝗲 𝘁𝗵𝗶𝘀 𝗰𝗼𝗺𝗺𝗮𝗻𝗱.")
        return

    try:
        _, message = event.raw_text.split(maxsplit=1)
    except ValueError:
        await event.reply("Usage: /broadcast <message>")
        return

    with open("registered_chats.txt", "r") as file:
        chat_ids = [int(line.strip()) for line in file.readlines()]

    for chat_id in chat_ids:
        try:
            if event.is_reply:
                replied_message = await event.get_reply_message()
                await client.forward_messages(chat_id, replied_message)
            else:
                await client.send_message(chat_id, message)
        except Exception as e:
            print(f"Failed to send message to {chat_id}: {e}")

    await event.reply("𝗠𝗲𝘀𝘀𝗮𝗴𝗲 𝗯𝗿𝗼𝗮𝗱𝗰𝗮𝘀𝘁𝗲𝗱 𝘀𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆. ✅")



@client.on(events.NewMessage(pattern='/register'))
async def register(event):
    chat_id = event.chat_id
    with open("registered_chats.txt", "a+") as file:
        file.seek(0)
        # Check if chat_id is already in the file
        if str(chat_id) not in file.read():
            file.write(f"{chat_id}\n")
            await event.respond("𝗧𝗵𝗮𝗻𝗸 𝘆𝗼𝘂 𝗙𝗼𝗿 𝘆𝗼𝘂𝗿 𝗥𝗲𝗴𝗶𝘀𝘁𝗿𝗮𝘁𝗶𝗼𝗻 ✅\n **Hope you will have Great Experience ahead!**", reply_to=event)
        else:
            await event.respond("𝗬𝗼𝘂 𝗮𝗿𝗲 𝗮𝗹𝗿𝗲𝗮𝗱𝘆 𝗿𝗲𝗴𝗶𝘀𝘁𝗲𝗿𝗲𝗱! ❤️", reply_to=event)

@client.on(events.NewMessage(pattern='/stats'))
async def stats(event):
    if not is_user_admin(event.sender_id):
        await event.reply("🛑 𝗬𝗼𝘂'𝗿𝗲 𝗻𝗼𝘁 𝗮𝘂𝘁𝗵𝗼𝗿𝗶𝘇𝗲𝗱 𝘁𝗼 𝘂𝘀𝗲 𝘁𝗵𝗶𝘀 𝗰𝗼𝗺𝗺𝗮𝗻𝗱.")
        return

    with open("registered_chats.txt", "r") as file:
        chat_ids = [int(line.strip()) for line in file.readlines()]

    await event.reply(f"📊 𝗧𝗼𝘁𝗮𝗹 𝗿𝗲𝗴𝗶𝘀𝘁𝗲𝗿𝗲𝗱 𝘂𝘀𝗲𝗿𝘀 : `{len(chat_ids)}`", reply_to=event)

@client.on(events.NewMessage(pattern='/start'))
async def cmd_start(event):
    texta = """
 🪄
    """
    edit = await event.respond(texta)
    time.sleep(1.5)
    textb = """
✨
    """
    edit = await edit.edit(textb)
    time.sleep(1.5)
    textc = """
 🚀
    """
    edit = await edit.edit(textc)
    time.sleep(1.5)
    url = 'https://t.me/BlackHeadsOP'
    buttons = [
        [Button.inline('Cmds', b'cmd'),
         Button.url('Channel', url)]
    ]
    textd = f"""
𝗛𝗲𝘆 {event.sender.first_name}
𝗪𝗘𝗟𝗖𝗢𝗠𝗘 𝗧𝗢 『ᏰᏂ』 ⛈

⚠️ 𝗗𝗼 /register 𝗕𝗲𝗳𝗼𝗿𝗲 𝗨𝘀𝗶𝗻𝗴 𝗺𝗲.
"""
    edit = await edit.edit(textd, buttons=buttons)

@client.on(events.CallbackQuery(data=b'cmd'))
async def cmd_callback(event):
    try:
        buttons=[
       [Button.inline('𝗕𝗔𝗖𝗞', b'back')]]
        new_text = """𝑲𝒏𝒐𝒘 𝒎𝒐𝒓𝒆... ✨

● 𝗦𝗶𝘁𝗲 𝗟𝗼𝗼𝗸𝘂𝗽 ⚙
➔ /bh <site url without https>

● 𝗔𝗰𝗰𝗼𝘂𝗻𝘁 𝗗𝗲𝘁𝗮𝗶𝗹𝘀 👨🏻‍💼
➔ /info

● 𝗥𝗲𝗱𝗲𝗲𝗺 𝗰𝗼𝗱𝗲 🤝🏻
➔ /redeem

● 𝗔𝗯𝗼𝘂𝘁 ⚡️
➔ /about

𝘼𝙡𝙡 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 𝙖𝙧𝙚 𝙡𝙞𝙨𝙩𝙚𝙙 𝙝𝙚𝙧𝙚, 𝙐𝙨𝙚 𝙩𝙝𝙚𝙢 𝙬𝙞𝙨𝙚𝙡𝙮!

     ❛ ━━━━･━━━━･━━━━ ❜"""
        await event.edit(new_text,buttons=buttons)
    except Exception as e:
        print(e)

@client.on(events.CallbackQuery(data=b'back'))
async def back_callback(event):
    try:
        url = 'https://t.me/BlackHeadsOP'
        buttons = [
            [Button.inline('Cmds', b'cmd'),
             Button.url('Channel', url)]
        ]
        textd = f"""
𝗛𝗲𝘆 {event.sender.first_name}
𝗪𝗘𝗟𝗖𝗢𝗠𝗘 𝗧𝗢 『ᏰᏂ』 ⛈

⚠️ 𝗗𝗼 /register 𝗕𝗲𝗳𝗼𝗿𝗲 𝗨𝘀𝗶𝗻𝗴 𝗺𝗲.
"""
        edit = await event.edit(textd, buttons=buttons)
    except Exception as e:
        print(e)

        
        
@client.on(events.NewMessage(pattern='/about'))
async def cmd_start(event):
    try:
        await event.respond("ℹ 𝗔𝗯𝗼𝘂𝘁 : \n**This bot is Maintained and Developed by Team BlackHeads** 👑\n**Use it only for Educational Purposes**, We are not responsible of any illegal things Performed by you.\n     ❛ ━━━━･━━━━･━━━━ ❜")
    except Exception as e:
        print(e)

@client.on(events.NewMessage(pattern='/gate'))
async def cmd_start(event):
    try:
        await event.respond("⚠ 𝗪𝗿𝗼𝗻𝗴 𝗰𝗼𝗺𝗺𝗮𝗻𝗱!\n𝗨𝘀𝗲 `/bh instagram.com` 𝘄𝗶𝘁𝗵𝗼𝘂𝘁 `https://`", reply_to=event)
    except Exception as e:
        print(e)


@client.on(events.NewMessage(pattern='/bh'))
async def report(event):
    global user_credit_file
    user_id = event.sender.id
    global rw
    global tx
    rw = event.raw_text
    tx = event.text
    nu=None        
            
    creditx = credit.get(user_id, 0)
    user_credit_file = f"{user_id}_credit.txt"
    if os.path.exists(user_credit_file):
                with open(user_credit_file, "r") as file:
                    credit_value = int(file.read())
    else:
                credit_value = 0
    if event.text.strip() == "/bh":
        await event.respond("⚠ 𝗪𝗿𝗼𝗻𝗴 𝗰𝗼𝗺𝗺𝗮𝗻𝗱 𝗳𝗼𝗿𝗺𝗮𝘁!\n𝗨𝘀𝗲 `/bh instagram.com` 𝘄𝗶𝘁𝗵𝗼𝘂𝘁 `https://`", reply_to=event)
        return            
    if credit_value <= 0:
        await event.respond('**Credits Finished! Try /refresh** or \nBuy 𝗣𝗿𝗲𝗺𝗶𝘂𝗺 for Unlimited usage 👑.\n𝗦𝗵𝗼𝗽 ➜ [BlackHeads](https://blackheads.mysellix.io/product/gateway-v2)',reply_to=event, parse_mode='MarkdownV2')
    else:
                global edit
                edit = await event.respond('𝗬𝗼𝘂𝗿 𝗥𝗲𝗾𝘂𝗲𝘀𝘁 𝗶𝘀 𝗶𝗻 𝗣𝗿𝗼𝗴𝗿𝗲𝘀𝘀...', reply_to=event)
                global start_time
                start_time = time.time()
                site_checking[user_id] = {"step": 1}
   


@client.on(events.NewMessage(func=lambda event: event.sender_id in site_checking))
async def report_step(event):
    global user_credit_file
    try:
        if '.' in rw:
            user_id = event.sender_id
            url = tx.split(" ")[1]
            w_url = normalize_url(url)
            global domain
            domain = url.split('//')[-1].split('/')[0]
            response = requests.get("http://" +domain)
            html_content = response.text
            captcha = ('captcha' in html_content.lower() or
                       'protected by reCAPTCHA' in html_content.lower() or
                       "I'm not a robot" in html_content.lower() or
                       'Recaptcha' in html_content or
                       "recaptcha/api.js" in html_content)
            cloudflare = ("Cloudflare" in html_content or
                          "cdnjs.cloudflare.com" in html_content or
                          "challenges.cloudflare.com" in html_content)

            website_url = url
            if not website_url.startswith(("http://", "https://")):
                w_url = "http://" + website_url
                payment_gateways = find_payment_gateway(w_url)
                if "Error" in payment_gateways:
                    await event.edit("Provide Valid URL, or Maybe Site issue :)")
                elif "Unknown" in payment_gateways:
                    ch_name = '『ᏰᏂ』'
                    ch_id = 'blackheadsop'
                    ch = f"[{ch_name}](https://t.me/{ch_id})"
                    end_time = time.time()
                    time_taken = end_time - start_time
                    rounded_time_taken = round(time_taken, 2)
                    await edit.edit(f""" ┏━━━━━━━⍟\n┃ 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻 𝗳𝗲𝘁𝗰𝗵𝗲𝗱 ✅\n┗━━━━━━━━━━━━⊛\n 𝗦𝗶𝘁𝗲 -» `{domain}`\n• 𝗚𝗮𝘁𝗲𝘄𝗮𝘆𝘀 ➜ unknown\n━━━━━━━━━━━━━━━\n[◈](https://i.ibb.co/CMcdMjf/Blue-Tosca-Geometric-Technology-Linkedln-Banner.png) 𝐓𝐢𝐦𝐞 𝐓𝐚𝐤𝐞𝐧 : `{rounded_time_taken}``s`\n[◈](https://i.ibb.co/CMcdMjf/Blue-Tosca-Geometric-Technology-Linkedln-Banner.png) 𝐁𝐨𝐭 [𝗚𝗮𝘁𝗲𝘄𝗮𝘆 𝗟𝗼𝗼𝗸𝘂𝗽V2](https://t.me/gatewaylookupv2bot)\n❝ ━━━━・{ch}・━━━━ ❞""")
                else:
                    us_id = event.sender.id
                    if event.sender.id in pre:
                        user = event.sender
                        checked = f"[{user.first_name}](tg://user?id={user.id})"
                        ch_name = '『ᏰᏂ』'
                        ch_id = 'blackheadsop'
                        ch = f"[{ch_name}](https://t.me/{ch_id})"
                        end_time = time.time()
                        time_taken = end_time - start_time
                        rounded_time_taken = round(time_taken, 2)
                        user_id = event.sender_id
                        current_time = datetime.now()
                        if (message_counts[user_id] > 1) and (current_time - last_message_time[user_id] < pre_window):
                                await edit.edit("⚠️ You are sending messages too quickly. Please wait a moment before sending another message.\n📛 𝗧𝗶𝗺𝗲𝗼𝘂𝘁 : `3s`")
                                message_counts[user_id] = 0
                        else:
                            msg=await edit.edit(f""" ┏━━━━━━━⍟\n┃ 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻 𝗳𝗲𝘁𝗰𝗵𝗲𝗱 ✅\n┗━━━━━━━━━━━━⊛\n 𝗦𝗶𝘁𝗲 -» `{domain}`\n• 𝗚𝗮𝘁𝗲𝘄𝗮𝘆𝘀 ➜ {', '.join(payment_gateways)}\n• 𝗦𝗲𝗰𝘂𝗿𝗶𝘁𝘆 ➜ Captcha : {'✅' if captcha else '⛔'}\n        Cloudflare : {'✅' if cloudflare else '⛔'}\n━━━━━━━━━━━━━━━\n[◈](https://i.ibb.co/CMcdMjf/Blue-Tosca-Geometric-Technology-Linkedln-Banner.png) 𝐓𝐢𝐦𝐞 𝐓𝐚𝐤𝐞𝐧 : `{rounded_time_taken}``s`\n[◈](https://i.ibb.co/CMcdMjf/Blue-Tosca-Geometric-Technology-Linkedln-Banner.png) 𝗖𝗵𝗲𝗰𝗸𝗲𝗱 𝗯𝘆 {checked} [𝗣𝗿𝗲𝗺𝗶𝘂𝗺]\n[◈](https://i.ibb.co/CMcdMjf/Blue-Tosca-Geometric-Technology-Linkedln-Banner.png) 𝐁𝐨𝐭 [𝗚𝗮𝘁𝗲𝘄𝗮𝘆 𝗟𝗼𝗼𝗸𝘂𝗽V2](https://t.me/gatewaylookupv2bot)\n❝ ━━━━・{ch}・━━━━ ❞""")
                            await client.send_message(LOG_GROUP_ID,msg)
                            user_id = event.sender.id
                            # Inside the block where you deduct credits
                            credit[user_id] = credit.get(user_id, 0) - 1
                            # Update the file with the new credit value
                            with open(user_credit_file, "w") as file:
                                file.write(str(credit[user_id]))

                    elif event.sender.id in vip:
                        user = event.sender
                        checked = f"[{user.first_name}](tg://user?id={user.id})" if user.username else user.first_name
                        ch_name = '『ᏰᏂ』'
                        ch_id = 'blackheadsop'
                        ch = f"[{ch_name}](https://t.me/{ch_id})"
                        end_time = time.time()
                        time_taken = end_time - start_time
                        rounded_time_taken = round(time_taken, 2)
                        msg=await edit.edit(f""" ┏━━━━━━━⍟\n┃ 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻 𝗳𝗲𝘁𝗰𝗵𝗲𝗱 ✅\n┗━━━━━━━━━━━━⊛\n 𝗦𝗶𝘁𝗲 -» `{domain}`\n• 𝗚𝗮𝘁𝗲𝘄𝗮𝘆𝘀 ➜ {', '.join(payment_gateways)}\n• 𝗦𝗲𝗰𝘂𝗿𝗶𝘁𝘆 ➜ Captcha : {'✅' if captcha else '⛔'}\n        Cloudflare : {'✅' if cloudflare else '⛔'}\n━━━━━━━━━━━━━━━\n[◈](https://i.ibb.co/CMcdMjf/Blue-Tosca-Geometric-Technology-Linkedln-Banner.png) 𝐓𝐢𝐦𝐞 𝐓𝐚𝐤𝐞𝐧 : `{rounded_time_taken}``s`\n[◈](https://i.ibb.co/CMcdMjf/Blue-Tosca-Geometric-Technology-Linkedln-Banner.png) 𝗖𝗵𝗲𝗰𝗸𝗲𝗱 𝗯𝘆 {checked} [𝐕𝗜𝗣 👑]\n[◈](https://i.ibb.co/CMcdMjf/Blue-Tosca-Geometric-Technology-Linkedln-Banner.png) 𝐁𝐨𝐭 [𝗚𝗮𝘁𝗲𝘄𝗮𝘆 𝗟𝗼𝗼𝗸𝘂𝗽V2](https://t.me/gatewaylookupv2bot)\n❝ ━━━━・{ch}・━━━━ ❞""")
                        await client.send_message(LOG_GROUP_ID,msg)
                
                
                    else:
                        user_id = event.sender_id
                        nu=None
                        
                        
                        if credit ==0:
                            await event.respond('**Credits Finished! Try /refresh** or \nBuy 𝗣𝗿𝗲𝗺𝗶𝘂𝗺 for Unlimited usage 👑.\n𝗦𝗵𝗼𝗽 ➜ [BlackHeads](https://blackheads.mysellix.io/product/gateway-v2)', reply_to=event)
                        else:
                            user = event.sender
                            checked = f"[{user.first_name}](tg://user?id={user.id})" if user.username else user.first_name
                            ch_name = '『ᏰᏂ』'
                            ch_id = '-1002017038709'
                            ch = f"[{ch_name}](tg://user?id={ch_id})"
                            user_id = event.sender.id
                            current_time = datetime.now()
                            time_window = timedelta(seconds=25)
                            if (message_counts[user_id] > 1) and (current_time - last_message_time[user_id] < time_window):
                                
                                await edit.edit("⚠️ You are sending messages too quickly. Please wait a moment before sending another message.\n📛 𝗧𝗶𝗺𝗲𝗼𝘂𝘁 : `12s`")
                                
                                time_window = timedelta(seconds=25)
                                message_counts[user_id] = 0
                            else:
                                end_time = time.time()
                                message_counts[user_id] += 1
                                last_message_time[user_id] = current_time
                                time_taken = end_time - start_time
                                rounded_time_taken = round(time_taken, 2)
                                msg = await edit.edit(f""" ┏━━━━━━━⍟\n┃ 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻 𝗳𝗲𝘁𝗰𝗵𝗲𝗱 ✅\n┗━━━━━━━━━━━━⊛\n 𝗦𝗶𝘁𝗲 -» `{domain}`\n• 𝗚𝗮𝘁𝗲𝘄𝗮𝘆𝘀 ➜ {', '.join(payment_gateways)}\n• 𝗦𝗲𝗰𝘂𝗿𝗶𝘁𝘆 ➜ Captcha : {'✅' if captcha else '⛔'}\n        Cloudflare : {'✅' if cloudflare else '⛔'}\n━━━━━━━━━━━━━━━\n[◈](https://i.ibb.co/CMcdMjf/Blue-Tosca-Geometric-Technology-Linkedln-Banner.png) 𝐓𝐢𝐦𝐞 𝐓𝐚𝐤𝐞𝐧 : `{rounded_time_taken}``s`\n[◈](https://i.ibb.co/CMcdMjf/Blue-Tosca-Geometric-Technology-Linkedln-Banner.png) 𝗖𝗵𝗲𝗰𝗸𝗲𝗱 𝗯𝘆 {checked} [𝗙𝗿𝗲𝗲]\n[◈](https://i.ibb.co/CMcdMjf/Blue-Tosca-Geometric-Technology-Linkedln-Banner.png) 𝐁𝐨𝐭 [𝗚𝗮𝘁𝗲𝘄𝗮𝘆 𝗟𝗼𝗼𝗸𝘂𝗽V2](https://t.me/gatewaylookupv2bot)\n❝ ━━━━・{ch}・━━━━ ❞""")
                                await client.send_message(LOG_GROUP_ID,msg)
                                user_id = event.sender.id
                            # Inside the block where you deduct credits
                                credit[user_id] = credit.get(user_id, 0) - 1
                            # Update the file with the new credit value
                                with open(user_credit_file, "w") as file:
                                    file.write(str(credit[user_id]))
                        
        del site_checking[user_id]            
        return
        print('Sending some words > ' + event.text)
       
    except Exception as e:
        print(e)
client.start()
client.run_until_disconnected()
