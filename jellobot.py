import discord
from discord.ext import commands

import re
import random

import pickle

bank = {}

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

        if "poop" in message.content:
            if chance <= 50:
                await message.channel.send('Poop??? HAHAHAHHAHAHAHAHh :rofl::rofl: :rofl: :rofl: :rofl: :rofl: https://media.discordapp.net/attachments/777581776217440307/819984348580937778/explode.gif')
        
        if "cool" in message.content:
            if chance <= 50:
                await message.channel.send('i bet this is cooler https://cdn.discordapp.com/attachments/810275293839097926/824673855259672616/maxresdefault.png')
        
        if "bruh" in message.content:
            if chance <= 50:
                await message.channel.send('burh')

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

@client.command(name='create_account', help='This command gives you a bank account with $1,000')
async def create_account(ctx):
    global bank

    if ctx.author.name in bank:
        await ctx.send('Hey, you already have a bank account!')

    else:
        bank.update({ctx.author.name: 1000})
        await ctx.send('Account has been created, and $1,000 has been placed in it!')

@commands.cooldown(1, 6.0, commands.BucketType.user)
@client.command(name='work', help='This command gives you money ranging from 1-100, there is a 6 second cooldown')
async def work(ctx):
    global bank

    if ctx.author.name in bank:
        money = random.randint(1, 100)
        bank[ctx.author.name] += money

        await ctx.send(f'You earned ${money}')

    else:
        await ctx.send("You don't have a bank account")

@client.command(name='give', help='This command gives another person money')
async def give(ctx, name, money):
    global bank

    if ctx.author.name in bank:
        if name in bank:
            if bank[ctx.author.name] >= int(money):
                bank[name] += int(money)
                bank[ctx.author.name] -= int(money)

                await ctx.send(f'{name} has recieved ${money}')

            else:
                await ctx.send("You don't have that much money")

        else: 
            await ctx.send(f"{name} doesn't have a bank account")

    else:
        await ctx.send("You don't have a bank account")

@client.command(name='lb', help='See leadboard')
async def lb(ctx):
    global bank

    await ctx.send(str(bank))

@client.command(name='save', help='Save the bank info')
async def save(ctx):
    global bank
    pickle.dump(bank, open('bank.txt', 'wb'))
    await ctx.send(f'Saved Data {bank}')

@client.command(name='load', help='Load the bank info')
async def load(ctx):
    global bank
    
    with open('bank.txt', 'rb') as handle:
        data = handle.read()
  
    bank = pickle.loads(data)
    await ctx.send(f'Loaded Data {bank}')

@client.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send('why have you brought me to this cruel world')
        break

client.run(TOKEN, bot=True)
