import discord   
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

bot_TKN = os.getenv('BOT_TOKEN') # when accessed online BOT_TOKEN comes from heroku config vars instead of local .env file
server_NAME = os.getenv('SERVER_NAME')
channel_NAME = os.getenv('CHANNEL_NAME')

intents = discord.Intents.all()
intents.message_content = True

client = discord.Client(intents=intents)
#|----------------------------------------------------------------------------------------------------------|



@client.event # .event is a decorator which listens to when discord opens, aka the 'client' var        
@commands.has_permissions(send_messages=True)     
async def on_ready(): # on_ready is a api function tht signals tht a connection with discord has been made

    server = discord.utils.get(client.guilds, name = server_NAME)
    soup_channel = discord.utils.get(server.channels, name= channel_NAME)

    print(f'{client.user} has connected to Discord!') # f'{}' has same function as .format
    await soup_channel.send('https://www.inspiredtaste.net/wp-content/uploads/2018/09/Easy-Chicken-Noodle-Soup-Recipe-1200.jpg')

# @client.event
# @commands.has_permissions()
# async def on_message(message):
    
#|----------------------------------------------------------------------------------------------------------|
client.run(bot_TKN) # This is run followed by ---^