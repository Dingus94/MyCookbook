import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')

TOKEN = 'XXXSECRETXXX'

@client.event
async def on_ready():
    print('Hello!')

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
