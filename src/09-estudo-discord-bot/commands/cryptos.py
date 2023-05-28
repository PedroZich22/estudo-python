import requests
import discord
from discord.ext import commands
from discord import app_commands


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

MY_GUILD = discord.Object(id=1111083976036192400)

class Crypto(commands.Cog):
    """ Works with crypto """
    
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(description="Veifica o preço de um par na Binance. Argumentos: moeda base")
    async def binance(self, interaction: discord.Interaction, coin:str, base:str):
        try:
            response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}{base.upper()}")

            data = response.json()
            price = data.get("price")

            if price:
                await interaction.response.send_message(f"O valor do par {coin}/{base} é: {price}")
            else:
                await interaction.response.send_message(f"O par {coin}/{base} é inválido")
        except Exception as error:
            await interaction.response.send_message("Ops... Deu algum erro!")
            print(error)


async def setup(bot):
    await bot.add_cog(Crypto(bot), guilds=[MY_GUILD])
