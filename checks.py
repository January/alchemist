import discord
import config

from discord.ext import commands


class owner_only(commands.CommandError):
    pass


def is_owner():
    def predicate(ctx):
        if ctx.author.id == int(config.owner_id):
            return True
        else:
            raise owner_only
    return commands.check(predicate)