import discord
from discord.ext import commands

class Mycog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot



@commands.command()
if message.content.startswith("Neighbor"):
    mid = User.id('142872588207521792').format(message)
        await client.send_message(message.channel, '{mid} mentioned')

def setup(bot):
    bot.add_cog(Mycog(bot))