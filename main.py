import asyncio
import discord
from discord.ext import commands

import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.members = True
intents.voice_states = True

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or(),
    intents=intents,
    activity=discord.Activity(type=discord.ActivityType.playing, name='mit dem code'),
    status=discord.Status.online,
    sync_commands=True,
    delete_not_existing_commands=True
)


async def load():
    await bot.load_extension("cogs.Welcome")


async def main():
    print("Initialise bot...")
    print("Loading cogs...")
    await load()
    print("Start bot...")
    await bot.start(os.getenv("TEST_BOT_TOKEN"))


asyncio.run(main())
