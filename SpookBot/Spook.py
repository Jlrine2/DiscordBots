import discord
import os

BotID = str(os.getenv(TOKEN))

client = discord.Client()




# on every message
@client.event
async def on_message(message):

    # Do not reply to self

    if message.author == client.user:
        return
    
    if message.content.startswith('/help'):
        await message.channel.send('I will spookify your server with the \
            command `/spookify` and undo that operation with `/unspookify`')

    if str(message.content).startswith('/spookify'):
        try:
            for channel in message.guild.channels:
                holder = channel.name
                if not channel.name.endswith('💀'):
                    holder = holder + '💀'
                if not channel.name.startswith('🎃'):
                    holder = '🎃' + holder
                await channel.edit(name=str(holder))
        except Exception as E:
            await message.channel.send('something went wrong, here is the error:\
                 ' + '\n\n ```\n' + str(E) + '\n```')
        return


    if str(message.content).startswith('/unspookify'):
        try:
            for channel in message.guild.channels:
                holder = channel.name
                holder = holder.replace('💀', '')
                holder = holder.replace('🎃', '')
                await channel.edit(name=str(holder))
        except Exception as E:
            await message.channel.send('something went wrong, here is the error:\
                 ' + '\n ```\n' + str(E) + '\n```')
        return




# on initialization
@client.event
async def on_ready():
    print ('logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')

client.run(BotID)
