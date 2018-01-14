#Homemade discord bot by agentcm1

import discord
import random
import math
import time

from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix='#')

Client = discord.Client()

@bot.event
async def on_ready():
    print("Agent's Sweg Bot is online!")
    print("Running on: ",bot.user.name)
    print("Current Bot ID: ",bot.user.id)
    await bot.change_presence(game=discord.Game(name="Say #helpme"))

@bot.async_event
async def on_member_join(Member: discord.User):
    await bot.send_message(Member,"Welcome to the MystGaming Discord! I'm Agent's Sweg Bot, and this is one of my discord. \n This Discord is currently managed by agentcm1#7394 (this bot's creator). \n Rules are: Respect staff descisions \n No abusive launguage \n Hackers aren't welcome \n Ask me before inviting people \n If people are in the recording channel msg them before joining in case you ruin their video \n Please only do bot commands in the bot commands text channel so it doesn't pollute the chat room  \n Have a great time!")
    await bot.send_message(bot.get_channel("170840090535264256"),"Welcome " + Member.name +  " to the Discord! Have a great time here :wink:")

@bot.command(pass_context=True)
async def helpme(ctx):
    await bot.say("This bot uses # \n \n Commands are: \n helpme - get help about the discord. \n coin - flip a coin. \n bored - gives you the link to the bored button website. \n contact - display my contact details. \n rules - read the discord rules.")
    await bot.say("Bot automatically also does new member notifications and DMs!")
@bot.command(pass_context=True)
async def coin(ctx):
    coin = random.randint(0,1)
    if coin == 0:
        await bot.say("Heads")
    else:
        await bot.say("Tails")

@bot.command(pass_context=True)
async def bored(ctx):
    await bot.say("http://boredbutton.com/random")
    
@bot.command(pass_context=True)
async def contact(ctx):
    await bot.say("Details are:")
    await bot.say("YouTube (agentcm1): https://goo.gl/MQxQfc")
    await bot.say("Twitter (@agentcm1): https://twitter.com/agentcm1")
    await bot.say("Email (agentcm1Uk): agentcm1uk@gmail.com")

@bot.command(pass_context=True)
async def rules(ctx):
    await bot.say("Rules are:")
    await bot.say("Respect staff descisions \n No abusive launguage \n No spamming ever \n Hackers aren't welcome \n Ask me before inviting people \n If people are in the recording channel msg them before joining in case you ruin their video \n Please only do bot commands in the bot commands text channel so it doesn't pollute the chat room  \n Have a great time!")

@bot.command(pass_context=True)
async def die(ctx):
    await bot.say("I wouldn't recommend that")

@bot.command(pass_context=True)
async def kys(ctx):
    await bot.say("I wouldn't recommend that")


bot.run("Mzc4MjMzMjI1NjkwMjE4NDk3.DRRq_w.dWBdStxYmue-SV9Ljve-wQpg6m4")
