import os
import random
import re

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

client = discord.Client() 

@client.event
async def on_ready():

    print(f"{client.user} has connected to Discord!")

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f"{client.user} is connected to the following guild:\n"
        f"{guild.name}(id: {guild.id})"
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    betty_white_quotes = [
        "Kindness and consideration of somebody besides yourself keeps you feeling young.",
        "I have no regrets at all. None. I consider myself to be the luckiest old broad on two feet.",
        "Everybody needs a passion. That’s what keeps life interesting. If you live without passion, you can go through life without leaving any footprints.",
        "About being called a “legend:” “I just laugh. Have I got them fooled.” —On a CNN interview with Joy Behar",
        "Retirement is not in my vocabulary. They aren’t going to get rid of me that way.",
        "I’m a health nut. My favorite food is hot dogs with French fries. And my exercise: I have a two-story house and a very bad memory, so I’m up and down those stairs.",
    ]
    pattern = "(?i)[^.]*(Betty White)[^.]*(.)?"
    result = re.match(pattern, message.content)
    if result:
        response = random.choice(betty_white_quotes)
        await message.channel.send(
            response,
            file=discord.File(
                random.choice(
                    (
                        "images/img1.jpg",
                        "images/img2.jpg",
                        "images/img3.jpg",
                        "images/img4.jpg",
                    )
                )
            ),
        )


client.run(TOKEN)
