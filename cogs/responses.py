import discord
from discord.ext import commands

import re
import random

shutup = False
una = False
is_human = True

class Responses(commands.Cog):
    '''Responses to various messages'''

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg):
        global shutup
        shutupChannel = channel = self.bot.get_channel(732387992727060522)
        faustDread = '<:faust_dread:731300962916106272>'

        if shutup == True and msg.author.id != 128440902468370432 and shutupChannel != msg.channel:
            return

        if "69" == msg.content:
            await msg.channel.send("Nice.")
            return
        if "420" == msg.content:
            await msg.channel.send("Blaze it.")
            return

        #..584 is avrae
        if msg.author == self.bot.user or msg.author.id == 261302296103747584:

            m = re.sub("<@![0-9]*>", "", str(msg.content))
            if "69" in m:
                await msg.channel.send("Nice.")
            elif "420" in m:
                await msg.channel.send("Blaze it.")
            else:
                return
        
        if msg.guild is None and msg.author != self.bot.user:
            channel = self.bot.get_channel(732387992727060522)
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

        if any([keyword in content for keyword in ('hello faust', "hi faust", "yo faust", "eyo faust", "henlo faust")]):
            if msg.author.id == 227205817642909698:
                await msg.channel.send("Hey there, pretty boy.")
            elif msg.author.id == 250389319884210196:
                await msg.channel.send("You hold too much power.")
            elif msg.author.id == 261970400328548363:
                await msg.channel.send("Greetings, me Rhena.")
            elif msg.author.id == 314337571377512448:
                await msg.channel.send("You're so tiny I want to pick you up.")
            elif msg.author.id == 417072424320761876:
                #await msg.channel.send("Whenever I see you, I remember that your God really *does* have a sense of humour.")
                await msg.channel.send("Hello, heard you coming from a mile away.")
            else:
                possible_responses = [
                    "Hi.",
                    "Hello.",
                    "Greetings. Now leave me be."
                ]
                await msg.channel.send(random.choice(possible_responses))

        if any([keyword in content for keyword in ('bye faust', "goodbye faust", "see ya faust", "see you faust")]):
            if msg.author.id == 227205817642909698:
                await msg.channel.send("Bye dipshit")
            elif msg.author.id == 250389319884210196:
                await msg.channel.send("Give me better rolls.")
            elif msg.author.id == 261970400328548363:
                await msg.channel.send("Don't tell me I'm *fired* " + faustDread)
            elif msg.author.id == 314337571377512448:
                await msg.channel.send("Noot you later.")
            elif msg.author.id == 417072424320761876:
                #await msg.channel.send("Don’t burn your fingers.")
                await msg.channel.send("I'll chain mail you later.")
            else:
                possible_responses = [
                    "Bye.",
                    "Dismissed.",
                    "Hmh."
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

        if ("count caldwell") in content:
            await msg.channel.send("Remove the 'o'.")


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


        if (re.search("(?:^|\W)tent(?:$|\W)", str(msg.content), re.IGNORECASE)):
            percent = random.randint(0, 100)
            bigassLine = random.randint(0,10000)
            if ("wank") in content:
                possible_responses = [
                    "That's just... disgusting",
                    "What the fuck.",
                    "Go outside. Pick up a rock. Touch some grass. Take a shower."
                ]
                await msg.channel.send(random.choice(possible_responses))
            else:
                if percent == 0:
                    possible_responses = [
                        "I would love to insult you but I'm afraid I won't do as well as nature did.",
                        "Do you get invited to many parties?",
                        "You're not worth the dirt to bury you in.",
                        "You're not worth the energy it'd take to disintegrate you with a simple spell."
                    ]
                    await msg.channel.send(random.choice(possible_responses))
                    return
                elif bigassLine == 1999:
                    await msg.channel.send("Tell me, why do you keep saying that word? I feel like it's in everywhere: In the wind that carries your awful smell, in the ground that eventually shall take your frigid body, even in the fire that will soon burn you; Just a flick of my fingers... Would you be kind and stop using this word 'Tent'. I do not wish to hear it anymore from that filthy mouth of yours. The next time I hear it, I'll remove your... speaking priviledges.")
                    return 
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
            await msg.channel.send("", file=discord.File("assets/fucker.gif"))

        # if any([keyword in content for keyword in ('shut up faust', 'silence faust', 'shut up, faust', 'silence, faust', 'SILENCEFSUST', 'shut the fuck up faust')]):
        #     await msg.channel.send("Fine. Silent treatment it is then.")
        #     shutup = True
        #     shutupChannel = self.bot.get_channel(msg.channel)
        #     await shutupTimer()
        #     return

        #without this the commands wont. work. at all. no touching
        #for some reason now it needed to be fucked with. it works fine without  XD
        #await self.bot.process_commands(msg)

        if content == ("faust concern"):
            await msg.channel.send("", file=discord.File("assets/faust_concern.png"))
        if content == ("mega chad supreme"):
            await msg.channel.send("", file=discord.File("assets/faust_megachadsupreme.png"))
        if content == ("oh no! anyway"):
            await msg.channel.send("", file=discord.File("assets/faust_ohnoanyway.png"))
        if content == ("faust do not"):
            await msg.channel.send("", file=discord.File("assets/faust_do_not.png"))
        if content == ("ma berries!"):
            await msg.channel.send("", file=discord.File("assets/edon_berries.png"))
        if content == ("faust ??"):
            await msg.channel.send("", file=discord.File("assets/faust_quesitionmark.png"))
        if content == ("faust, say the line"):
            await msg.channel.send("", file=discord.File("assets/faust_saytheline.jpg"))
        if content == ("resident sleeper"):
            await msg.channel.send("", file=discord.File("assets/faust_waiting.png"))
        if content == ("w h e e z e"):
            await msg.channel.send("", file=discord.File("assets/faust_wheeze.png"))
        if content == ("reynard blink"):
            await msg.channel.send("", file=discord.File("assets/reynard_blink.png"))
        if content == ("gathering souls"):
            await msg.channel.send("", file=discord.File("assets/soul_gather.png"))
        if content == ("your akutions have konesequenses"):
            await msg.channel.send("", file=discord.File("assets/the_consequences.jpg"))
        if content == ("elf and onion soup"):
            await msg.channel.send("", file=discord.File("assets/troll_soup.jpg"))
        if content == ("yikes"):
            await msg.channel.send("", file=discord.File("assets/yikes.jpg"))
        if content == ("need 2 pee") or content == ("need2pee") or content == ("need to pee"):
            await msg.channel.send("https://media.discordapp.net/attachments/816549902430765066/845595393663959130/unknown.png")

def setup(bot):
    bot.add_cog(Responses(bot))