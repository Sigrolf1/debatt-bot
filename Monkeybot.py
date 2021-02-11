
import discord
from discord import Intents
from discord.utils import get
import pandas as pd
intents = discord.Intents(messages=True, guilds=True, members=True)
import random
from PIL import Image
from discord.ext import commands
from discord import Member
from io import BytesIO

client = commands.Bot(command_prefix="!")


""" @client.command()
async def Wanted(ctx, user: discord.Member = None):
    if not user:
        user = ctx.author
    wanted = Image.open("wanted-poster-old-distressed-western-criminal-template-dead-alive-wanted-background_176411-33.jpg")
    asset = user.avatar_url_as(size = 128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp = pfp.resize((177,177))
    wanted.paste(pfp, (240,424))
    wanted.save("profile.jpg")
    await ctx.send(file = discord.File("profile.jpg")) """

""" @client.command(name="monke sound")
async def monke(ctx):
        # Gets voice channel of message author
    voice_channel = ctx.author.channel
    channel = None
    if voice_channel != None:
        channel = voice_channel.name
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source="C:<path_to_file>"))
        # Sleep while audio is playing.
        while vc.is_playing():
            sleep(.1)
        await vc.disconnect()
    else:
        await ctx.send(str(ctx.author.name) + "is not in a channel.")
        # Delete command after the audio is done playing.
        await ctx.message.delete() """


""" @client.command()
async def spill(context, url : str):
    voiceChannel = discord.utils.get(context.guild_voiceChannel, name = 'chill')
    voice = discord.utils.get(client.voice_clients, guild=context.guild)
    await voiceChannel.connect

 """
















""" @client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 785607459674521603:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        if payload.emoji.name == "monkey_face":
            print("Monkey-role")
            role = discord.utils.get(guild.roles, name = "Monkey-army")

        elif payload.emoji.name == "x":
            print("Rich man Role")
            role = discord.utils.get(guild.roles, name = "3rd-impostor-gang")
        else:
            role = discord.utils.get(guild.roles, name = payload.emoji.name)

        if role is not None:
            member = payload.member
            if member is not None:
                await member.add_roles(role)
                print("done")
            else:
                print("Member not found")
 """

@client.command(pass_context=True, name="ape")
async def join(ctx):
    if ctx.message.author.voice:
        channel = ctx.message.author.voice.channel
        await channel.connect()


@client.command(pass_context=True)
async def leave(ctx):
    if ctx.message.author.voice:
        server = ctx.message.guild.voice_client
        await server.disconnect()


@client.command(name="iq")
async def iq(ctx):
    iq = random.randint(70,155)
    if ctx.author.id == 250262694970523650:
        iq = 69
    if iq < 80:
        myEmbe = discord.Embed(title = "Din iq er", description = f"{iq}", color = 0xADD8E6)
        myEmbe.set_author(name="Lol stupid ass hoe!")
        await ctx.send(embed=myEmbe)

    elif iq > 150:
        myEmbe = discord.Embed(title = "Din iq er", description = f"{iq}", color = 0xADD8E6)
        myEmbe.set_author(name="Fysøren, du e et geni!")
        await ctx.send(embed=myEmbe)
    else:
        myEmbe = discord.Embed(title = "Din iq er", description = f"{iq}", color = 0xADD8E6)
        await ctx.send(embed=myEmbe)



@client.command(name="monkey")
async def randimg(ctx):
    images = ["/Users/sigurdrolfsnes/Desktop/Monkey1.png", "/Users/sigurdrolfsnes/Desktop/Monkey2.png","/Users/sigurdrolfsnes/Documents/Dokumenter – Sigurds MacBook Pro/Discord bot/Monkey/xxtentacionmonke.jpg","/Users/sigurdrolfsnes/Documents/Dokumenter – Sigurds MacBook Pro/Discord bot/Monkey/Monkey12.png","/Users/sigurdrolfsnes/Documents/Dokumenter – Sigurds MacBook Pro/Discord bot/Monkey/Bicyclemonkey.png","/Users/sigurdrolfsnes/Desktop/cursed-monkey-43712629.png", "/Users/sigurdrolfsnes/Desktop/Snapchat-134534640.jpg"]
    random_image = random.choice(images)
    await ctx.send(file=discord.File(random_image))

@client.command(name="wise_monkey")
async def wise_monkey(ctx):
    quote = ["Noen ganger så burde du bare be til monkey-gud!"]
    random_quote = random.choice(quote)
    await ctx.send(random_quote)

""" @client.command(name="monkey_fact")
async def monkey_fact(ctx):
    quote = ["", ""]
    random_quote = random.choice(quote)
    await ctx.send(random_quote) """

@client.command(name="skriv")
async def skriv(ctx, *args):
    general_channel = client.get_channel(748120949567782917)
    try:
        await general_channel.send(" ".join(args))
    except:
        pass




@client.command()
async def pfp(ctx, member: Member = None):
 if not member:
     member = ctx.author
 await ctx.send(member.avatar_url)

word = ["guf", "neger", "nigger", "Neger", "Nigger", "Niggerslayer", "niggerslayer"]


