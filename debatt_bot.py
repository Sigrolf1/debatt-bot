import discord
from discord.ext import commands
import random
from discord import Member
client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    client.check_channel = client.get_channel(795953430325755957)
    client.check_channel2 = client.get_channel(773636554505715726)

@client.command(pass_context=True)
async def join(ctx):
    if ctx.message.author.voice:
        channel = ctx.message.author.voice.channel
        await channel.connect()


@client.command(pass_context=True)
async def leave(ctx):
    if ctx.message.author.voice:
        server = ctx.message.guild.voice_client
        await server.disconnect()

@client.command(name="påstand")
async def wise_monkey(ctx):
    quote = ["Kommunisme er kommunisme", "Kapitalisme er Kapitalisme"]
    random_quote = random.choice(quote)
    await ctx.send(random_quote)

@client.command(name="skriv")
async def skriv(ctx, *args):
    try:
        await ctx.send(" ".join(args))
    except:
        pass

@client.command()
async def pfp(ctx, member: Member = None):
 if not member:
     member = ctx.author
 await ctx.send(member.avatar_url)

word = ["guf", "neger", "nigger", "Neger", "Nigger", "Niggerslayer", "niggerslayer","retard","retard"]

@client.event
async def on_message(message):
    if message.channel == client.check_channel and any(word in message.content.lower() for word in word) or message.channel == client.check_channel2 and any(word in message.content.lower() for word in word):
        await message.delete()
    await client.process_commands(message)
client.run("")