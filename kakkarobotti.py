import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio
import time
import random
from random import choice
import sys

PREFIX = ">"
bot = commands.Bot(command_prefix=PREFIX)
TOKEN = "NzMwNDQyODExNzY5NDg3NDIw.XwXk0Q.qnEv4yi0L-3XBVNNv6Rlq4qOScs"
wagons = 0

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    print(bot.user.id)
    bot.loop.create_task(background_loop())
    print("Background loop created")
    print("------------")

@bot.event
async def on_message(msg):
    faustDread = '<:faust_dread:731300962916106272>'

    if msg.author == bot.user:
        return
    
    if msg.guild is None and msg.author != bot.user:
        channel = bot.get_channel(732387992727060522)
        author = msg.author
        await channel.send(str(author) + ": " + msg.content)
    
    if msg.author.id == 83010416610906112:
        print("nightbot is shit")
        possible_responses = [
            "go forth and multiply",
            "go fuck yourself",
            "***FUCK THE BARKEEPER!***",
            "give me back my money!"
        ] 
        await msg.channel.send(random.choice(possible_responses))
    
    if msg.content == ('HELLO FAUST'):
        if msg.author.id == 227205817642909698:
            await msg.channel.send("Shut the fuck up")
        else:
            await msg.channel.send("Hey, hey, hey, keep it down, okay?")
        return
    
    content = str(msg.content).lower()

    if content == ('hello faust'):
        if msg.author.id == 227205817642909698:
            await msg.channel.send("Hey there, pretty boy")
        elif msg.author.id == 250389319884210196:
            await msg.channel.send("You cannot kill me in a way that matters.")
        elif msg.author.id == 261970400328548363:
            await msg.channel.send("Greetings, me Rhena")
        elif msg.author.id == 314337571377512448:
            await msg.channel.send("You're so tiny I want to pick you up")
        elif msg.author.id == 417072424320761876:
            await msg.channel.send("Whenever I see you, I remember that your God really *does* have a sense of humour.")
        else:
            possible_responses = [
                "Hi.",
                "Hello.",
                "Greetings. We done here? Good. Now leave me be."
            ]
            await msg.channel.send(random.choice(possible_responses))

    if content == ('bye faust'):
        if msg.author.id == 227205817642909698:
            await msg.channel.send("Bye dipshit")
        elif msg.author.id == 250389319884210196:
            await msg.channel.send("Give me better rolls")
        elif msg.author.id == 261970400328548363:
            await msg.channel.send("Me Rhena.")
        elif msg.author.id == 314337571377512448:
            await msg.channel.send("Noot you later")
        elif msg.author.id == 417072424320761876:
            await msg.channel.send("Turn around and I'll burn your ass, have a nice day though")
        else:
            possible_responses = [
                "Bye",
                "Dismissed",
                "Hmh"
            ]
            await msg.channel.send(random.choice(possible_responses))
    
    if any([keyword in content for keyword in ('eternal fire', "witch hunter", "witch hunters")]):
        possible_responses = [
            "<:faust_dread:731300962916106272>",
            'No.',
            'Keep that talk away from me.',
            'Yeah, fuck off',
            'You have the audacity to talk about that bullshit here, in front of me',
            "How much value do you put on your tongue?",
            'ᵣₑₑₑₑₑₑₑₑₑₑₑ'
        ] 
        await msg.add_reaction(faustDread)
        await msg.channel.send(random.choice(possible_responses))

    if content == ("faust?"):
        possible_responses  = [
            "<:faust_dread:731300962916106272>",
            "Yes {}?".format(msg.author.display_name),
            "What is it, {}?".format(msg.author.display_name)
        ]
        await msg.channel.send(random.choice(possible_responses))

    if "wagon" in content:
        possible_responses = [
            "Let's not talk about that.",
            "Change the subject, please.",
            "DON'T.",
            "I am pISSED",
            "Stay quiet!",
            "Don't remind me."
        ]
        await msg.channel.send(random.choice(possible_responses))

    if any([keyword in content for keyword in ('wagen', 'vagen', 'vvagen', 'vvagon')]):
        possible_responses = [
            "Can't even spell it correctly?",
            "Here, let me help you: Wagon.",
            "Really? At least you tried."
        ]
        await msg.channel.send(random.choice(possible_responses))

    if ("sauna") in content:
        if ("swedish") in content:
            possible_responses = [
                "Those can burn.",
                "Not even a real sauna.",
                "Those poor souls."
            ]
        elif ("wank") in content:
            possible_responses = [
                "Really? Can you not?",
                "You're not worth the dirt to bury you in.",
                "I am sure even the Church of Eternal Fire disapproves it."
            ]
        else:
            possible_responses = [
                "<:eyess:633797028882677760>",
                "Sauna? Where?",
                "Oh, to find one...",
                "I miss them."
            ]
        await msg.channel.send(random.choice(possible_responses))

    if ("tent") in content:
        percent = random.randint(0, 100)
        if percent == 0:
            possible_responses = [
                "I would love to insult you but I'm afraid I won't do as well as nature did.",
                "Do you get invited to many parties?",
                "You're not worth the dirt to bury you in.",
                "You're not worth the energy it'd take to disintegrate you with a simple spell.",
            ]
            await msg.channel.send(random.choice(possible_responses))
        else:
            possible_responses = [
                "I don't know what you're talking about",
                "I am looking away",
                "I do not see it",
                "It was the wine",
                "It was the wind, I swear",
                "It was the other guy over there",
                "Tent? What tent?",
                "Tent? Haven't seen any of those here"
            ]
            await msg.channel.send(random.choice(possible_responses))

    if content == ("❤️"):
        await msg.channel.send("❤️")

    if content.startswith("bonk"):
        await msg.channel.send("", file=discord.File("fucker.gif"))

    #without this the commands wont. work. at all. no touching
    await bot.process_commands(msg)

