from discord.ext import commands

import checks

class Dev:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @checks.is_owner()
    async def eval(self, ctx, *, code):
        """Leaving this command open by accident could possibly result in the heat death of the universe."""
        await ctx.send(f"`{eval(code)}`")

def setup(bot):
    bot.add_cog(Dev(bot))