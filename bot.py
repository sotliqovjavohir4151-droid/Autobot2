from telethon import TelegramClient
import asyncio

api_id = 39671684
api_hash = "442196ac66c2e4100b61a31a0dff4eab"

client = TelegramClient("session2", api_id, api_hash)

groups = [
"https://t.me/Xorazmtelefon_bozori_N1",
"https://t.me/buxoro_telefon_bozori_bukhara",
"https://t.me/Andijon_Fargona_Namangan7",
"https://t.me/BUXORO_TELEFON_BOZORI_3",
"https://t.me/Qarshi_telefon_bozori",
"https://t.me/telfon_bozori_qarshi",
"https://t.me/Qarshi_Telefon_Bozori1",
"https://t.me/Qarshi_Telefon_bozor_Qashqadaryo",
"https://t.me/qarshi_telefon_qashqadaryo_bozor",
"https://t.me/gulobod_navoi_chat",
"https://t.me/Qarshi_telefon_bozorin1",
"https://t.me/fargona_margilon_telefon_bozorN1",
"https://t.me/Guruppalar_qiziqarli",
"https://t.me/Tanishuv_Dostlarr_Sevishganlar",
"https://t.me/mehribonlariiiim_0277",
"https://t.me/notkrug_chat",
"https://t.me/xorazm_telefon_bozor_group",
"https://t.me/dil_tabriklari",
"https://t.me/Navoiy_telefonn_bozor"
]

message = """
• Bizga Kuniga 10 Tadan 1000 Tagacha Ovoz Yeg'a Oladiganlar Kerak

• Ovozlarni Maximal Darajada Qimmat Olishga Harakat Qilamiz

• Bizning Jamoaga Qo'shiling

Narxlar kundan kunga ko'tarilib boradi.
Eng baland va ishonchli kanal.

Isbotlar profilda
"""

bad_groups = []

async def main():
    await client.start()
    print("Bot ishga tushdi")

    while True:
        for g in groups:
            if g in bad_groups:
                continue

            try:
                await client.send_message(g, message)
                print("Yuborildi:", g)
                await asyncio.sleep(5)

            except Exception as e:
                print("Yuborilmadi:", g)
                print("Sabab:", e)
                bad_groups.append(g)

        print("10 minut kutyapti...")
        await asyncio.sleep(450)

asyncio.run(main())
