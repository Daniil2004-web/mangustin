import discord
import requests
import json
client = discord.Client()

helloArr = ["hello","hi","hh","he"]
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    for arr in helloArr:
        if message.content == arr:
            await message.channel.send("asd")
    if message.content == "погода":
         r = requests.get("http://api.openweathermap.org/data/2.5/weather?q=kurgan&appid=a6756a7aff9564a61122501b4ad92a9b")
         await message.channel.send("r.text")
         jsonData = json.loads(r.text)
    message.channel.send(json["main"]["temp"] - 273.15)
    await message.channel.send(f"{temp} °C" )
@client.event
async def on_message(message):
    print (message)
    if message.author == client.user:
        return

    if message.content  == 'img':

        await message.channel.send(content="asasd", file=discord.File("ror.jpg"))

client.run('ODI3NTAzNjIwODQ0NTUyMjQy.YGb-zQ.4-CLPuRhLCtMxrJvRJzyhg4RER0')
