from http import client
from discord.ext import commands
import discord
import random
from discord.utils import get

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True, # Commands aren't case-sensitive
    intents = intents # Set up basic permissions
)

bot.author_id = 1022113011403604111  # Change to your discord id

intents.presences = True

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx):
    await ctx.send('pong')

@bot.command()
async def name(ctx):
    await ctx.send(ctx.author.name)

@bot.command()
async def d6(ctx):
    await ctx.send(random.randint(1,6))
    
@bot.listen("on_message")
async def on_message(message):
    if message.content == "Salut tout le monde":
            await message.channel.send('Salut tout seul ' + message.author.mention)
            

@bot.command(pass_context=True)
async def admin(ctx, user : discord.Member):    
    role = discord.utils.get(ctx.guild.roles, name="Admin")
    if role == None:
        guild = ctx.guild
        await guild.create_role(name="Admin")
    await user.add_roles(role)

@bot.command()
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)
    

@bot.command()
async def count(ctx):
    List = []
    for member in ctx.guild.members:
        List.append(str(member.status))
        print(str(member.status))
        print(List)
    
    idle = List.count("idle")
    offline = List.count("offline")
    online = List.count("online")
    dnd = List.count("dnd")
    message = str(idle) + " member(s) are idle, " + str(offline) + " member(s) are offline, " + str(online) + " member(s) are online and " + str(dnd) + " members are in Do not Disturb."
    await ctx.send(message)
            
    
    
token = "MTAyMjExMjgzOTM0OTA0MzIzMA.GO4lxS.lHA7mkCDCkrgYlVwyX5EzjXg_t8Ak70mVxYihc"
bot.run(token)  # Starts the bot