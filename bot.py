import os
from telethon import TelegramClient
from telethon.sessions import StringSession
import asyncio

api_id = int(os.getenv("API_ID", "0"))
api_hash = os.getenv("API_HASH", "API_HASH_HERE")
session_string = os.getenv("SESSION", "1AZWarzUBu24n6ckue23T8na_t7z5nWOWtFA730NIXE2aZsdwgfw5LtWFZP3UK-p7FNukcwZXY5cbMZHuVlRJBbGI2SrjBGkh8UN3B020-07mHPzEBBDvPKrgaCOkrWpXCDGvsw3h5JqPUguOj8GmXFJ_l3ekwBu8j2dQou7LtwkSc8k7aQ1k5V6nSz6L33apSb62cpBa1_Ixye1646MzK-1svz4KyRIiV3GSvTTQ1gGb4x3OmTP25fhBKmdAwct5z3KsCxahcmLNp-si9A-LwVntmgK6ZjNCyXOzLykgdxkwRPm_TRRNikEr12lKX1nNYEFKDXN2yxZcXbs6m1vKYcxxbsSwDxE=")
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

