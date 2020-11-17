import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')

TOKEN = 'XXXSECRETXXX'

cogs = ['cogs.events', 'cogs.utils']

for cog in cogs:
    try:
        client.load_extension(cog)
    except Exception as e:
        print(f'Could not load cog {cog}:{str(e)}')

@client.event
async def on_ready():
    print('Hello!')

@client.command()
async def loadcog(ctx, cogname = None):

    if cogname is None:
        return

    try:
        client.load_extension(cogname)
    except Exception as e:
        print(f'Could not load cog{cogname}: {str(e)}')
    else:
        print('Laded Cog Succesfully')

@client.command()
async def unloadcog(ctx, cogname = None):

    if cogname is None:
        return

    try:
        client.unload_extension(cogname)
    except Exception as e:
        print(f'Could not unload cog{cogname}: {str(e)}')
    else:
        print('unloaded Cog Succesfully')

@client.command()
async def ping(ctx):

    await ctx.send(':ping_pong: Pong!')

@client.command()
async def say(ctx, *, message = None):

    if message == None:
        await ctx.send('Please provide a message!')
        return

    await ctx.send(message)

@client.command()
async def roleinfo(ctx, role: discord.User):

    await ctx.send(role.id)

@client.command()
async def multi(ctx, role: discord.Role, user: discord.User):

    await ctx.send(role.id)
    await ctx.send(user.id)


client.run(TOKEN)
