import discord
import cred
from discord.ext import commands

TOKEN = cred.TOKEN

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# command prefix to trigger bot
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.command(name='hello', help='Responds with Hello!')
async def hello(ctx):
    await ctx.send('Hello!')


@bot.event
async def on_member_join(member):
    guild = member.guild
    channel = bot.get_channel(cred.MEMBER_LANDING)
    welcome_message = f'Welcome {member.mention} to the {guild.name}!\n\n' + \
                      ('Please look at #welcome-and-rules but refrain from '
                       'posting there.') + \
                      ('\nPlease let Josh Voyles know if you have sever '
                       'feedback or problems.\n') + \
                      ('Contribute to this channels bot here: '
                       'https://github.com/Josh-Voyles/UMGC-Discord-Bot')
    await channel.send(welcome_message)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user.name}')


bot.run(TOKEN)
