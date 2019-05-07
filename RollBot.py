import discord
import random
import re

# open config file
config_file = open("RollBot.Config", "r")

# get token value without new line
BotID = config_file.readline().split(": ")[1].rstrip('\r\n')

# comment

client = discord.Client()

# roll a random dice of n value


def roll(n):
    return random.randint(1, n)


# on every message
@client.event
async def on_message(message):

    # Do not reply to self

    if message.author == client.user:
        return

    if str(message.content).startswith('/roll'):
        for die in re.findall('d\d+', message.content):
            num = re.findall('\d+', die)[0]
            send = 'Rolling d' + str(int(num)) + '... result: ' + str(roll(int(num)))
            await message.channel.send(send)
        return




# on initialization
@client.event
async def on_ready():
    print ('logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')

client.run(BotID)
