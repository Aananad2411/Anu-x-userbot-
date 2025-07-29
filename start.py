import asyncio
import os
from redis.asyncio import Redis
from pyrogram import Client

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
SESSION_STRING = os.environ.get("SESSION_STRING")
REDIS_URL = os.environ.get("REDIS_URL")
REDIS_PASS = os.environ.get("REDIS_PASS")

app = Client(name="AnuX", api_id=API_ID, api_hash=API_HASH, session_string=SESSION_STRING)
redis = Redis.from_url(REDIS_URL, password=REDIS_PASS, decode_responses=True)

async def check_redis():
    try:
        await redis.set("anu_test", "working")
        pong = await redis.get("anu_test")
        if pong == "working":
            print("✅ Redis connected.")
        else:
            print("❌ Redis test failed.")
    except Exception as e:
        print(f"Redis error: {e}")

async def start_bot():
    await check_redis()
    await app.start()
    print("✨ Anu X Userbot Started")
    await idle()
    await app.stop()

if __name__ == "__main__":
    asyncio.run(start_bot())
