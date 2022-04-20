from urllib import response
import discord
from discord import app_commands
from discord.ext import commands

class test(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="hello", description="test desc")
    async def hello(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message("test cmd wasd")

    @app_commands.command(name="another", description="cmd")
    async def another(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message("testing 2nd cmd")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(test(bot))