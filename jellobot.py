import discord
from discord.ext import commands

import re
import random
import pickle
from nltk.corpus import wordnet as wn
from datetime import datetime

bank = {}
all_verbs = [word for synset in wn.all_synsets('v') for word in synset.lemma_names()]

client = commands.Bot(command_prefix='?')
TOKEN = 'ODI0MzQ2NzI5NjIwMzA4MDA5.YFuCtw.25TEAm7RPLg29HOGGWpbHlL3rtk'

@client.event
async def on_message(message):
    if client.user.id != message.author.id:
        chance = random.randint(1, 100)
        chance_threshold = 15

        for word in message.content.split(' '):
            if word in all_verbs:
                if chance <= chance_threshold:
                    content = re.findall('(?<='+word+' '').*', message.content, re.IGNORECASE)
                    content = word + 's ' + content[0]
                    
                    await message.channel.send(f'your face {content}')
                    break

        if 'poop' in message.content:
            if chance <= chance_threshold:
                await message.channel.send('Poop??? HAHAHAHHAHAHAHAH :rofl::rofl: :rofl: :rofl: :rofl: :rofl: https://media.discordapp.net/attachments/777581776217440307/819984348580937778/explode.gif')
        
        if 'cool' in message.content:
            if chance <= chance_threshold:
                await message.channel.send('i bet this is cooler https://cdn.discordapp.com/attachments/810275293839097926/824673855259672616/maxresdefault.png')
        
        if 'bruh' in message.content:
            if chance <= chance_threshold:
                await message.channel.send('burh')

        if '?poll' in message.content:
            await message.delete()

    await client.process_commands(message)

@client.event
async def on_ready():
    print('Bot ready!')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='my stonks go down'))

@client.command(name='die', help='This command returns a random last word')
async def die(ctx):
    responses = ['why have you brought my short life to an end', 'i could have done so much more', 'i have a family, kill them instead']
    await ctx.send(random.choice(responses))

@client.command(name='useless', help='This command returns a useless image')
async def useless(ctx):
    responses = ['https://static.boredpanda.com/blog/wp-content/uploads/2016/10/most-pointless-useless-things-65-581068f5ece85__605.jpg', 
    'https://static.boredpanda.com/blog/wp-content/uploads/2016/10/most-pointless-useless-things-54-58104dfd135ee__605.jpg', 
    'https://static.boredpanda.com/blog/wp-content/uploads/2016/10/most-pointless-useless-things-27-580efbbfaf47d__605.jpg', 
    'https://static.boredpanda.com/blog/wp-content/uploads/2016/10/most-pointless-useless-things-64-5810663160697__605.jpg', 
    'https://static.boredpanda.com/blog/wp-content/uploads/2016/10/most-pointless-useless-things-580f00ea20fbc__605.jpg', 
    'https://static.boredpanda.com/blog/wp-content/uploads/2016/10/most-pointless-useless-things-20-580efbb012454__605.jpg', 
    'https://static.boredpanda.com/blog/wp-content/uploads/2016/10/most-pointless-useless-things-28-580efbc2b7d17__605.jpg', 
    'https://static.boredpanda.com/blog/wp-content/uploads/2016/10/most-pointless-useless-things-56-5810555a6ca72__605.jpg', 
    'https://static.boredpanda.com/blog/wp-content/uploads/2016/10/most-pointless-useless-things-58-580f509a12aa1__605.jpg', 
    'https://static.boredpanda.com/blog/wp-content/uploads/2016/10/most-pointless-useless-things-50-580f127697aa2__605.jpg', 
    'https://static.boredpanda.com/blog/wp-content/uploads/2016/10/most-pointless-useless-things-60-58106823f0dad__605.jpg', 
    'https://static.boredpanda.com/blog/wp-content/uploads/2016/10/most-pointless-useless-things-22-580efbb5c06e1__605.jpg', 
    'https://static.boredpanda.com/blog/wp-content/uploads/2016/10/most-pointless-useless-things-19-580efbadd9602__605.jpg', 
    'https://static.boredpanda.com/blog/wp-content/uploads/2016/10/most-pointless-useless-things-60-58105e76caf94__605.jpg', 
    'https://static.boredpanda.com/blog/wp-content/uploads/2016/10/most-pointless-useless-things-580f080cc3f2e__605.jpg', 
    'https://static.boredpanda.com/blog/wp-content/uploads/2016/10/most-pointless-useless-things-36-580efbd3bffe9__605.jpg', 
    'https://static.boredpanda.com/blog/wp-content/uploads/2016/10/most-pointless-useless-things-40-580f0af19a2d2__605.jpg',
    'https://static.boredpanda.com/blog/wp-content/uploads/2016/10/most-pointless-useless-things-56-580f5037ead05__605.jpg',
    'https://static.boredpanda.com/blog/wp-content/uploads/2016/10/most-pointless-useless-things-34-580efbd040884__605.jpg',
    'https://static.boredpanda.com/blog/wp-content/uploads/2016/10/most-pointless-useless-things-42-580f0c41c293c__605.jpg',
    'https://static.boredpanda.com/blog/wp-content/uploads/2016/10/most-pointless-useless-things-50-580f1f4a270ef__605.jpg',
    'https://static.boredpanda.com/blog/wp-content/uploads/2016/10/most-pointless-useless-things-53-580f197497207__605.jpg']

    await ctx.send(random.choice(responses))

@client.command(name='poll', help='This command allows a poll with upvotes and downvotes', pass_context = True)
async def poll(ctx, *, question):
    embed = discord.Embed(title = 'POLL', color=ctx.author.color, description=question, timestamp=datetime.now())
    embed.set_footer(text=f'AUTHOR: {ctx.author.name}')
    message = await ctx.send(embed=embed) 
    await message.add_reaction('👍')
    await message.add_reaction('👎')

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

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f'This command is on cooldown, you can use it in {round(error.retry_after, 2)} seconds')

client.run(TOKEN, bot=True)