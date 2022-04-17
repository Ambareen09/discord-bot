from http import client
import discord
import requests
import os
import json

from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

bot = discord.Client()


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)


@bot.event
async def on_ready():
    guild_count = 0

    for guild in bot.guilds:
        print(f"- {guild.id} (name: {guild.name})")

        guild_count = guild_count + 1

    print("SampleDiscordBot is in " + str(guild_count) + " guilds.")


@bot.event
async def on_message(message):
    if message.content.lower() == "hello" or message.content.lower() == "hi":
        await message.channel.send(f"Hey there {message.author.mention}!")

    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

bot.run(DISCORD_TOKEN)
