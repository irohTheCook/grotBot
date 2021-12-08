from discord.ext import commands
from random import randint


class DiceRoll(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.emoji_d6 = {
            1: "<:d6_1:852225703427833856>",
            2: "<:d6_2:852224034783363113>",
            3: "<:d6_3:852224035261513728>",
            4: "<:d6_4:852224034888613940>",
            5: "<:d6_5:852224034971320321>",
            6: "<:d6_6:852225703458111508>",
        }

    @commands.command()
    async def roll(self, ctx, number=1):
        rolls = []
        if 0 < number <= 60:
            for _ in range(number):
                rolls.append(randint(1, 6))
            rolls.sort()
            msg = "You'z rolled: "

            prev = None
            for roll in rolls:
                if prev != roll:
                    msg += '\n'
                msg += self.emoji_d6[roll]
                prev = roll
            await ctx.send(msg)
        else:
            await ctx.send("I haz 60 dice, no more, no less.")


def setup(client):
    client.add_cog(DiceRoll(client))
