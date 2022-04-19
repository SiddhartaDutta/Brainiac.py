import os
from dotenv import load_dotenv
load_dotenv()

import discord
intents = discord.Intents.default()
intents.message_content = True
from discord.ext import commands

from Cogs_Test.test_cog import test_cog

Brainiac = commands.Bot(command_prefix=commands.when_mentioned, intents=intents)

@Brainiac.event
async def on_ready():
    print(f'Logged in as {Brainiac.user}!')

@Brainiac.event
async def on_message(message):
    print(f'Message from {message.author}: {message.content}')

Brainiac.add_cog(test_cog(Brainiac))

Brainiac.run(os.getenv('BOT-TOKEN'))