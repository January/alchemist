from discord.ext import commands

import discord
import checks
import config
import random


class Moderation:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member, *, reason: str="No reason specified."):
        """Show someone the door, optionally with a reason."""
        try:
            await user.send(f"You have been kicked from *{ctx.guild.name}*.\n\n**Reason**: {reason}"
                            f"\n\nKicked by **{ctx.author}**.")
            await ctx.guild.kick(user)
            await ctx.send(f"Kicked `{user}`.")
        except discord.errors.Forbidden:
            if user.top_role.position > ctx.me.top_role.position:
                await ctx.send("**Error**: Can't kick that person. They have a higher role level than me.")
            elif user.top_role.position == ctx.me.top_role.position:
                await ctx.send("**Error**: Can't kick that person. They have the same role level as me.")
            else:
                await ctx.send("**Error**: Permission error. Perhaps I don't have the Kick Members permission.")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member, *, reason: str="No reason specified."):
        """Show someone the door, and lock it, optionally with a reason."""
        try:
            await user.send(f"You have been banned from *{ctx.guild.name}*.\n\n**Reason**: {reason}"
                            f"\n\nBanned by **{ctx.author}**.")
            await ctx.guild.ban(user, delete_message_days=0, reason=reason)
            await ctx.send(f"Banned `{user}`.")
        except discord.errors.Forbidden:
            if user.top_role.position > ctx.me.top_role.position:
                await ctx.send("**Error**: Can't ban that person. They have a higher role level than me.")
            elif user.top_role.position == ctx.me.top_role.position:
                await ctx.send("**Error**: Can't ban that person. They have the same role level as me.")
            else:
                await ctx.send("**Error**: Permission error. Perhaps I don't have the Ban Members permission.")

def setup(bot):
    bot.add_cog(Moderation(bot))