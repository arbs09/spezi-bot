import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import random

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

spezi_bilder = [
    "Link for Image",
]

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    activity = discord.Game(name="mit Spezi", type=3)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print('------')
    print("Guilds and Member Counts:")
    for guild in bot.guilds:
        print(f"{guild.name} ({guild.id}) - {guild.member_count} members")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if "Prost" in message.content:
        await message.channel.send("Prost")

    if "Spezi" in message.content:
        random_spezi_image = random.choice(spezi_bilder)
        await message.reply(random_spezi_image)

    await bot.process_commands(message)

bot.run(TOKEN)
