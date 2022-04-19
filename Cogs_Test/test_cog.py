import discord
from discord import app_commands
from discord.ext import commands

class test_cog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="test")
    async def test(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message("test cmd", ephemeral=True)