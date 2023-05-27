import discord
from discord.ext import commands

class Register(commands.Cog):
    """ A lot of Samrt Commands """
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="registrar", help="Registra um aluno no aluno.txt.")
    async def register_student(self, ctx, *expression):
        dados = ','.join(expression)
        try:
            with open("src/09-estudo-discord-bot/alunos.txt", "a", encoding='UTF-8') as arquivo:
                checar = open("src/09-estudo-discord-bot/alunos.txt", "r", encoding='UTF-8')
                if (dados[0] or dados[3] not in checar):
                    arquivo.writelines(dados,"\n")
                checar.close()
            await ctx.send("O aluno foi registrado!")

        except Exception as e:
            print(e)

            await ctx.send("O aluno não foi registrado! Revise os argumentos em !help")


    @commands.command(name="listar-alunos", help="Registra um aluno no aluno.txt.")
    async def list_student(self, ctx):

        with open("src/09-estudo-discord-bot/alunos.txt", "r", encoding='UTF-8') as arquivo:
            alunos = arquivo.read()
        
            embed = discord.Embed(
                title="Resultado da busca de imagem",
                description="PS: A busca é totalmente aleatória",
                color=0x00FFFF,
            )

            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar)
            embed.set_footer(text="Feito por " + self.bot.user.name, icon_url=self.bot.user.avatar)
            for aluno in alunos:
                embed.add_field(name="Alunos registrados: ", value=f"{aluno}")

        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Register(bot))
