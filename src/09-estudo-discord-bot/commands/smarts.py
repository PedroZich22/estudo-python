import discord
from discord.ext import commands
from discord import app_commands

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

MY_GUILD = discord.Object(id=1111083976036192400)

class Smarts(commands.Cog):
    """ A lot of Samrt Commands """
    
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name="calcular", description="Calcular uma expressão. Argumentos: expressão")
    async def calculate_expression(self, interaction: discord.Interaction, expression:str):
        response = eval(expression)

        await interaction.response.send_message(f"A resposta é: {response}")


async def setup(bot):
    await bot.add_cog(Smarts(bot), guilds=[MY_GUILD])
