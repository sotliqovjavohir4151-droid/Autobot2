from telethon import TelegramClient
import asyncio

api_id = 35158970
api_hash = "7bfec4703a3d652c7becf1e72cdb2d07"

client = TelegramClient('session', api_id, api_hash)

groups = [
    'https://t.me/open_budjet_uz_jamoasi',
    'https://t.me/Navoiy_telefonn_bozor'
]

async def main():
    while True:
        for g in groups:
            await client.send_message(g, "Salom")
        await asyncio.sleep(300)

with client:
    client.loop.run_until_complete(main())
