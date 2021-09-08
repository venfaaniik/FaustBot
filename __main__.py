import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio #needed
import time
from datetime import datetime #needed
import random
from random import choice
import sys
import os.path
from os import path
from pathlib import Path

PREFIX = ">"
intents = discord.Intents().default()
intents.members = True
intents.presences = True
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

TOKEN = open("TOKEN.txt","r").read()

#wagons = 0
#casualties = 0


# Below cogs represents our folder our cogs are in. Following is the file name. So 'meme.py' in cogs, would be cogs.meme
# Think of it like a dot path import
initial_extensions = ['cogs.responses',
                        'cogs.status',
                        'cogs.commands',
                        'cogs.utils',
                        'cogs.music',]


if __name__ == '__main__':
    print('---------------------------------')
    for extension in initial_extensions:
        bot.load_extension(extension)
        print(str(extension) + " loaded.")

@bot.event
async def on_ready():
    print('\n\n---------------------------------')
    print('Logged in as {0.user}'.format(bot))
    print('Bot id: ' + str(bot.user.id))
    print('Discord version: ' + str(discord.__version__))
    print('---------------------------------')
    # bot.loop.create_task(background_loop())
    # #bot.loop.create_task(checkTime())
    # #print("Background loop created")
    # if path.exists("casualties.txt"):
    #     print("File      Path:", os.path.abspath("casualties.txt"))
    #     await readWagons()
    # else:
    #     print("File      Path:", os.path.abspath("casualties.txt"))
    #     await writeWagons()
    # print(casualties)
    # print("------------")

@bot.event
async def on_member_join(member):
    print("A new member " + member.name + " joined!")
    channel = member.guild.system_channel
    if channel is not None:
        await channel.send("Welcome {0.mention}. I hope you enjoy your stay".format(member))

@bot.event
async def on_member_update(before, after): 
    if (str(after.id) == "128440902468370432"):
        if (str(after.status) == "invisible") or (str(after.status) == "offline"):
                await bot.change_presence(status=discord.Status.invisible)
                # extensions disable
                print('---------------------------------')
                for extension in initial_extensions:
                    bot.unload_extension(extension)
                    print(str(extension) + " unloaded.")
                print('---------------------------------')

        elif (str(before.status) == "offline") or (str(before.status) == "invisible"):
                await bot.change_presence(status=discord.Status.online)
                # extensions re-enable
                print('---------------------------------')
                for extension in initial_extensions:
                    bot.load_extension(extension)
                    print(str(extension) + " loaded.")
                print('---------------------------------')


    

@bot.command(hidden = True)
async def DM(ctx, arg, *, message):
    """DM any user, must give ID"""
    user_id = (arg)
    user = await bot.fetch_user(user_id)
    if ctx.author.id == 128440902468370432:
        await user.send(message)
    elif ctx.author.id == 250389319884210196:
        await ctx.send("How far are you willing to go to get this power of mine?")
    else:
        await ctx.send("Sorry sweetheart, can't do it for you")
    await ctx.message.delete()

@bot.command(hidden = True)
async def DMuser(ctx, user: discord.Member, *, message):
    """DM any user, must mention"""
    if ctx.author.id == 128440902468370432:
        await user.send(message)
    elif ctx.author.id == 250389319884210196:
        await ctx.send("There is only one being with this kind of power and it is not you.")
    else:
        await ctx.send("Sorry sweetheart, can't do it for you")
    await ctx.message.delete()

@bot.command(hidden = True)
async def sendTo(ctx, arg, *, message):
    """Sends a message to a channel"""
    if ctx.author.id == 128440902468370432:
        arg = int(arg)
        channel = bot.get_channel(arg)
        await channel.send(message)
    elif ctx.author.id == 250389319884210196:
        await ctx.send("This is something that not even Gods should meddle with.")
    else:
        await ctx.send("Sorry sweetheart, can't do it for you")
    await ctx.message.delete()

@bot.command(hidden = True)
async def say(ctx, *, message):
    """Say something to the current channel as Faust"""
    if ctx.author.id == 128440902468370432:
        await ctx.send(message)
    elif ctx.author.id == 250389319884210196:
        await ctx.send("This is something that not even Gods should meddle with.")
    else:
        await ctx.send("Sorry sweetheart, can't do it for you")
    await ctx.message.delete()
    
@bot.command()
async def info(ctx, user: discord.Member):
    """Gives information about any user"""
    if user is not None:
        await ctx.send("The users name is: {}".format(user.name))
        await ctx.send("The users id is: {}".format(user.id))
        await ctx.send("The users status is: {}".format(user.status))
        await ctx.send("The users highest role is: {}".format(user.top_role))
        await ctx.send("The user joined at: {}".format(user.joined_at))
    else:
        await ctx.send("You must mention a user!")

#dice throw, simple
@bot.command(name='roll', aliases=['r'])
async def roll(ctx, dice: str):
    """Roll NdN"""
    rollsList = []
    resultTotal = 0
    try: 
        rolls, limit = map(int, dice.split('d'))
    except Exception:
         await ctx.send('Format has to be in NdN!')
         return
    for x in range(int(rolls)):
        temp = random.randint(1, limit)
        rollsList.append(temp)
        resultTotal += temp
    rollsList = bolding(rollsList, limit)
    await ctx.send("{0.mention}\n".format(ctx.author) + "**Roll:** " + dice + " (" + str(rollsList).replace("'", "").strip("[]") + ")" + "\n**Total:** (" + str(resultTotal) + ")")
    await ctx.message.delete()

