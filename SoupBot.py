import discord      
from discord.ext import commands
import os
from dotenv import load_dotenv # for loading stuff from the .env file

load_dotenv() # can now get access to stuff from .env file

bot_TKN = os.getenv('BOT_TOKEN')

intents = discord.Intents.default() # line 16/17/19 is setup bs idk wtf it is for
intents.message_content = True

client = discord.Client(intents=intents)

#|----------------------------------------------------------------------------------------------------------|

@client.event # .event is a decorator which listens to when discord opens, aka the 'client' var             
async def on_ready(): # on_ready is a api function tht signals tht a connection with discord has been made  
    print(f'{client.user} has connected to Discord!') # f'{}' has same function as .format
    
#|----------------------------------------------------------------------------------------------------------|
client.run(bot_TKN) # This is run followed by ---^