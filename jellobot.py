import discord
from discord.ext import commands

import re
import random

client = commands.Bot(command_prefix='>>')
TOKEN = ''

@client.event
async def on_message(message):
    if client.user.id != message.author.id:
        chance = random.randint(1,100)

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

@client.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send('why have you brought me to this cruel world')
        break

client.run(TOKEN, bot=True)
