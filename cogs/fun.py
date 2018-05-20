from discord.ext import commands

import checks
import config
import random


class Fun:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @checks.is_owner()
    async def say(self, ctx, *, message: str):
        """Test command, this probably will not stay"""
        try:
            await ctx.message.delete()
        except:
            pass
        if ctx.author is not ctx.author.bot:
            await ctx.send(message)
        else:
            return

    @commands.command(aliases=['rand'])
    async def random(self, ctx, min, max):
        """Generates a random number in a user-specified range."""
        if min > max:
            await ctx.send("**Error**: `min > max`.")
            return

        if min < -1e100 or max > 1e100:
            return await ctx.send("**Error**: That number is too big. (outside `[-1e100, 1e100]`).")

        rand_num = random.randint(min, max)
        await ctx.send(f"How does {rand_num} sound?")

def setup(bot):
    bot.add_cog(Fun(bot))