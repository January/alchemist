import discord

import config
import checks
from discord.ext import commands

bot = commands.AutoShardedBot(command_prefix=config.prefix, description="Alchemist Bot", pm_help=None)

extensions = ["cogs.fun",
              "cogs.dev",
              "cogs.function",
              "cogs.moderation"]


@bot.event
async def on_ready():
    print("Logged in as {}#{} ({})\n=============".format(bot.user.name, bot.user.discriminator, bot.user.id))
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print("Error: Couldn't load extension {}\n{}: {}".format(extension, type(e).__name__, e))


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("**Error**: That is not a valid command.")
        return
    if isinstance(error, commands.DisabledCommand):
        await ctx.send("**Error**: This command has been disabled.")
        return
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("**Error**: You do not have permission to use this command.")
        return
    if isinstance(error, checks.owner_only):
        await ctx.send("**Error**: That command can only be used by the bot owner.")
        return
    if isinstance(ctx.channel, discord.DMChannel):
        await ctx.send("**Error**: Sorry, you can't use this bot in a DM.")
        return

bot.run(config.token)