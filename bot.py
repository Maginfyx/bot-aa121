import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
import os
roles = ["491676004004134912"]

Client = discord.Client()
client = commands.Bot(command_prefix="pp!")

@client.event
async def on_message(message):
    if message.content.upper().startswith('PP!INFO'):
        userID = message.author.id
        await client.send_message(message.channel, "*Hi there <@%s>! Welcome to Pizza People, JacktheG4m3r's fan discord server! To find more info, please go to the info channel in the channel category* ***'announcements and stuff'***." % (userID))
    if message.content.upper().startswith('PP!SAY'):
        args = message.content.split(" ")
        await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
    if message.content.upper().startswith('PP!HELP'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> **Bot Commands**" % (userID))
        await client.send_message(message.channel, "help, say, info, subjack")
    if message.content.upper().startswith('PP!SUBJACK'):
        userID = message.author.id
        await client.send_message(message.channel, "Subscribe to Jack here: https://bit.ly/2H4woiP")
    if message.content.upper().startswith('PP!MEGAOOFSPAM'):
        await bot.say(random.choice(["@everyone DIE",
                                             "@everyone Do you agree Jack has a penis so small you can't see it?",
                                             "@everyone Also, you have a bitch face so go fuck yourself!",
                                             "@everyone PAY 500 US DOLLARS OR NO COMPUTER AND CONSOLE FOR A YEAR",
                                             "@everyone Ok please get out the fucking room I'm playing minecraft!",
                                             "@everyone Mommy...PLEASE FUCKING LET ME MAKE THIS MINECRAFT MINEPLEX BEDWARS VIDEO!!1!11!",
                                             "@everyone WHO WANTS ADMIN? SIMPLY GO TO PORNHUB.COM AND REDEEM YOUR PRIZE BY WATCHING 1,000 PORN VIDEOS! NO LOGIN INFO OR DOWNLOADS!",
                                             "@everyone Nivea Soft Cream...More Like Nivea Soft Dick",
                                             "@everyone Jack is a cunt lmao"]))  

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="Cooking Pizzas!"))
    
   
    
client.run(str(os.environ.get('bottoken')))
 
