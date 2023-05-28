import discord
from discord.ext import commands
from discord import app_commands

MY_GUILD = discord.Object(id=1111083976036192400)

class Images(commands.Cog):
    """ Works with images """
    
    def __init__(self, bot):
        self.bot = bot
    
        
    @app_commands.command(name="foto", description="Gera uma foto aleatória. (Não requer argumentos)")
    async def get_random_image(self, interaction: discord.Interaction):
        url_image = "https://picsum.photos/1920/1080"

        embed = discord.Embed(
            title="Resultado da busca de imagem",
            description="PS: A busca é totalmente aleatória",
            color=0x00FFFF,
        )

        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar)
        embed.set_footer(text="Feito por " + self.bot.user.name, icon_url=self.bot.user.avatar)
        embed.add_field(name="API", value="Usamos a API do https://picsum.photos")
        embed.add_field(name="Parâmetros", value="{largua}/{altura}")
        embed.add_field(name="Exemplo", value=url_image, inline=False)
        embed.set_image(url=url_image)

        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(Images(bot), guilds=[MY_GUILD])
