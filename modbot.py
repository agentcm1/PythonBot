import discord

from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix='#')

Client = discord.Client()

@bot.event
async def on_ready():
    print("Agent's Mod Bot is online!")
    print("Running on: ",bot.user.name)
    print("Current Bot ID: ",bot.user.id)
    await bot.change_presence(game=discord.Game(name="Watch out... -_-"))

@bot.event
async def on_message(message):
    if message.content.startswith("fuck"):
        await bot.send_message(message.channel, "WATCH YOUR PROFANITY")
        await bot.send_message(message.channel, "Moderator was notified")
        await bot.send_message(bot.get_channel("391968369005428737"), "@agentcm1, Somebody swore in one of the channels!")
    elif message.content.startswith("crap"):
        await bot.send_message(message.channel, "WATCH YOUR PROFANITY")
        await bot.send_message(message.channel, "Moderator was notified")
        await bot.send_message(bot.get_channel("391968369005428737"), "@agentcm1, Somebody swore in one of the channels!")
    elif message.content.startswith("cunt"):
        await bot.send_message(message.channel, "WATCH YOUR PROFANITY")
        await bot.send_message(message.channel, "Moderator was notified")
        await bot.send_message(bot.get_channel("391968369005428737"), "@agentcm1, Somebody swore in one of the channels!")
    elif message.content.startswith("shit"):
        await bot.send_message(message.channel, "WATCH YOUR PROFANITY")
        await bot.send_message(message.channel, "Moderator was notified")
        await bot.send_message(bot.get_channel("391968369005428737"), "@agentcm1, Somebody swore in one of the channels!")
    elif message.content.startswith("faggot"):
        await bot.send_message(message.channel, "WATCH YOUR PROFANITY")
        await bot.send_message(message.channel, "Moderator was notified")
        await bot.send_message(bot.get_channel("391968369005428737"), "@agentcm1, Somebody swore in one of the channels!")
    elif message.content.startswith("kys"):
        await bot.send_message(message.channel, "WATCH YOUR PROFANITY")
        await bot.send_message(message.channel, "Moderator was notified")
        await bot.send_message(bot.get_channel("391968369005428737"), "@agentcm1, Somebody swore in one of the channels!")
    elif message.content.startswith("arse"):
        await bot.send_message(message.channel, "WATCH YOUR PROFANITY")
        await bot.send_message(message.channel, "Moderator was notified")
        await bot.send_message(bot.get_channel("391968369005428737"), "@agentcm1, Somebody swore in one of the channels!")
    elif message.content.startswith("dick"):
        await bot.send_message(message.channel, "WATCH YOUR PROFANITY")
        await bot.send_message(message.channel, "Moderator was notified")
        await bot.send_message(bot.get_channel("391968369005428737"), "@agentcm1, Somebody swore in one of the channels!")
    elif  message.content.startswith("nigger"):
        await bot.send_message(message.channel, "WATCH YOUR PROFANITY")
        await bot.send_message(message.channel, "Moderator was notified")
        await bot.send_message(bot.get_channel("391968369005428737"), "@agentcm1, Somebody swore in one of the channels!")
    elif message.content.endswith("fuck"):
        await bot.send_message(message.channel, "WATCH YOUR PROFANITY")
        await bot.send_message(message.channel, "Moderator was notified")
        await bot.send_message(bot.get_channel("391968369005428737"), "@agentcm1, Somebody swore in one of the channels!")
    elif message.content.endswith("cunt"):
        await bot.send_message(message.channel, "WATCH YOUR PROFANITY")
        await bot.send_message(message.channel, "Moderator was notified")
        await bot.send_message(bot.get_channel("391968369005428737"), "@agentcm1, Somebody swore in one of the channels!")
    elif message.content.endswith("shit"):
        await bot.send_message(message.channel, "WATCH YOUR PROFANITY")
        await bot.send_message(message.channel, "Moderator was notified")
        await bot.send_message(bot.get_channel("391968369005428737"), "@agentcm1, Somebody swore in one of the channels!")
    elif message.content.endswith("faggot"):
        await bot.send_message(message.channel, "WATCH YOUR PROFANITY")
        await bot.send_message(message.channel, "Moderator was notified")
        await bot.send_message(bot.get_channel("391968369005428737"), "@agentcm1, Somebody swore in one of the channels!")
    elif message.content.endswith("kys"):
        await bot.send_message(message.channel, "WATCH YOUR PROFANITY")
        await bot.send_message(message.channel, "Moderator was notified")
        await bot.send_message(bot.get_channel("391968369005428737"), "@agentcm1, Somebody swore in one of the channels!")
    elif message.content.endswith("arse"):
        await bot.send_message(message.channel, "WATCH YOUR PROFANITY")
        await bot.send_message(message.channel, "Moderator was notified")
        await bot.send_message(bot.get_channel("391968369005428737"), "@agentcm1, Somebody swore in one of the channels!")
    elif message.content.endswith("dick"):
        await bot.send_message(message.channel, "WATCH YOUR PROFANITY")
        await bot.send_message(message.channel, "Moderator was notified")
        await bot.send_message(bot.get_channel("391968369005428737"), "@agentcm1, Somebody swore in one of the channels!")
    elif  message.content.endswith("nigger"):
        await bot.send_message(message.channel, "WATCH YOUR PROFANITY")
        await bot.send_message(message.channel, "Moderator was notified")
        await bot.send_message(bot.get_channel("391968369005428737"), "@agentcm1, Somebody swore in one of the channels!")    
    elif message.content.endswith("crap"):
        await bot.send_message(message.channel, "WATCH YOUR PROFANITY")
        await bot.send_message(message.channel, "Moderator was notified")
        await bot.send_message(bot.get_channel("391968369005428737"), "@agentcm1, Somebody swore in one of the channels!")
    elif message.content.endswith("gay"):
        await bot.send_message(message.channel, "EXPOSED")
    elif message.content.endswith("bot is rubbish"):
        await bot.send_message(message.channel, "you hurt my feelings :cry:")
    elif message.content.endswith("bot sucks"):
        await bot.send_message(message.channel, "you hurt my feelings :cry:")
    
bot.run("MzkxOTU2MTgzNjEyOTE1NzEz.DRgNKw.7LL6TIABluPNRkxY2HfMsAw-EkM")
