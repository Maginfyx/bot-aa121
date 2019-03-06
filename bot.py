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
        await client.send_message(message.channel, "<@%s> This bot has multiple features. Check them out below!" % (userID))
        await client.send_message(message.channel, "https://bit.ly/2Tlbp1Z")
        await client.send_message(message.channel, "**This bot restarts very often for repairs, bug fixes and updates. The game status sometimes tells you when updates are incoming!**")
        await client.send_message(message.channel, "https://bit.ly/2J570eC")
        await client.send_message(message.channel, "**Pizza People is a Discord server owned by Jack (aka. JacktheG4m3r). It at first was made to be a friend server, but has grown to be his fan discord server. Pizza People is a friendly server, but remember to follow the rules!**")
        await client.send_message(message.channel, "https://bit.ly/2Tlbp1Z")
        await client.send_message(message.channel, "https://bit.ly/2Tlbp1Z")
@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="Cooking Pizzas!"))
   
      
  
    
client.run(str(os.environ.get('bottoken')))
 
