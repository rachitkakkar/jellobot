import discord
from discord.ext import commands

import re

client = commands.Bot(command_prefix='>>')
TOKEN = ''

@client.event
async def on_message(message):
    if client.user.id != message.author.id:
        if 'your' in message.content:
            regex = re.findall('(?<=your ).*', message.content, re.IGNORECASE)

            if len(regex) > 0:
                await message.channel.send(f'your face is {regex[0]}')

        if 'you' in message.content:
            regex = re.findall('(?<=you ).*', message.content, re.IGNORECASE)

            if len(regex) > 0:
                await message.channel.send(f'your face is {regex[0]}')

        if "you're" in message.content:
            regex = re.findall("(?<=you\'re ).*", message.content, re.IGNORECASE)

            if len(regex) > 0:
                await message.channel.send(f'your face is {regex[0]}')

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
