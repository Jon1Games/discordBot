import os.path

import discord
from discord.ext import commands
import yaml

import createConfig


class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if not os.path.isfile("config/" + str(member.guild.id) + ".yml"):
            await createConfig.createConf(member.guild.id)
        config = yaml.safe_load(open("config/" + str(member.guild.id) + ".yml"))
        if config["WelcomeMessage"]["Enabled"]:
            channel = self.bot.get_channel(config['WelcomeMessage']['ChannelID'])
            embed = discord.Embed(title=config['WelcomeMessage']['Title'],
                                  description=config['WelcomeMessage']['Description'].format(user=member.mention),
                                  color=discord.Color.from_rgb(config['WelcomeMessage']['Color']['Red'],
                                                               config['WelcomeMessage']['Color']['Green'],
                                                               config['WelcomeMessage']['Color']['Blue']))

            embed.set_thumbnail(url=member.avatar)

            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog Welcome loaded")


async def setup(bot):
    await bot.add_cog(Welcome(bot))
