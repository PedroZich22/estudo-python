import discord
from discord import app_commands
from discord import ui
from register import Register
MY_GUILD = discord.Object(id=1111083976036192400)

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

register = Register()

class MyModal(ui.Modal, title="Registrar aluno"):
    prontuario = ui.TextInput(label="Entre com o prontuário", placeholder="SP0000", style=discord.TextStyle.short)
    name = ui.TextInput(label="Entre com o nome", placeholder="Pedro Zich", style=discord.TextStyle.short)
    email = ui.TextInput(label="Entre com o email", placeholder="pedro@email.com", style=discord.TextStyle.short)

    async def on_submit(self, interaction: discord.Interaction, prontuario, name, email):
        await register.register_student(self, prontuario, name, email)


@app_commands.command(name="modal", description="registrar aluno via modal")
async def modal(interaction: discord.Interaction):
    await interaction.response.send_message(MyModal())

async def setup(bot):
    await bot.add_cog()
