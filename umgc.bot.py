import discord
import cred
from discord.ext import commands
import textwrap

# hidden Discord token
TOKEN = cred.TOKEN

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# command prefix to trigger bot
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel
    welcome_message = textwrap.dedent(f"""Welcome {member.mention} to the {member.guild.name}!
                      Please look at # welcome-and-rules and introduce yourself!.
                      Please let Josh Voyles know if you have sever feedback or problems.
                      ('Contribute to this channels bot here: {cred.GITHUB}""")
    await channel.send(welcome_message)


@bot.command(name='hello', help='Responds with Hello!')
async def say_hello(ctx, member):
    await ctx.send(f'Hello!, {member.mention}')


@bot.command(name='github', help='Responds with its Github address.')
async def show_github(ctx):
    instructios = "\nIf you'd like to join the project, DM Josh Voyles your email indicating you'd like to join."
    await ctx.send(cred.GITHUB + instructios)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user.name}')


bot.run(TOKEN)
