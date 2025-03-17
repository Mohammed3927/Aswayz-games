import discord
from discord.ext import commands
import asyncio

class Roulette(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.players = []
        self.min_players = 2
        self.max_players = 5

    @commands.command(name="روليت")
    async def start_roulette(self, ctx):
        if ctx.channel.id not in config.GAME_CHANNELS:
            return await ctx.send("🚫 لا يمكنك تشغيل اللعبة هنا!")

        embed = discord.Embed(title="🎡 لعبة الروليت", description="اضغط زر `✅ دخول` للمشاركة!", color=discord.Color.blue())
        join_button = discord.ui.Button(label="✅ دخول", style=discord.ButtonStyle.green)
        leave_button = discord.ui.Button(label="❌ خروج", style=discord.ButtonStyle.red)

        async def join_callback(interaction):
            if interaction.user not in self.players:
                self.players.append(interaction.user)
                await interaction.response.send_message(f"{interaction.user.mention} انضم للعبة!", ephemeral=True)

        async def leave_callback(interaction):
            if interaction.user in self.players:
                self.players.remove(interaction.user)
                await interaction.response.send_message(f"{interaction.user.mention} خرج من اللعبة!", ephemeral=True)

        join_button.callback = join_callback
        leave_button.callback = leave_callback

        view = discord.ui.View()
        view.add_item(join_button)
        view.add_item(leave_button)

        message = await ctx.send(embed=embed, view=view)

        await asyncio.sleep(30)  # وقت بدء اللعبة

        if len(self.players) < self.min_players:
            return await ctx.send("🚫 لم يصل عدد اللاعبين للحد الأدنى!")

        await ctx.send("🎲 اللعبة بدأت!")

def setup(bot):
    bot.add_cog(Roulette(bot))
