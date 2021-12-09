import discord
from discord.ext import commands


class WarScroll(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ws(self, ctx):
        author = ctx.author.id
        faction_embd = discord.Embed(
            title="You pick da allienz...",
            colour=discord.Colour(0xffffff),
        )
        faction_embd.add_field(name="Order", value="\u200b", inline=True)
        faction_embd.add_field(name="Death", value="\u200b", inline=True)
        faction_embd.add_field(name="\u200b", value="\u200b", inline=True)
        faction_embd.add_field(name="Chaos", value="\u200b", inline=True)
        faction_embd.add_field(name="Destruction", value="\u200b", inline=True)
        faction_embd.add_field(name="\u200b", value="\u200b", inline=True)
        await ctx.send(embed=faction_embd)

        if author == ctx.message.author.id:
            pass


def setup(client):
    client.add_cog(WarScroll(client))
