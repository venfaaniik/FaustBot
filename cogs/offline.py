import discord
from discord.ext import commands

from discord.ext.commands.bot import Bot

class Offline(commands.Cog):
    '''Offline status'''

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        print(before.status + " || " + before.id)
        if str(before.status) == "online":
            if (str(after.status) == "offline"):
                print("soemthing changed")
                if (str(after.id) == "128440902468370432"):
                    print("void went offline")
                    await self.bot.change_presence(status=discord.Status.offline)
                    #await Bot.close()

        #shouldnt even workkkk
        elif str(before.status) == "offline":
            if (str(after.status) == "online"):
                print("something changed")
                if (str(after.id) == "128440902468370432"):
                    await self.bot.change_presence(status=discord.Status.online)
                    print ("void went online")
                    #await Bot.connect()


def setup(bot):
    bot.add_cog(Offline(bot))