from await import await
from discord.ext.commands import Bot
import asyncio
import markovify
import cat
import aiohttp
import requests
import time
import os
import discord
from twitter import *



t = Twitter(auth=OAuth("token", "token_secret", "consumer_key", "consumer_secret"))








AustinBot = Bot(command_prefix="$")


@AustinBot.event
async def on_ready():
    print("Client logged in")


@AustinBot.command()
async def twitterdirect(message, messages):
    return t.direct_messages.new(
    user=message,
    text=messages)

@AustinBot.command()
async def twitter(messages):
    return t.statuses.update(
    status=messages)

@AustinBot.command()
async def hg(*args):
    return await AustinBot.say("you a homo gay")




@AustinBot.command()
async def homo(*args):
    return await AustinBot.say("homosexuals are gay")

@AustinBot.command(pass_context=True)
async def cat(*args):
    catPicture = requests.get('thecatapi.com API KEY HERE')
    embed6=discord.Embed(
        title=catPicture.url, color=0x1f903f)
    try:
        return await AustinBot.say(catPicture.url)
    except Exception:
        pass

@AustinBot.command()
async def markov(*Args):
    with open("path to textfile", encoding="utf8") as f:
        text = f.read()

        text_model = markovify.Text(text, state_size=2)
    try:
        return await AustinBot.say(text_model.make_sentence(tries=50, max_overlap_total=8, max_overlap_ratio=0.6, char_limit=200))
    except Exception:
        pass

@AustinBot.command()
async def dice(*args):
    import random
    cards = ['1', '2', '3', '4', '5', '6']
    return await AustinBot.say("You rolled a {}!".format(random.choice(cards)))

@AustinBot.command()
async def chicken(*args):
    return await AustinBot.say("🐔 BRaWK")

@AustinBot.command()
async def rr(*args):
    import random
    RR=["💥🔫 ***Bang!*** You died!", "***Click*** You lived."]
    return await AustinBot.say(random.choice(RR))



AustinBot.run("discord-api-key-thing-here")