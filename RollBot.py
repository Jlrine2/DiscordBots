import discord, random, re

#open config file
config_file = open("RollBot.Config", "r")

#get token value without new line
BotID = config_file.readline().split(": ")[1].rstrip('\r\n')

#comment

client = discord.Client()

#roll a random dice of n value
def roll(n):
    return random.randint(1, n)

#retrieve the n value for a dice roll from message
def get_die(text):
    rollstr = re.findall('/roll d\d+',text)
    die = re.findall('\d+',rollstr[0])
    return die[0]




#on every message
@client.event
async def on_message(message):

    #Do not reply to self

    if message.author == client.user:
        return

    if '/roll' in message.content:
        die = get_die(message.content)
        print(die)
        await client.send_message(message.channel, 'Rolling d' + str(int(die)) + '... result: ' + str(roll(int(die))))
        return


#on initialization
@client.event
async def on_ready():
    print ('logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')

client.run(BotID)