# cheat for higher rolls
@bot.command(hidden = True)
async def roII(ctx, dice: str):
    """High roll-cheat"""
    rollsList = []
    resultTotal = 0
    cheat = 1
    try: 
        rolls, limit = map(int, dice.split('d'))
        # works only for the author/Void
        if ctx.author.id == 128440902468370432:
             cheat = random.randint(1, limit)
    except Exception:
         await ctx.send('Format has to be in NdN!')
         return

    for x in range(int(rolls)):
        if cheat > 0:
            temp = random.randint(cheat, limit)
        else:
            temp = random.randint(1, limit)
        rollsList.append(temp)
        resultTotal += temp
    rollsList = bolding(rollsList, limit)
    await ctx.send("{0.mention}\n".format(ctx.author) + "**Roll:** " + dice + " (" + str(rollsList).replace("'", "").strip("[]") + ")" + "\n**Total:** (" + str(resultTotal) + ")")
    await ctx.message.delete()

#cheat for lower rolls
@bot.command(hidden = True)
async def rolI(ctx, dice: str):
    """Low roll-cheat"""
    rollsList = []
    resultTotal = 0
    cheat = 1
    try: 
        rolls, limit = map(int, dice.split('d'))
        # works only for the author/Void
        if ctx.author.id == 128440902468370432:
             cheat = random.randint(-limit+1, 0)
    except Exception:
         await ctx.send('Format has to be in NdN!')
         return
    for x in range(int(rolls)):
        if cheat < 0:
            temp = random.randint(1, (limit+cheat))
        else:
            temp = random.randint(1, limit)
        rollsList.append(temp)
        resultTotal += temp

    rollsList = bolding(rollsList, limit)
    await ctx.send("{0.mention}\n".format(ctx.author) + "**Roll:** " + dice + " (" + str(rollsList).replace("'", "").strip("[]") + ")" + "\n**Total:** (" + str(resultTotal) + ")")
    await ctx.message.delete()


    ### a relict from the past. ###
# ------------------------------------------------- #

# @bot.command(aliases=['wagons', 'wagon'])
# async def w(ctx, *args):
#     """Drops the current amount of levitating wagons"""
#     global casualties
#     global is_human
#     global una

#     resultTotal = unaSaves = totalDead = 0
#     for x in range(int(wagons)):
#         resultTotal += random.randint(1, 10)
#     casualties +=resultTotal

#     if is_human == True:
#         saver = "Someone"
#         if ctx.author.id == 261970400328548363:
#             saver = "Una"
#         elif ctx.author.id == 227205817642909698:
#             saver = "Edon"
#         elif ctx.author.id == 417072424320761876:
#             saver = "Belagorn"
#         elif ctx.author.id == 128440902468370432:
#             saver = "Someone"
#         elif ctx.author.id == 250389319884210196:
#             saver = "The God"
#         else:
#             saver = ctx.author.display_name
#         savePerc = random.randint(0, 100)
#         if (savePerc == 0) or (savePerc == 100):
#             if (savePerc == 100):
#                 totalDead = resultTotal
#             else:
#                 totalDead = 0
#         else:
#             totalDead = (resultTotal * (savePerc * 0.01))

#         unaSaves = int(resultTotal) - int(totalDead)
#         casualties -= int(unaSaves)
        
#         if unaSaves == resultTotal:
#             await ctx.send("Dropped wagons: " + str(wagons) + "\nCollateral damage: (" + str(resultTotal) + ") \n" + saver + " manages to save: (" + str(int(unaSaves)) + "). Holy fuck! \nTotal dead: (" + str(int(totalDead)) + "). BUFF " + saver + ".")
#         elif unaSaves == 0:
#             await ctx.send("Dropped wagons: " + str(wagons) + "\nCollateral damage: (" + str(resultTotal) + ") \n" + saver + " manages to save: (" + str(int(unaSaves)) + "). \nTotal dead: (" + str(int(totalDead)) + ").  Wake up, " + saver + ".")
#         else:
#             await ctx.send("Dropped wagons: " + str(wagons) + "\nCollateral damage: (" + str(resultTotal) + ") \n" + saver + " manages to save: (" + str(int(unaSaves)) + "). Nice. \nTotal dead: (" + str(int(totalDead)) + "). Good job " + saver + ".")
#         await ctx.message.delete()
#         una = True

#     await writeWagons()

# async def writeWagons():
#     f = open("casualties.txt", "w")
#     f.write(str(int(casualties))) 
#     f.close()

# async def readWagons():
#     f = open("casualties.txt", "r")
#     global casualties
#     casualties = int(f.read())

def bolding(rollList, limit):
    tempList = []
    i = 0
    for x in rollList:
        tempNmb = rollList[i]
        if tempNmb == limit or tempNmb == 1:
            bolded = ("**" + str(tempNmb) + "**")
            tempList.append(bolded)
        else:
            tempList.append(rollList[i])
        i += 1
    return tempList

# doesn't work anymore.
# async def checkTime():
#     await bot.wait_until_ready()
#     while not bot.is_closed:
#         sent = False
#         while True:
#             now = datetime.now()
#             current_time = now.strftime("%H:%M")
#             #print("Current Time =", current_time)

#             if (current_time == '04:20') and (sent == False):  # check if matches with the desired time
#                 print('Blazing it!')
#                 channel = bot.get_channel(632372863495700519)
#                 await channel.send("Blaze it.")
#                 sent = True
#             else:
#                 sent = False
#             await asyncio.sleep(60)

bot.run(TOKEN, bot=True, reconnect=True)