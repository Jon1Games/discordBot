import discord
from discord.ext import commands
from discord import app_commands
from cogs.TemporaryVoiceChannel import TempVoiceButtons


class Setup(commands.Cog):
    def __int__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog Setup loaded")


    @app_commands.command()
    async def setupvoice(self, interaction: discord.Interaction):
        view = TempVoiceButtons()
        await interaction.response.send_message("Settings", view=view)



async def setup(bot):
    await bot.add_cog(Setup(bot))
