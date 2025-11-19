from logic import Pokemon

import os
from dotenv import load_dotenv
import random

load_dotenv(override = True)

TOKEN = os.environ.get("DISCORD_TOKEN")

import discord
from discord.ext import commands

intents = discord.Intents.all()
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
        await pokemon.fetch_stats()
        await pokemon.set_stats()
        await ctx.send(await pokemon.info())
        image_url = await pokemon.show_img()
        if image_url:
            embed = discord.Embed()
            embed.set_image(url=image_url)
            await ctx.send(embed=embed)
        else:
            await ctx.send("Pokémonun görüntüsü yüklenemedi!")
    else:
        await ctx.send("Zaten kendi Pokémonunuzu oluşturdunuz!")

@bot.command("pokebilgi")
async def go(ctx):
    author = ctx.author.name
    if author in Pokemon.pokemons:
        pokemon = Pokemon.pokemons[author]
        await ctx.send(pokemon.info())
    else:
        await ctx.send("Pokemonun yok")

@bot.command()
async def attack(ctx):
    target = ctx.message.mentions[0] if ctx.message.mentions else None
    if target:
        if target.name in Pokemon.pokemons and ctx.author.name in Pokemon.pokemons:
            enemy = Pokemon.pokemons[target.name]
            attacker = Pokemon.pokemons[ctx.author.name]
            result = await attacker.attack(enemy)
            await ctx.send(result)
        else:
            await ctx.send("Savaşmak için her iki katılımcının da Pokemon sahibi olması gerekir!")
    else:
        await ctx.send("Saldırmak istediğiniz kullanıcıyı etiketleyerek belirtin.")

bot.run(TOKEN)
