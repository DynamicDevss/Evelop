import discord
import os
import random
from discord.ext import commands

client = commands.Bot(command_prefix=':')


@client.event
async def on_ready():
    print('Successful login as {0.user} Thanks for using Evelop'.format(client))
    await client.change_presence(status=discord.Status.online, activity = discord.Activity(type=discord.ActivityType.watching, name='Your commands'))

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send ('Command not detected.')

@client.command()
async def about(ctx):
    await ctx.send('Hello! My name is Evelop, i was created by: Dynamic Devs. Credits to: Cisaa and Lukas')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run("we're not dumb")