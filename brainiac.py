import os
from dotenv import load_dotenv
load_dotenv()

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

class MyBot(commands.Bot):
    
    def __init__(self):
        super().__init__(command_prefix = commands.when_mentioned, intents = intents, application_id = os.getenv('APP-ID'))

    async def setup_hook(self):

        for filename in os.listdir('./cogs'):
            if filename.endswith('.py') and not (filename == '__init__.py'):
                await self.load_extension(f'cogs.{filename[:-3]}')
                print(filename)
        
        await test.tree.sync(guild = discord.Object(id = os.getenv('GUILD-TOKEN')))

    async def on_ready(self):
        print(f'{self.user} has connected to Discord.')

test = MyBot()
test.run(os.getenv('BOT-TOKEN'))

# test = commands.Bot(command_prefix=commands.when_mentioned, intents=intents)

# async def load_cogs():

#     for filename in os.listdir('./Cogs_Test'):
#         if filename.endswith('.py') and not (filename == '__init__.py'):
#             test.load_extension(f'Cogs.{filename[:-3]}')
#             print(filename)

# @test.event
# async def on_ready():
#     print(f'Logged in as {test.user}!')
#     print('''Loading Cogs:---''')
#     await load_cogs()

# @test.event
# async def on_message(message):
#     print(f'Message from {message.author}: {message.content}')

# #await test.add_cog(test_cog(test))


# test.run(os.getenv('BOT-TOKEN'))