@bot.event
async def on_member_join(member):
    print("A new member " + member.name + " joined!")
    channel = member.guild.system_channel
    if channel is not None:
        await channel.send("Welcome {0.mention}. I hope you enjoy your stay".format(member))   

@bot.command()
async def DM(ctx, arg, *, message):
    user_id = (arg)
    user = await bot.fetch_user(user_id)
    if ctx.author.id == 128440902468370432:
        await user.send(message)
    elif ctx.author.id == 250389319884210196:
        await ctx.send("How far are you willing to go to get this power of mine?")
    else:
        await ctx.send("Sorry sweetheart, can't do it for you")

@bot.command()
async def DMuser(ctx, user: discord.Member, *, message):
    if ctx.author.id == 128440902468370432:
        await user.send(message)
    elif ctx.author.id == 250389319884210196:
        await ctx.send("There is only one being with this kind of power and it is not you.")
    else:
        await ctx.send("Sorry sweetheart, can't do it for you")

@bot.command()
async def sendTo(ctx, arg, *, message):
    if ctx.author.id == 128440902468370432:
        #channel = bot.get_channel(730444242836652042)
        arg = int(arg)
        channel = bot.get_channel(arg)
        await channel.send(message)
    elif ctx.author.id == 250389319884210196:
        await ctx.send("This is something that not even Gods should meddle with.")
    else:
        await ctx.send("Sorry sweetheart, can't do it for you")

@bot.command()
async def join(ctx):
    voicechannel = discord.utils.get(ctx.guild.channels, name='General')
    vc = await voicechannel.connect()
    vc.play(discord.FFmpegPCMAudio("testing.mp3"), after=lambda e: print('done', e))

#do it like that you can requets for others' playlists too
@bot.command()
async def playlist(ctx, arg):
    if arg=="youtube":
        await ctx.send("https://www.youtube.com/playlist?list=PLQhLL9WuSGAZA-V3mRK6YQYJO_7VWlylV")
    elif arg == "spotify":
        await ctx.send("https://open.spotify.com/playlist/4K31hkykN1DyYacH5vlJnG")
    else:
        await ctx.send("The command is playlist youtube/spotify")
    
