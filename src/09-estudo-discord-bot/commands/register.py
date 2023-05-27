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
            async def verify_data(dados):
                    checar = open("src/09-estudo-discord-bot/alunos.txt", "r", encoding='UTF-8')
                    if dados not in checar.readlines():
                        arquivo.write(dados + "\n")
                    else:
                        await ctx.send("Prontuário ou email já utilizado por outro aluno!")
                    checar.close()


            with open("src/09-estudo-discord-bot/alunos.txt", "a", encoding='UTF-8') as arquivo:
                verify_data(dados)
            await ctx.send("O aluno foi registrado!")

        except Exception as error:
            print(error)
            await ctx.send("O aluno não foi registrado! Revise os argumentos em !help")


    @commands.command(name="listar-alunos", help="Registra um aluno no aluno.txt.")
    async def list_student(self, ctx):

        with open("src/09-estudo-discord-bot/alunos.txt", "r", encoding='UTF-8') as arquivo:
        
            embed = discord.Embed(
                title="Resultado da busca pelos alunos registrados",
                description="Alunos registrados pelo comando !registrar ",
                color=0x00FFFF,
            )
            
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar)
            embed.set_footer(text="Feito por " + self.bot.user.name, icon_url=self.bot.user.avatar)

            for dados in arquivo.readlines():
                aluno = dados.split(",")
                lista = ['prontuario', 'nome', 'email']
                dicionario = {}
                for index, value in enumerate(lista):
                    dicionario[value.strip()] = aluno[index].strip()
                
                embed.add_field(
                    name=f"Dados do Aluno {dicionario['nome']}:", 
                    value=f"Prontuário: {dicionario['prontuario']},\n Nome: {dicionario['nome']}, \n Email: {dicionario['email']}"
                )
                print(dicionario)

        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Register(bot))
