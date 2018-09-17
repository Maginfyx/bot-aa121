import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

api = str(os.environ.get('RIOT_KEY'))


Client = discord.Client()
client = commands.Bot(command_prefix="?")

@client.event
async def on_message(message):
    if message.content.upper().startswith('!SALES'):
        userID = message.author.id
        server = client.get_server("490938256683302912")
        args = message.content.split(" ")
        await client.send_message(server.get_channel("490942613269250048"), "%s" % (" ".join(args[1:])))
        await client.send_message(message.author, "A salesman will contact you! Thank you for buying! Item you wanted to buy:")
        await client.send_message(message.author, "%s" % (" ".join(args[1:])))
        await client.send_message(server.get_channel("490942613269250048"), "<@%s> requested a sale!" % (userID))

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="Handling sales!"))

bot.run(os.environ['BOT_TOKEN'])

client.run("NDkxMjc5MTAyMDgzMzM0MTQ1.DoFnUA.5QMJow6njym0oncsh_dJTDRFFDE")
