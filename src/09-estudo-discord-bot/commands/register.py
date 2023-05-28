import discord
from discord import app_commands, ui
from discord.ext import commands
MY_GUILD = discord.Object(id=1111083976036192400)

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

class MyModal(ui.Modal, title="Registrar aluno"):
        prontuario = ui.TextInput(label="Entre com o prontuário", placeholder="SP0000", style=discord.TextStyle.short)
        nome = ui.TextInput(label="Entre com o nome", placeholder="Pedro Zich", style=discord.TextStyle.short)
        email = ui.TextInput(label="Entre com o email", placeholder="pedro@email.com", style=discord.TextStyle.short)

        async def on_submit(self, interaction: discord.Interaction):
            dados = f"{self.prontuario.value},{self.nome.value},{self.email.value}"
            try:
                async def salvar(dados):
                    with open("src/09-estudo-discord-bot/alunos.txt", "a", encoding='UTF-8') as arquivo:
                        arquivo.write(dados+"\n")
                        await interaction.response.send_message("O aluno foi registrado!")

                with open("src/09-estudo-discord-bot/alunos.txt", "r", encoding='UTF-8') as checar:
                    chama = checar.read()

                # chama = chama.split(',')

                if self.prontuario.value in chama or self.email.value in chama:
                    await interaction.response.send_message("Prontuário ou email já utilizado por outro aluno!")
                else:
                    await salvar(dados)

            except Exception as error:
                print(error)
                await interaction.response.send_message("O aluno não foi registrado! Revise os argumentos em !help")


class Register(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # @app_commands.command(name="registrar", description="Registra um aluno no aluno.txt.")
    # async def register_student(self, interaction: discord.Interaction, prontuario:str, nome:str, email:str):
    #     dados = f"{prontuario},{nome},{email}"
    #     try:
    #         async def salvar(dados):
    #             with open("src/09-estudo-discord-bot/alunos.txt", "a", encoding='UTF-8') as arquivo:
    #                 arquivo.write(dados+"\n")
    #                 await interaction.response.send_message("O aluno foi registrado!")

    #         with open("src/09-estudo-discord-bot/alunos.txt", "r", encoding='UTF-8') as checar:
    #             chama = checar.read()

    #         # chama = chama.split(',')

    #         if prontuario in chama or email in chama:
    #             await interaction.response.send_message("Prontuário ou email já utilizado por outro aluno!")
    #         else:
    #             await salvar(dados)

    #     except Exception as error:
    #         print(error)
    #         await interaction.response.send_message("O aluno não foi registrado! Revise os argumentos em !help")


    @app_commands.command(name="modal", description="registrar aluno via modal")
    async def modal(self, interaction: discord.Interaction):
        await interaction.response.send_modal(MyModal())


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
    await bot.add_cog(Register(bot), guilds=[MY_GUILD])
