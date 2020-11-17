import discord
from discord.ext import commands

class Events(commands.Cog):

    def __init__(self, client):

        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):

        await self.client.get_channel("""CHANNEL ID""").send(str(member + 'Joined the server!'))

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await self.client.get_channel("""CHANNEL ID""").send(str(member + 'Left the server! :sob:'))

def setup(client):
    client.add_cog(Events(client))
