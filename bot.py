import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk

bot = commands.Bot(command_prefix='.')

print (discord.__version__)

@bot.event
async def on_ready():
    print ("Ready when you are xd")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)

@bot.command(pass_context=True)
async def helpme(ctx):
    await bot.say("@staff, @Head Staff, He need help!!")
    print ("user has called for help")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
@commands.has_role("Owner")
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="", color=0x00ff00)
    embed.set_author(name="Server Information")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
@commands.has_role("Owner")
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: Cya, {}. Ya loser!".format(user.name))
    await bot.kick(user)

@bot.command(pass_context=True)
@commands.has_role("Owner")
async def ban(ctx, user: discord.Member):
    await bot.say("{}, Is Banned, Bye -_-!".format(user.name))
    await bot.ban(user)

@bot.command(pass_context=True)
@commands.has_role("Owner")
async def unban(ctx, user: discord.Member):
    await bot.say("{}, Is Unbanned welcome him when he joins".format(user.name))
    await bot.revokeban(user)

@bot.command(pass_context=True)
async def buy(ctx):
    embed = discord.Embed(title="test", description="Private message Lone After reading #info.", color=0x00ff00)
    embed.set_footer(text="SeaHub Copyrights!")
    embed.set_author(name="Step 1")
    embed.add_field(name="Step 2", value="Use the paid GUI in #paid-version/ go to the Register tab put your token, And your username and password you will login with, That is it!", inline=True)
    await bot.say(embed=embed)

bot.run("NDU4MDMyMzU1NDYyODczMDg4.DgiE1w.pdU-wlFHkuJRVxc08uvqAe5YNy8")