@client.event
async def on_ready():
    """ bot_workshop = client.get_channel(748120949567782917)
    await bot_workshop.send("") """

    """ brukernavn = ["Hjelp!", "Jeg er døende!", "Kan noen gi meg hjerte lungeredning?", "Jeg har ALS", "Min papa blir lei seg hvis jeg dør plz hjelp"]
    random_brukernavn = random.choice(brukernavn)
    await general_channel.send(random_brukernavn)
    await general_channel.send('https://tenor.com/view/dying-monkey-dying-gif-13123180 ') """
    """ myEmbed = discord.Embed(title = "**Choose your fate**", description = " ", color = 0xADD8E6)
    myEmbed.add_field(name = "**Monkey-army**", value = "*React with monkey to become apart of the army*", inline=False)
    myEmbed.add_field(name = "**Monkey-hater**", value = "*React with x to become monkey-hater, fuk u!*", inline=False)
    myEmbed.set_footer(text="Dear monkey-bot")
    myEmbed.set_author(name="Monkey")
    await bot_workshop.send(embed=myEmbed) """


@client.command(name="bøker")
async def version(context):
    myEmbed = discord.Embed(title = "Linker til digitale lærebøker", description = "Linkene med brettboka logger du inn med feide, deretter prøv gratis", color = 0xADD8E6)
    myEmbed.add_field(name = "Mattematikk 1T", value = "https://issuu.com/gyldendalnorskforlag/docs/moenster_1t_bm", inline=False)
    myEmbed.add_field(name = "Engelsk", value = "https://brettboka.no/edushop/products/607", inline=False)
    myEmbed.add_field(name = "Naturfag", value = "https://issuu.com/gyldendalnorskforlag/docs/senit_naturfag_sf_bib_liten", inline=False)
    myEmbed.set_footer(text="Bare klikk på linkene.")
    myEmbed.set_author(name="Monkey")
    await context.message.channel.send(embed=myEmbed)




@client.command(name="matte")
async def Matematikk(context):
    myEmbed = discord.Embed(title = "Matematikk", description = "Diverse digitale verktøy", color = 0x45ffc1)
    myEmbed.add_field(name = "Skolestudio", value = "https://www.skolestudio.no/Monster--Matematikk--11/b927cc05-7e2d-4404-a9b4-2540259712a7--1%20Tall%20og%20regning", inline=False)
    myEmbed.add_field(name = "Smartøving", value = "https://mønster.smartoving.no/student#/choose", inline=False)
    myEmbed.add_field(name = "Smartbok", value = "Eg har ikkje ein link å gi deg", inline=False)
    myEmbed.set_footer(text="Bare klikk på linkene")
    myEmbed.set_author(name="Monkey")
    await context.message.channel.send(embed=myEmbed)


@client.command(name="Vegard")
async def Vegard(context):
    images = ["Nerd_dating.jpg","Skjermbilde 2020-11-30 kl. 14.44.40.png"]
    random_image = random.choice(images)
    await context.send(file=discord.File(random_image))


@client.command(name="india")
async def india(context):
    images = ["india.mp4"]
    random_image = random.choice(images)
    await context.send(file=discord.File(random_image))

@client.command(name="curse")
async def curse(context):
    images = ["video0.mp4"]
    random_image = random.choice(images)
    await context.send(file=discord.File(random_image))

@client.command(name="Wald")
async def Wald(context):
    images = ["61SMGN6mFHL.png"]
    random_image = random.choice(images)
    await context.send(file=discord.File(random_image))

@client.command(name="rødtysker")
async def rødtysker(context):
    images = [""]
    random_image = random.choice(images)
    await context.send(file=discord.File(random_image))

@client.command(name="kanye")
async def kanye(context):
    images = ["Unknown.jpeg"]
    random_image = random.choice(images)
    await context.send(file=discord.File(random_image))

@client.command(name="ål")
async def ål(context):
    images = ["image0.jpg"]
    random_image = random.choice(images)
    await context.send(file=discord.File(random_image))



@client.command(name="sand")
async def Sand(context):
    images = ["Sand.png"]
    random_image = random.choice(images)
    await context.send(file=discord.File(random_image))

@client.command(name="Tuva")
async def Tuva(context):
    images = ["Tuva.png"]
    random_image = random.choice(images)
    await context.send(file=discord.File(random_image))

@client.command(name="lars")
async def lars(context):
    images = ["LARS.jpg"]
    random_image = random.choice(images)
    await context.send(file=discord.File(random_image))

""" @client.event
async def on_message(message):
    if message.author.id == 399269658827423744:
        await message.delete() """
    

""" @client.event
async def on_message(message):
    if message.channel == client.check_channel and any(word in message.content.lower() for word in word) or message.channel == client.check_channel2 and any(word in message.content.lower() for word in word):
        await message.delete()

    general_channel = client.get_channel(539030337997635594)
    if message.content == "india":
        images = ["india.mp4", "video0-79.mp4"]
        random_image = random.choice(images)

        await general_channel.send(file=discord.File(random_image)) """
        
        



client.run("Nzc1NjIzMzU5NTk3NTEwNjY3.X6pBiw.zjG-fVxrhW7iMXYuhZXa3x-LvPw")