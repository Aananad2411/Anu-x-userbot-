import aiohttp
import os
from telethon import events

def register(bot):
    @bot.on(events.NewMessage(pattern=r"\.install (.+)"))
    async def install_plugin(event):
        url = event.pattern_match.group(1)
        if not url.endswith(".py"):
            return await event.reply("❌ Please provide a valid `.py` file URL.")

        plugin_name = url.split("/")[-1]
        path = f"plugins/{plugin_name}"

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    if resp.status == 200:
                        content = await resp.text()
                        with open(path, "w") as f:
                            f.write(content)
                        from core.loader import load_plugins
                        load_plugins(bot)
                        await event.reply(f"✅ Installed and loaded `{plugin_name}`.")
                    else:
                        await event.reply("❌ Failed to download the plugin.")
        except Exception as e:
            await event.reply(f"❌ Error: {e}")
