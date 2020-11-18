import discord
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont

# cogs

class Utils(commands.Cog):

    def __init__(self, client):

        self.client = client

    @commands.command()
    async def userinfo(self, ctx, user: discord.User = None):

        if user is None:
            await ctx.send('Please provide a user to get info on!')
            return

        embed = discord.Embed(title = 'Userinfo', description = f'Here is some information about {user.name}', colour = discord.Colour.blue())

        embed.add_field(name = user, value = f'- User\'s name:  {user.name}\n- User\'s ID: {user.id}\n- User\'s discrim: {user.discriminator}\n- User is a bot: {user.bot}', inline = False)

        embed.set_thumbnail(url = user.avatar_url)

        await ctx.send(':wave:', embed = embed)


        out.show()


def setup(client):

    client.add_cog(Utils(client))

