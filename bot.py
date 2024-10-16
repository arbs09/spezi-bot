import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import random
import requests
import sys
from datetime import datetime, timedelta

start_time = datetime.now()

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

spezi_bilder = [
    "https://www.laweekly.com/wp-content/uploads/2024/07/howies1-759x500.jpg",
    "https://www.laweekly.com/wp-content/uploads/2024/07/L1054819-360x240.jpg",
]

def check_images(image_urls):
    for url in image_urls:
        try:
            response = requests.head(url, allow_redirects=True)
            if response.status_code != 200:
                print(f"Image URL is not available: {url}")
                sys.exit()
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            print(f"Image URL is not available: {url}")
            sys.exit()
    print("All images are available.")

check_images(spezi_bilder)

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
    
    message_content = message.content.lower()

    if "prost" in message_content:
        await message.channel.send("Prost")
        await message.channel.send(random.choice(spezi_bilder))

    if ("ich habe bock auf spezi" in message_content or "ich mag spezi" in message_content or "ich liebe spezi" in message_content):
        await message.channel.send("Ich auch")
        await message.channel.send(random.choice(spezi_bilder))

    if "krombacher spezi" in message_content:
        await message.channel.send("ekelhaft")

    if "hallo" in message_content:
        await message.channel.send("Hallo!")

    await bot.process_commands(message)


@bot.slash_command(name="uptime", description="Check the bot's uptime")
async def uptime(ctx: discord.ApplicationContext):
    current_time = datetime.now()
    uptime = current_time - start_time

    weeks, remainder = divmod(int(uptime.total_seconds()), 604800) 
    days, remainder = divmod(remainder, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    embed = discord.Embed(
        title="PyGuard Uptime",
        description=f"{weeks} weeks, {days} days, {hours} hours, {minutes} minutes, {seconds} seconds",
        color=15363389
    )
    await ctx.respond(embed=embed, ephemeral=True)


bot.run(TOKEN)
