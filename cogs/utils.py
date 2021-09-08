import discord
from discord.ext import commands

class Utils(commands.Cog):
    '''An utility function class for everything'''

    def __init__(self, bot):
        self.bot = bot
        

    # async def shutupTimer():
    #     global shutup
    #     timer = 60
    #     print("Shutting up for " + str(timer) + " seconds")
    #     await asyncio.sleep(timer) #Sleep for x before updating
    #     print("No longer silenced")
    #     shutup = False
    #     return

    @commands.command(hidden=True) # this is for making a command
    async def ping(self, ctx):
    	await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms')

    #await bot.wait_until_ready()
        # while not self.bot.is_closed:
            #global wagons
            #global is_human
            #global una

            # guild = self.bot.get_guild(458318646108749824)
            #wagons = random.randint(1, 3)

            # while True:
                #wagons += random.randint(1,10)
                # randMsg = random.randint(2, 6)
                # user = choice(guild.members)

                # if randMsg == 1:
                #     await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= str(wagons) + " wagons levitating."))
                # if randMsg == 2:
                #     await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name = "his own beautiful voice."))
                # elif randMsg == 3:
                #     await self.bot.change_presence(activity=discord.Game(name="with fire."))
                # elif randMsg == 4:
                #     winning = random.randint(0, 500)
                #     if (winning == 0):
                #         await self.bot.change_presence(activity=discord.Game(name="Gwent again and winning."))
                #     else:
                #         await self.bot.change_presence(activity=discord.Game(name="Gwent again and losing."))
                # elif randMsg == 5:
                #     await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= "{}".format(user.display_name)))
                # elif randMsg == 6:
                #     await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= "{}".format(user.display_name) +  " from afar ( ͡◉ ͜ʖ ͡◉)"))
                # elif randMsg == 7:
                #     await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= "{}".format(user.display_name) + " levitating."))
                # elif randMsg == 8:
                #     await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= "ALL THE " + str(wagons) + " WAGONS CRASHING TOWARDS THE GROUND."))
                # elif randMsg == 9:
                #     await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name = "the silence of " + str(int(casualties)) + " dead bodies."))
                # else:
                #     print("randmsg = " + str(randMsg) + ", it gave an error")


                # await asyncio.sleep(120) #Sleep for x before updating
                
                # if randMsg == 8:
                #     if una == False:               
                #         is_human = False
                #         await w(wagons)
                #         is_human = True
                #     wagons = 0
                #     una = False

def get_time_string(self, seconds):
        hours = seconds / 3600
        minutes = (seconds / 60) % 60
        seconds = seconds % 60
        return '%0.2d:%02d:%02d' % (hours, minutes, seconds)

def setup(bot):
    bot.add_cog(Utils(bot))