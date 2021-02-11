import discord
from discord.ext import commands
import random
import json 
import os

client = commands.Bot(command_prefix="!")

@client.command()
async def open_account(user):
    new_user = str({str(user.id): {"wallet": 0, "bank": 0}})
    with open("/Users/sigurdrolfsnes/Documents/Discord bot/Discord bot/Bank.json","w") as f:
        f.write(new_user)
        
async def get_bank_data():
    with open("Bank.json","r") as f:
        users = json.load(f)
    return users

client.run("NzczNjQ4MTMwMjEwMDA1MDEy.X6MR9w.ILL3CEIbBrRU18A51PoVd33PrNg")

