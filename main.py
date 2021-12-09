import discord
from discord.ext import commands
from os import listdir


client = commands.Bot(command_prefix='grot ',
                      case_insensitive=True,
                      activity=discord.Game(name="with his plastic dudes"))


for filename in listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        print(f"Cog {filename} loaded.")


@client.event
async def on_command_error(ctx, error):

    # Missing Required Argument
    mra_embd = discord.Embed(
        title="You'z given no argument you buffoon",
        colour=discord.Colour(0x000000),
    )
    mra_embd.set_image(url="https://i.imgur.com/GB9qLol.png")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply(embed=mra_embd, mention_author=False)

    # Bad Argument
    ba_embd = discord.Embed(
        title="Wong argument you bloodey snot",
        colour=discord.Colour(0x000000),
    )
    ba_embd.set_image(url="https://i.imgur.com/GB9qLol.png")
    if isinstance(error, commands.BadArgument):
        await ctx.reply(embed=ba_embd, mention_author=False)


@client.event
async def on_ready():
    print("Grot bot ready!")

with open("token.txt", "r") as token:
    client.run(token.read())
