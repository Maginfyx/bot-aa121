import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
import os
roles = ["491676004004134912"]

Client = discord.Client()
client = commands.Bot(command_prefix="?")

@client.event
async def on_message(message):
    if message.content.upper().startswith('?SALES'):
        userID = message.author.id
        server = client.get_server("490938256683302912")
        args = message.content.split(" ")
        messageid = message.id
        embed=discord.Embed(title=":shopping_cart: Item requested", description="Someone requested an item!", color=0x00ff00)
        embed.add_field(name="Game", value="%s" % (args[1]), inline=False)
        embed.add_field(name="Item", value="%s" % (args[2]), inline=False)
        embed.add_field(name="Quantity", value="%s" % (args[3]), inline=False)
        embed.add_field(name="User", value="<@%s>" % (userID), inline=False)
        embed.add_field(name="Receipt ID", value=messageid, inline=False)
        msg = await client.send_message(message.channel, "Getting ready... 0% done")
        time.sleep(1)
        await client.edit_message(msg, "Setting up order... 25% done")
        time.sleep(1)
        await client.edit_message(msg, "Contacting services... 50% done")
        time.sleep(1)
        await client.edit_message(msg, "Sending order... 75% done")
        time.sleep(2)
        await client.send_message(server.get_channel("490942613269250048"), embed=embed)
        await client.edit_message(msg, "Thank you for the purchase!")
    if message.content.upper().startswith('?ANNOUNCE'):
        if "490942293944041484" in [role.id for role in message.author.roles]:
            server = client.get_server("490938256683302912")
            args = message.content.split(" ")
            await client.send_message(server.get_channel("491676268853723138"), "@everyone %s" % (" ".join(args[1:])))
        else:
            await client.send_message(message.channel, "You do not meet the requirements to complete this action.")
    if message.content.upper().startswith('?WARNING'):
        if "490942293944041484" in [role.id for role in message.author.roles]:
            server = client.get_server("490938256683302912")
            args = message.content.split(" ")
            embed=discord.Embed(title=":warning: Warning from Admin", description="Warning from an adminstator.", color=0x00ff00)
            embed.add_field(name="Warning Reason", value="%s" % (" ".join(args[1:])), inline=False)
            await client.send_message(server.get_channel("495707512436162560"), embed=embed)
            await client.send_message(message.channel, "Admins have been warned.")
        else:
            await client.send_message(message.channel, "You do not meet the requirements to complete this action.")

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="Handling sales!"))
  
    



bot.run('BOT_TOKEN')
