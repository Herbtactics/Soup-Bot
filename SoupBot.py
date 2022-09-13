import discord   
from discord.ext import commands
import os
from dotenv import load_dotenv # for loading stuff from the .env file

load_dotenv()

bot_TKN = os.getenv('BOT_TOKEN')
CHANNELID = os.getenv('_CHANNELID')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
#|----------------------------------------------------------------------------------------------------------|

@client.event # .event is a decorator which listens to when discord opens, aka the 'client' var             
async def on_ready(): # on_ready is a api function tht signals tht a connection with discord has been made  
    print(f'{client.user} has connected to Discord!') # f'{}' has same function as .format

# @client.event
# @commands.has_permissions()
# async def on_message(message):
    
#|----------------------------------------------------------------------------------------------------------|
client.run(bot_TKN) # This is run followed by ---^