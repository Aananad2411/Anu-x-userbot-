import asyncio
import os
from telethon import TelegramClient, events
import aioredis

from core.loader import load_plugins

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION = os.getenv("SESSION", "anu_x_userbot")

REDIS_URL = os.getenv("REDIS_URL")
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")

bot = TelegramClient(SESSION, API_ID, API_HASH)
bot.redis = None

async def setup_redis():
    if REDIS_URL:
        bot.redis = await aioredis.from_url(
            REDIS_URL,
            password=REDIS_PASSWORD,
            decode_responses=True
        )
        print("✅ Redis connected")
    else:
        print("⚠️ Redis not configured")

async def main():
    await bot.start()
    await setup_redis()
    load_plugins(bot)
    print("🚀 Anu X Userbot is up and running!")
    await bot.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
