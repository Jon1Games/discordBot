from discord.ext import commands


class AdminCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="first_slash")
    async def first_slash(self, ctx):
        await ctx.respond("You executed the slash command!")

    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog AdminCommand loaded")


async def setup(bot):
    await bot.add_cog(AdminCommand(bot))
