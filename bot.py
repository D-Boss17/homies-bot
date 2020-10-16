# bot.py
import os
import discord
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} is now connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, Vsdk madarchod welcome to our server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    sixty_nine = [
         'Nice!!', 'VSDK', 'Hot funeral selfies', 'I slay it, Queen'
    ]
    binayak = ['popat', 'xito udh', 'seliya', 'shellu']
    how_gay = ['sala 100% gay ho yaar ', '100%', 'risheb ta lastai gay ho', 'binayak jati nai gay ho', 'infinitely gay']

    budi = ['Preeti ho preeti', 'Binayak vsdk ho', 'binayak ra risheb honeymoon ma gaisakyo', 'Rekha thapa ho fix', 'mula single nai marxa', 'college ko sab kt haru']

    commands = ['howgay risheb', 'risheb ko budi ko ho', '69', 'roast binayak']
    if message.content == commands[0]:
        response = random.choice(how_gay)
        await message.channel.send(response)

    if message.content == commands[1]:
        response = random.choice(budi)
        await message.channel.send(response)

    if message.content == commands[2]:
        response = random.choice(sixty_nine)
        await message.channel.send(response)

    if message.content == commands[3]:
        response = random.choice(binayak)
        await message.channel.send(response)

    if message.content == 'yo help':
        for i in enumerate(commands):
            await message.channel.send(i)

client.run(TOKEN)
