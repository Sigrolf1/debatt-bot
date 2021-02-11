#Import Discord Package

import discord
from discord import Intents
from discord.utils import get
import pandas as pd
intents = discord.Intents(messages=True, guilds=True, members=True)
import random
import json 
import os
from discord.ext import commands


#Prefixen
client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    client.check_channel = client.get_channel(773823760494100481)
    client.check_channel2 = client.get_channel(773636554505715726)

@client.command(name="reaction_create_post")
async def reaction_create_post(context):
    
    myEmbed= discord.Embed(title = "Arena Champs RPG", description = "", color = 0xffff00)
    myEmbed.add_field(name = "What is it?", value = "Arena champs RPG is an interactive fun (osv).........", inline=False)
    myEmbed.add_field(name = "How it works: ", value = "It works in .................", inline=False)
    myEmbed.set_footer(text="Have any questions? Contact @Developer")
    myEmbed.set_author(name="RPG-bot")
    await context.message.channel.send(embed=myEmbed)






word = ["guf", "neger", "nigger", "Neger", "Nigger", "Niggerslayer", "niggerslayer"]
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

@client.command(name="Skriv" or "skriv")
async def skriv(ctx, *args):
    try:
        await ctx.send(" ".join(args))
    except:
        pass

@client.command(name="info")
async def version(context):
    myEmbed= discord.Embed(title = "Arena Champs RPG", description = "", color = 0xffff00)
    myEmbed.add_field(name = "What is it?", value = "Arena champs RPG is an interactive fun (osv).........", inline=False)
    myEmbed.add_field(name = "How it works: ", value = "It works in .................", inline=False)
    myEmbed.set_footer(text="Have any questions? Contact @Developer")
    myEmbed.set_author(name="RPG-bot")
    await context.message.channel.send(embed=myEmbed)

@client.command()
async def addrole(ctx, role: discord.Role, user: discord.Member):
        await user.add_roles(role)
        await ctx.send(f"Vellykket lagt {user.mention} til i {role.mention}.")
        print("Koden kjørte")

@client.command(name="monkey" or "Monkey")
async def randimg(context):
    images = ["Monkey/Monkey1.jpg", "Monkey/Monkey2.jpg", "Monkey/Monkey3.jpg", "Monkey/Monkey4.jpg", "Monkey/Monkey5.jpg", "Monkey/Monkey6.jpg", "Monkey/Monkey7.jpeg", "Monkey/Monkey8.jpeg", "Monkey/Monkey9.jpg", "Monkey/Monkey10.png"]
    
    random_image = random.choice(images)

    await context.send(file=discord.File(random_image))

@client.command()
async def removerole(ctx, role: discord.Role, user: discord.Member):
        await user.remove_roles(role)
        await ctx.send(f"Vellykket fjernet {role.mention} fra {user.mention}.")
        print("Koden kjørte")
        
@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 774706294484369419:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        if payload.emoji.name == "Duelist":
            print("Duelist Role")
            role = discord.utils.get(guild.roles, name = "Duelist")

        elif payload.emoji.name == "Richman":
            print("Rich man Role")
            role = discord.utils.get(guild.roles, name = "Richman")
        else:
            role = discord.utils.get(guild.roles, name = payload.emoji.name)

        if role is not None:
            member = payload.member
            if member is not None:
                await member.add_roles(role)
                print("done")
            else:
                print("Member not found")


@client.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 774706294484369419:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        if payload.emoji.name == "Duelist":
            role = discord.utils.get(guild.roles, name="Duelist")
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            await member.remove_roles(role)
        if payload.emoji.name == "Richman":
            role = discord.utils.get(guild.roles, name="Richman")
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if role != None:
                await member.remove_roles(role)


""" @client.event
async def on_raw_reaction_remove(payload):
    intents = discord.Intents.all()
    client = discord.Client(intents=intents)
    message_id = payload.message_id
    if message_id == 774706294484369419:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : jg.id == guild_id, client.guilds)

        if payload.emoji.name == "Duelist":
            print("Duelist Role")
            role = discord.utils.get(guild.roles, name = "Duelist")

        elif payload.emoji.name == "Richman":
            print("Rich man Role")
            role = discord.utils.get(guild.roles, name = "Richman")
        else:
            role = discord.utils.get(guild.roles, name = payload.emoji.name)

        if role is not None:
            member = payload.member
            if member is not None:
                await member.remove_roles(role)
                print("Ferdig")
            else:
                print("Member not found")
        else:
            print("Role not found.") """

@client.command(name="emoji")
async def on_reaction_add(ctx, reaction):
    if reaction.lower() == "😄":
        await ctx.send("Are you happy?")
    elif reaction.lower() == "🤣":
        await ctx.send("Why you laughing bro?")
    elif reaction.lower() == "😭":
        await ctx.send("Why you crying you pussy!")
    else:
        await ctx.send("This not working bro")

    """ await ctx.send('{} har blitt lagt til i {}'.format(ctx.message.author, reaction)) """



@client.event
async def on_message(message):
    
    if message.content == "Arena champs info":
        general_channel = client.get_channel(773636554505715726)
        
        myEmbed= discord.Embed(title = "Arena Champs RPG", description = "", color = 0xffff00)
        myEmbed.add_field(name = "What is it?", value = "Arena champs RPG is an interactive fun (osv).........", inline=False)
        myEmbed.add_field(name = "How it works: ", value = "It works in .................", inline=False)
        myEmbed.set_footer(text="Have any questions? Contact @Developer")
        myEmbed.set_author(name="RPG-bot")

        await general_channel.send(embed=myEmbed)
    if message.content == "RPG info":
        await message.author.send("Im here to tell you how it works")
    if message.content == "Rank":
        await message.author.send("Congratulations you have ranked up!")
    
    if message.content == "Hp":
        #Add a row to my dataframe that contains the message
        df = pd.read_csv("/Users/sigurdrolfsnes/Documents/Discord bot/Discord bot/output.csv", index_col=0)
        df = df.append({"A":"Your health is 100"},ignore_index=True)
        df.to_csv("/Users/sigurdrolfsnes/Documents/Discord bot/Discord bot/output.csv")
    await client.process_commands(message)


    if message.channel == client.check_channel and any(word in message.content.lower() for word in word) or message.channel == client.check_channel2 and any(word in message.content.lower() for word in word):
        await message.delete()

    """ if message.author.id == 163002821430607872:
        await message.delete() """

#Run client
client.run("NzczNjQ4MTMwMjEwMDA1MDEy.X6MR9w.ILL3CEIbBrRU18A51PoVd33PrNg")