@bot.command()
async def info(ctx, user: discord.Member):
    if user is not None:
        await ctx.send("The users name is: {}".format(user.name))
        await ctx.send("The users id is: {}".format(user.id))
        await ctx.send("The users status is: {}".format(user.status))
        await ctx.send("The users highest role is: {}".format(user.top_role))
        await ctx.send("The user joined at: {}".format(user.joined_at))
    else:
        await ctx.send("You must mention a user!")

#dice throw test
@bot.command(name='roll', aliases=['r'])
async def roll(ctx, dice: str):
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
    await ctx.send("Your roll: (" + str(resultTotal) + ") \n (" + str(rollsList).replace("'", "").strip("[]") + ")")

#higher
@bot.command()
async def roII(ctx, dice: str):
    rollsList = []
    resultTotal = 0
    cheat = 1
    try: 
        rolls, limit = map(int, dice.split('d'))
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
    await ctx.send("Your roll: (" + str(resultTotal) + ") \n (" + str(rollsList).replace("'", "").strip("[]") + ")")

#lower
@bot.command()
async def rolI(ctx, dice: str):
    rollsList = []
    resultTotal = 0
    cheat = 1
    try: 
        rolls, limit = map(int, dice.split('d'))
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
    await ctx.send("Your roll: (" + str(resultTotal) + ") \n (" + str(rollsList).replace("'", "").strip("[]") + ")")

@bot.command()
async def w(ctx):
    print("wagons: " + str(wagons))
    resultTotal = unaSaves = totalDead = 0
    for x in range(int(wagons)):
        resultTotal += random.randint(1, 10)
    unaSaves = random.randint(1, resultTotal)
    totalDead = (resultTotal - unaSaves)
    await ctx.send("Dropped wagons: " + str(wagons) + "\nCollateral damage: (" + str(resultTotal) + ") \nUna manages to save: (" + str(unaSaves) + "). Good job! \nTotal dead: (" + str(totalDead) + "). F to them.")

def bolding(rollList, limit):
    tempList = []
    i = 0
    for x in rollList:
        tempNmb = rollList[i]
        if tempNmb == limit or tempNmb == 1:
            bolded = ("**" + str(tempNmb) + "**")
            tempList.append(bolded)
            #print(bolded)
        else:
            tempList.append(rollList[i])
        i += 1
    #print(tempList)
    return tempList

# FAUST THE BAAAARD?

@bot.command()
async def stop(self, ctx):
    """Stops and disconnects the bot from voice"""
    await ctx.voice_client.disconnect()


async def background_loop():
    await bot.wait_until_ready()
    print("background_loop initialized")
    global wagons
    wagons = random.randint(1, 3)
    #wagons = 11
    while True:
        wagons += random.randint(1,10)
        #print("wagons: " + str(wagons))
        #channel = bot.get_channel("632372863495700519") 
        randMsg = random.randint(1, 8)
        if randMsg == 1:
            #wagons
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= str(wagons) + " wagons levitating."))
        elif randMsg == 2:
            #listening
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name = "his own beautiful voice."))
        elif randMsg == 3:
            #playing
            await bot.change_presence(activity=discord.Game(name="with fire."))
        elif randMsg == 4:
            #playing2
            await bot.change_presence(activity=discord.Game(name="Gwent again and losing."))
        elif randMsg == 5:
            guild = bot.get_guild(458318646108749824)
            user = choice(guild.members)
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= "{}".format(user.display_name)))
        elif randMsg == 6:
            guild = bot.get_guild(458318646108749824)
            user = choice(guild.members)
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= "{}".format(user.display_name) +  " from afar ( ͡◉ ͜ʖ ͡◉)"))
        elif randMsg == 7:
            guild = bot.get_guild(458318646108749824)
            user = choice(guild.members)
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= "{}".format(user.display_name) + " levitating"))
        elif randMsg == 8:
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= "ALL THE " + str(wagons) + " WAGONS DROPPING."))
        else:
            print("randmsg = " + str(randMsg) + ", it gave an error")
        await asyncio.sleep(120) #Sleep for x before updating
        if randMsg == 8:
            wagons = 0

bot.run(TOKEN)