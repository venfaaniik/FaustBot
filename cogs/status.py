import discord
from discord.ext import commands, tasks

import asyncio
from datetime import datetime
from itertools import cycle
import random
from random import choice, randint

class Status(commands.Cog):
    '''Status message'''

    def __init__(self, bot):
        self.bot = bot
        self.status = cycle(["with fire.", "dice poker.", "with pebbles.", "with a magelight.", "dead.", "Gwent.", "with Pebbles.", "."])

    @tasks.loop(seconds=120.0)
    async def change_status(self):
        easteregg = randint(1, 10000)
        if easteregg == 1268:
            print("Did you remember to put yourself in the correct position?")
            await self.bot.change_presence(activity=discord.Game("a game whose rules he does not know."))
        elif easteregg == 6666:
            print("Whispers of flame...")
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="to quiet whispers."))
        else:
            status = next(self.status)
            await self.bot.change_presence(activity=discord.Game(status))
        
    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.wait_until_ready()
        try:
            self.change_status.start()
            #print("status cog started")
        except Exception as e:
            print(f'**`ERROR:`** {type(e).__name__} - {e}')


def setup(bot):
    bot.add_cog(Status(bot))