from discord.ext import commands
import discord
from discord import app_commands

MY_GUILD = discord.Object(id=1111083976036192400)

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
class Talks(commands.Cog):
    """ Talks with user """

    def __init__(self, bot):
        self.bot = bot

    # !oi
    @app_commands.command(name="oi", description="Envia um Oi(Não erquer argumentos)")
    async def send_hello(self, interaction: discord.Interaction):
        name = interaction.user.name

        response = f"Olá, {name}"

        await interaction.response.send_message(response)

    # !segredo
    @commands.command(name="segredo", help="Envia um segredo no privado. (Não requer argumentos)")
    async def secret(self, ctx):
        try:
            await ctx.author.send("Oi")
        except discord.errors.Forbidden:
            await ctx.send("Não posso te contar o segredo, habilite receber mensagens de qualquer pessoa do servidor (Opções > Privacidade)")


async def setup(bot):
    await bot.add_cog(Talks(bot), guilds=[MY_GUILD])
