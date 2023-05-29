import discord
from discord import app_commands, ui
from discord.ext import commands
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, Spacer, TableStyle
from reportlab.lib.styles import getSampleStyleSheet


MY_GUILD = discord.Object(id=1111083976036192400)

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


class Register(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="modal", description="registrar aluno via modal")
    async def modal(self, interaction: discord.Interaction):
        await interaction.response.send_modal(modal_cadastro())

    @app_commands.command(name="listar-alunos", description="Registra um aluno no aluno.txt.")
    async def list_student(self, interaction: discord.Interaction, tipo: str = None):

        if tipo == 'pdf':
            await lista_pdf(interaction)
            await get_students("src/09-estudo-discord-bot/alunos.txt")
        else:
            await lista_embed(interaction, self.bot)
        

async def get_students(caminho):
    with open(caminho, "r", encoding='UTF-8') as arquivo:
        linhas = []

        for linha in arquivo:
            dados = linha.split(",")
            linhas.append(dados)

    return linhas


async def lista_embed(interaction, bot):
    try:
        embed = discord.Embed(
                title="Resultado da busca pelos alunos registrados",
                description="Alunos registrados pelo comando !registrar ",
                color=0x00FFFF,
            )

        embed.set_author(name=bot.user.name, icon_url=bot.user.avatar)
        embed.set_footer(text="Feito por " + bot.user.name, icon_url=bot.user.avatar)

        dados = await get_students("src/09-estudo-discord-bot/alunos.txt")
        for dado in dados:
            embed.add_field(
                name=f"Dados do Aluno {dado[1]}:",
                value=f"Prontuário: {dado[0]},\n Nome: {dado[1]}, \n Email: {dado[2]}",
                inline=False
            )

        await interaction.response.send_message(embed=embed)
    except discord.Forbidden:
        await interaction.response.send_message()


async def lista_pdf(interaction):
    try:
        dados = await get_students("src/09-estudo-discord-bot/alunos.txt")

        nome_pdf = "alunos_cadastrados.pdf"
        doc = SimpleDocTemplate(nome_pdf, pagesize=letter)

        styles = getSampleStyleSheet()
        conteudo = []

        titulo = Paragraph("Alunos cadastrados", style=styles["Heading1"])
        conteudo.append(titulo)

        conteudo.append(Spacer(1, 30))

        header = ["Prontuario", "Nome", "Email"]
        dados.insert(0, header)

        estiloTabela = TableStyle([
            ("BACKGROUND", (0,0), (2,0), "black"),
            ("TEXTCOLOR", (0,0), (2,0), "white"),
            ("GRID", (0,0), (-1,-1), 1, "black"),
            ("FONTSIZE", (0, 0), (-1, -1), 12),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE")
        ])

        tabela = Table(dados, colWidths="33%", rowHeights=30)
        tabela.setStyle(estiloTabela)
        conteudo.append(tabela)
        conteudo.append(Spacer(1, 20))

        numero_de_alunos = Paragraph(f"<b>Total de alunos: </b>{len(dados) - 1}")
        conteudo.append(numero_de_alunos)

        doc.build(conteudo)

    except Exception as e:
        print(e)

class modal_cadastro(ui.Modal, title="Registrar aluno"):
        prontuario = ui.TextInput(label="Entre com o prontuário", style=discord.TextStyle.short)
        nome = ui.TextInput(label="Entre com o nome", style=discord.TextStyle.short)
        email = ui.TextInput(label="Entre com o email", style=discord.TextStyle.short)

        async def on_submit(self, interaction: discord.Interaction):
            dados = f"{self.prontuario.value},{self.nome.value},{self.email.value}"
            try:
                async def salvar(dados):
                    with open("src/09-estudo-discord-bot/alunos.txt", "a", encoding='UTF-8') as arquivo:
                        arquivo.write(dados+"\n")
                        await interaction.response.send_message("O aluno foi registrado!")

                with open("src/09-estudo-discord-bot/alunos.txt", "r", encoding='UTF-8') as checar:
                    chama = checar.read()
                        
                    if self.prontuario.value in chama or self.email.value in chama:
                        await interaction.response.send_message("Prontuário ou email já utilizado por outro aluno!")
                    else:
                        await salvar(dados)

            except Exception as error:
                print(error)
                await interaction.response.send_message("O aluno não foi registrado! Revise os argumentos em !help")


async def setup(bot):
    await bot.add_cog(Register(bot), guilds=[MY_GUILD])
