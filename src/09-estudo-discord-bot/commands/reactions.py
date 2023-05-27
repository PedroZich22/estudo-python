from discord.ext import commands

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
    await bot.add_cog(Reactions(bot))
