import discord
from discord.ext import commands
import config

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=config.PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f"Bot {bot.user} is now running!")
    for filename in os.listdir("./games"):
        if filename.endswith(".py"):
            bot.load_extension(f"games.{filename[:-3]}")

bot.run(config.BOT_TOKEN)
