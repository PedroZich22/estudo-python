from discord.ext import commands, tasks
import datetime

class Dates(commands.Cog):
    """ Work with dates """

    def __init__(self, bot):
        self.bot = bot

    @tasks.loop(hours=1)
    async def current_time(self):
        now =  datetime.datetime.now()
        now = now.strftime("%d/%m/%Y às %H:%M:%S")

        channel = self.bot.get_channel(1111083976736653334)

        await channel.send(f"Data atual: {now}")


async def setup(bot):
    await bot.add_cog(Dates(bot))
