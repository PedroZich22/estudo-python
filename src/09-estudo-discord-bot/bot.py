from decouple import config
import sys
sys.path.append("C:\\Users\\pedro\\OneDrive\\Área de Trabalho\\estudo-python\\src\\09-estudo-discord-bot\\commands")
import os
import discord
from discord import ui, app_commands
from discord.ext import commands

MY_GUILD = discord.Object(id=1111083976036192400)

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

bot = commands.Bot(intents=intents, command_prefix="!")

@bot.event
async def on_ready():
    print(f"Estou pronto! Estou conectado como {bot.user}")
    await load_cogs(bot)

    synced = await bot.tree.sync(guild=MY_GUILD)
    print(f"Synced {len(synced)} command(s)")

    await bot.get_cog('Dates').current_time.start()


async def load_cogs(a):
    for file in os.listdir("src/09-estudo-discord-bot/commands"):
        if file.endswith(".py"):
            cog = file[:-3]
            await bot.load_extension(f"commands.{cog}")

    await a.load_extension("manager")
    await a.load_extension("tasks.dates")


TOKEN = config("TOKEN")
bot.run(TOKEN)
