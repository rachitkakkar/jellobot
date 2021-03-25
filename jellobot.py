import discord
from discord.ext import commands

import re
import random

client = commands.Bot(command_prefix='?')
TOKEN = ''

@client.event
async def on_message(message):
    if client.user.id != message.author.id and message.author.id != 690631706650083328:
        chance = 50

        if 'your' in message.content:
            regex = re.findall('(?<=your ).*', message.content, re.IGNORECASE)

            if len(regex) > 0:
                if chance <= 50:
                    await message.channel.send(f'your face is {regex[0]}')

        if 'you' in message.content:
            regex = re.findall('(?<=you ).*', message.content, re.IGNORECASE)

            if len(regex) > 0:
                if chance <= 50:
                    await message.channel.send(f'your face is {regex[0]}')

        if "you're" in message.content:
            regex = re.findall("(?<=you\'re ).*", message.content, re.IGNORECASE)

            if len(regex) > 0:
                if chance <= 50:
                    await message.channel.send(f'your face is {regex[0]}')

        if "im" in message.content or "Im" in message.content:
            regex = re.findall("(?<=im\'re ).*", message.content, re.IGNORECASE)

            if len(regex) > 0:
                if chance <= 50:
                    await message.channel.send(f'your face is {regex[0]}')

        if "is" in message.content:
            regex = re.findall("(?<=is ).*", message.content, re.IGNORECASE)

            if len(regex) > 0:
                if chance <= 50:
                    await message.channel.send(f'your face is {regex[0]}')

        if "bruh" in message.content:
            if chance <= 50:
                await message.channel.send(f'burh')

    await client.process_commands(message)

@client.event
async def on_ready():
    print('Bot ready!')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="my stonks go down"))

@client.command(name='die', help='This command returns a random last word')
async def die(ctx):
    responses = ['why have you brought my short life to an end', 'i could have done so much more', 'i have a family, kill them instead']
    await ctx.send(random.choice(responses))

@client.command(name='ping', help='This command returns latency')
async def ping(ctx):
    await ctx.send(f'**Pong!** {round(client.latency*1000)} ms')

@client.command(name='green_screen', help='This command helps you frame me')
async def green_screen(ctx):
    await ctx.send('https://i.ytimg.com/vi/80ygBP8r7As/maxresdefault.jpg')

@client.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send('why have you brought me to this cruel world')
        break

client.run(TOKEN, bot=True)
