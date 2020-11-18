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

    @commands.command()
    async def hornyjail(self, ctx, user: discord.user = None):
        if user is None:
            await ctx.send('Please provide the username of the horny perpetrator!')
            return

        from PIL import Image, ImageDraw, ImageFont
        # get an image
        base = Image.open("Pillow/Tests/images/hopper.png").convert("RGBA")

        # make a blank image for the text, initialized to transparent text color
        txt = Image.new("RGBA", base.size, (255,255,255,0))

        # get a font
        fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 40)
        # get a drawing context
        d = ImageDraw.Draw(txt)

        # draw text, half opacity
        d.text((10,10), "Hello", font=fnt, fill=(255,255,255,128))
        # draw text, full opacity
        d.text((10,60), "World", font=fnt, fill=(255,255,255,255))

        out = Image.alpha_composite(base, txt)

        out.show()




def setup(client):

    client.add_cog(Utils(client))

