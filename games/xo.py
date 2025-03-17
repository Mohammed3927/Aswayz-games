import discord
from discord.ext import commands

class XO(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="xo")
    async def start_xo(self, ctx):
        await ctx.send("🎮 لعبة XO قيد التطوير 🚧")

def setup(bot):
    bot.add_cog(XO(bot))
