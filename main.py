import discord
from discord.ext import commands
import requests #allows to make http requests
import json #as the API returns json
import random
import os
from keep_alive import keep_alive



client=discord.Client()

sad= ["sad", "depressed", "unhappy", "exhausted"]

starter_enc=["Cheer up! Tomorrow is another chance", "Just take a deep breath.", "You are a great person !", "It's just a bad day not a bad life.", "Life is better when you are laughing!", "Tough time don't last, tough people do."]

def getquote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q']+" ~"+json_data[0]['a']
    return(quote)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author==client.user:
        return
    
    #msg= message.content
    if message.content.startswith('$ping') or message.content.startswith('$Ping'):
        await message.channel.send(f"Pong! {round(client.latency * 1000)}ms")
    if message.content.startswith('$help'):
        myEmbed = discord.Embed(title= 'Here are my list of commands', color=discord.Color.green(), description="$inspire\n$hello\n$goodnight")
        await message.channel.send(embed=myEmbed)
    if message.content.startswith('$hello') or message.content.startswith('$Hello'):
        await message.channel.send('Holaaa!')
    if message.content.startswith('$bye') or message.content.startswith('$goodnight'.lower()):
        await message.channel.send('Sayonara <3')
    if message.content.startswith('$inspire') or message.content.startswith('$Inspire'):
        quote=getquote()
        await message.channel.send(quote)
    async def inspire(context):
       if message.content.startswith('$help'):
        myEmbed = discord.Embed(title= 'Here are my list of commands', color=discord.Color.green(), description="$inspire\n$hello\n$goodnight")
        await context.message.channel.send(embed=myEmbed)
    await client.process_commands(message)
    if any(word in msg for word in sad):
        #await message.channel.send(random.choice(starter_enc))

keep_alive()
client.run(os.environ.get("TOKEN"))
