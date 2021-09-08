import discord
from discord.ext import commands

from datetime import datetime
import random

class Commands(commands.Cog):
    '''Various Commands'''

    @commands.command(name='Clairvoyance', aliases=['c', 'foresee', 'foretell', 'predict'])
    async def clairvoyance(self, ctx):
        ''' < A classic 8-ball but more magic >'''

        possible_responses = [
                'Definitely not.',
                'The Destiny sure isn\'t on your side.',
				'This future shows the outcome is negative.',
				'How could you even consider that.' ,
                'No.',
				'Neén.',
                'Eh, I don\'t think so.',
                'That is unlikely.',
                'No, probably not.',
                'Probably.',
                'There is a chance for that.',
                'Oh yes.',
				'Yeá.',
				'Indubitably.',
                'Certainly.',
                'Without a doubt.',
                'As I see it, yes.',
                'I am sure of that.'
                ]
        await ctx.send(random.choice(possible_responses))

## my deranged way to sign dates on art. Used for annoying certain friends for now.
    @commands.command(name = 'date', hidden = True)
    async def date(self, ctx):
        date = int(datetime.today().strftime('%Y%m%d'))
        rooted = date**2
        await ctx.send("Today is √" + str(rooted))

    @commands.command(name = 'Bubblewrap', description= 'I give you some modern bubblewrap to pop. Pop away.', aliases=['bw', 'bubblewrap'])
    async def bubblewrap (self, ctx):
        '''< For peace of mind >'''

        line = "||pop|| ||pop|| ||pop|| ||pop|| \n"
        await ctx.send("Have some bubble wrap: \n" + line + line + line + line)

def setup(bot):
    bot.add_cog(Commands(bot))