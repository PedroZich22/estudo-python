from discord.ext import commands

class Smarts(commands.Cog):
    """ A lot of Samrt Commands """
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="calcular", help="Calcular uma expressão. Argumentos: expressão")
    async def calculate_expression(self, ctx, *expression):
        expression = ''.join(expression)
        response = eval(expression)

        await ctx.send(f"A resposta é: {response}")


async def setup(bot):
    await bot.add_cog(Smarts(bot))
