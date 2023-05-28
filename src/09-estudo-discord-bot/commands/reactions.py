from discord.ext import commands
import discord
from discord import app_commands

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


MY_GUILD = discord.Object(id=1111083976036192400)

class Reactions(commands.Cog):
    """ Work with eactions """
    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if reaction.emoji == "👍":
            role = user.guild.get_role(1111343277220835469)
            await user.add_roles(role)
        elif reaction.emoji == "💩":
            role = user.guild.get_role(1111343347055984771)
            await user.add_roles(role)


async def setup(bot):
    await bot.add_cog(Reactions(bot), guilds=[MY_GUILD])
