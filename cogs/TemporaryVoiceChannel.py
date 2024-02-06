import discord
import yaml
from discord.ext import commands
import os
import createConfig


class TemporaryVoice(commands.Cog):
    temporary_channels = []

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog TempVoice loaded")

    @commands.Cog.listener()
    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState,
                                    after: discord.VoiceState):
        if not os.path.isfile("config/" + str(member.guild.id) + ".yml"):
            await createConfig.createConf(member.guild.id)
        config = yaml.safe_load(open("config/" + str(member.guild.id) + ".yml"))
        if config["TemporaryVoice"]["Enabled"]:
            possible_channel_name = config["TemporaryVoice"]["CreateChannelName"].format(user=member.name)
            if after.channel:
                if after.channel.id == config["TemporaryVoice"]["ChannelID"]:
                    temp_channel = await after.channel.clone(name=possible_channel_name)
                    await member.move_to(temp_channel)
                    self.temporary_channels.append(temp_channel.id)

            if before.channel:
                if before.channel.id in self.temporary_channels:
                    if len(before.channel.members) == 0:
                        await before.channel.delete()
                        self.temporary_channels.remove(before.channel.id)


async def setup(bot):
    await bot.add_cog(TemporaryVoice(bot))
