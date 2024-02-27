import os.path

import discord
from discord.ext import commands
import yaml

import createConfig


class JoinRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if not os.path.isfile("config/" + str(member.guild.id) + ".yml"):
            await createConfig.createConf(member.guild.id)
        config = yaml.safe_load(open("config/" + str(member.guild.id) + ".yml"))
        if config["AutoRole"]["Enabled"]:
            role = discord.utils.get(member.guild.roles, name=str(config['AutoRole']['RoleName']))
            await member.add_roles(role)

    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog JoinRole loaded")


async def setup(bot):
    await bot.add_cog(JoinRole(bot))
