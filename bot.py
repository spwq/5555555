import os
from telethon import TelegramClient
from telethon.sessions import StringSession
import asyncio

api_id = int(os.getenv("API_ID", "0"))
api_hash = os.getenv("API_HASH", "API_HASH_HERE")
session_string = os.getenv("SESSION", "1AZWarzUBu3Z0d464gS18oNceuOOlkhlk1vzriNa2YM5ysEswEgu01cGjA4Utz-0A7M_PLunnyfJJuG1aACJeyyanEAHRk_NWMLpAWvp93ouLdQjsD5MWMY3XHy8RLCXVmP91iRZMPRkOGDRDwyQWJCFJx43MiLVzRc1nhPTHQFZe4EJipqi9oq1kz-4K9I1HWOqqkWp4X7q47EqgmyESPz_JoHfHLCv3-OAikHlGJN0h75OzNs2ngMDPtDofXpaK2LeGMZ05wCxhNS5bpKjsKoKdz6TXzZqTUZ6C32Zso1kBjDAGJ23j_vkk2-bhkgb1jL_0Eyxk7hmDObnHLCHDCo0jhBX4hL8=")
group_link = os.getenv("GROUP_LINK", "")

if not api_id or not api_hash or not session_string or not group_link:
    print("⚠️ المتغيرات غير مكتملة، تأكد من إضافتها في الموقع")
else:
    client = TelegramClient(
        StringSession(session_string),
        api_id,
        api_hash
    )

    sent_ids = set()

    async def main():
        await client.start()
        print("✅ تم تسجيل الدخول")

        saved = await client.get_entity("me")
        group = await client.get_entity(group_link)

        print("🚀 بدأ نقل الفيديوهات...")

        while True:
            try:
                async for msg in client.iter_messages(saved, reverse=True):
                    if not msg.video:
                        continue
                    if msg.id in sent_ids:
                        continue

                    await client.send_file(group, msg.video, caption=msg.text or "")
                    sent_ids.add(msg.id)

                    await asyncio.sleep(10)

                await asyncio.sleep(30)

            except Exception as e:
                print(f"⚠️ خطأ: {e}")
                await asyncio.sleep(15)

    client.loop.run_until_complete(main())
