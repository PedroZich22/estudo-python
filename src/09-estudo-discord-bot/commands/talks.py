from discord.ext import commands
import discord

class Talks(commands.Cog):
    """ Talks with user """

    def __init__(self, bot):
        self.bot = bot
    
    # !oi
    @commands.command(name="oi", help="Envia um Oi(Não erquer argumentos)")
    async def send_hello(self, ctx):
        name = ctx.author.name

        response = f"Olá, {name}"

        await ctx.send(response)

    # !segredo
    @commands.command(name="segredo", help="Envia um segredo no privado. (Não requer argumentos)")
    async def secret(self, ctx):
        try:
            await ctx.author.send("Oi")
            await ctx.author.send("Ola")
            await ctx.author.send("Oi oi")
        except discord.errors.Forbidden:
            await ctx.send("Não posso te contar o segredo, habilite receber mnsagens de qualquer pessoa do servidor (Opções > Privacidade)")


async def setup(bot):
    await bot.add_cog(Talks(bot))
