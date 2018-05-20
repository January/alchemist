import discord


def make_list_embed(fields):
    # Thanks to robingall2910 for this.
    embed = discord.Embed(description="\u200b")
    for key, value in fields.items():
        embed.add_field(name=key, value=value, inline=True)
    return embed
