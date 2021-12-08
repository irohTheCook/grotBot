import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix='grot ',
                      case_insensitive=True,
                      activity=discord.Game(name="with his plastic dudes"))


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        print(f"Cog {filename} loaded.")


@client.event
async def on_ready():
    print("Grot bot ready!")

with open("token.txt", "r") as token:
    client.run(token.read())
