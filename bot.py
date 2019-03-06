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
        server = client.get_server("514856941617414165")
        args = message.content.split(" ")
        messageid = message.id
        embed=discord.Embed(title=":question: PPBot Help", description="You have requested help with the bot.", color=0x00ff00)
        embed.add_field(name="<@%s>", value=" " % (userID), inline=False)
        embed.add_field(name="Here are the bot commands!", value="help, say, info" inline=False)
        time.sleep(1)
        msg = await client.send_message(message.channel, embed=embed)
        await client.edit_message(msg, "Here is the help!")


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="Cooking Pizzas!"))
  
    
client.run(str(os.environ.get('bottoken')))
 
