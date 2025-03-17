import discord
from discord.ext import commands
import os
import json
from games import *

# Load configuration settings
with open('config.json') as f:
    config = json.load(f)

# Create a new bot instance
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix=config['prefix'], intents=intents)

# Event to indicate the bot is ready
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

# Command to start a game
@bot.command(name='start')
async def start_game(ctx, game_name: str):
    # Check if the game exists
    if game_name not in games:
        await ctx.send(f'Game {game_name} does not exist.')
        return

    # Check if the user has the required permission
    if not ctx.author.guild_permissions.manage_events:
        await ctx.send('You do not have the required permission to start this game.')
        return

    # Start the game
    game = games[game_name](ctx)
    await game.start()

# Command to join a game
@bot.command(name='join')
async def join_game(ctx, game_name: str):
    # Check if the game exists
    if game_name not in games:
        await ctx.send(f'Game {game_name} does not exist.')
        return

    # Check if the user has the required permission
    if not ctx.author.guild_permissions.manage_events:
        await ctx.send('You do not have the required permission to join this game.')
        return

    # Join the game
    game = games[game_name](ctx)
    await game.join()

# Command to leave a game
@bot.command(name='leave')
async def leave_game(ctx, game_name: str):
    # Check if the game exists
    if game_name not in games:
        await ctx.send(f'Game {game_name} does not exist.')
        return

    # Check if the user has the required permission
    if not ctx.author.guild_permissions.manage_events:
        await ctx.send('You do not have the required permission to leave this game.')
        return

    # Leave the game
    game = games[game_name](ctx)
    await game.leave()

# Run the bot
bot.run(config['token'])
