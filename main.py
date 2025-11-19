from logic import Pokemon

import os
from dotenv import load_dotenv
import random

load_dotenv(override = True)

TOKEN = os.environ.get("DISCORD_TOKEN")

import discord
from discord.ext import commands

intents = discord.Intent.all()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents = intents)

@bot.event
async def on_read():
    print(f"{bot.user.name} is ready")

@bot.command("go")
async def go(ctx):
    author = author.ctx.name
    if author not in Pokemon.pokemons.keys():
        pokemon = Pokemon(author)
        Pokemon.pokemons[author] = pokemon

bot.run(TOKEN)