import asyncio
import discord   
from discord.ext import commands
import os
from dotenv import load_dotenv
import Selenium_virtual as sv


load_dotenv()

bot_TKN = os.getenv('BOT_TOKEN') # when accessed online BOT_TOKEN comes from heroku config vars instead of local .env file
server_NAME = os.getenv('SERVER_NAME')
channel_NAME = os.getenv('CHANNEL_NAME')
channel_ID = os.getenv('CHANNEL_ID')

intents = discord.Intents.all()
intents.message_content = True

client = discord.Client(intents=intents)
#|----------------------------------------------------------------------------------------------------------|

@client.event # .event is a decorator which listens to when discord opens, aka the 'client' var
async def on_ready(): # on_ready is a api function tht signals tht a connection with discord has been made

    print(f'{client.user} has connected to Discord!') # f'{}' has same function as .format

@client.event
@commands.has_permissions(send_messages=True, manage_channels=True)
async def on_message(message):

    server = discord.utils.get(client.guilds, name = str(server_NAME))
    soup_channel = discord.utils.get(server.channels, name= channel_NAME)

    soup_channel_id = message.channel.id

    if message.author == client.user:
        return

    if soup_channel_id == channel_ID and 'premade' in message.content.lower():
        await soup_channel.send('Getting ingredients...')
        await sv.custom_process()
        await soup_channel.send(file=discord.File(sv.location))
        await soup_channel.send(sv.result_name)
        await sv.delete()

    if soup_channel_id == channel_ID and 'custom' in message.content.lower():
        await soup_channel.send('Input your ingredients...')
    
    if soup_channel_id == channel_ID and 'clear' in message.content.lower():
        await message.channel.send('clearing...')
        await asyncio.sleep(3)
        await message.channel.purge()
    
    # if soup_channel_id == int(channel_ID) and 'retard' in message.content.lower():
    #     members = []
    #     await message.channel.send('clearing...')

#|----------------------------------------------------------------------------------------------------------|
client.run(bot_TKN) # This is run followed by ---^