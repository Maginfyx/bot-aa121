import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
import os
roles = ["491676004004134912"]

Client = discord.Client()
client = commands.Bot(command_prefix="pp!")

statusmsg = ['Cooking pizzas...','Checking pizzas...','Watching Pizza People...','Eating pizzas...','Selling pizzas...']

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
    

async def change_status():
        await client.wait until ready()
        messages = cycle(statusmsg)
    
        while no client.is_closed:
                current_status = next(messages)
                await client.change_presence(game=discord.Game(name=current_status))
                await asyncio.sleep(2)
    
   
client.loop.create_task(change_status())    
client.run(str(os.environ.get('bottoken')))

 
