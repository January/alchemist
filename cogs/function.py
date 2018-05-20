from discord.ext import commands

class Function:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def notetoself(self, ctx, note):
        """Send a note to yourself."""
        await ctx.author.send(note)
        await ctx.send(":pencil: Note sent.")

    @commands.command()
    async def ping(self, ctx):
        """Ping."""

        s = await ctx.send("Please wait... if you're still reading this, something's probably gone wrong")

        p = self.bot.latency * 1000

        await s.edit(content=f"Pong! `{p:.1f}ms`")

def setup(bot):
    bot.add_cog(Function(bot))