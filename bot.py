import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import random
import requests
import sys

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

spezi_bilder = [
    "https://cdn.discordapp.com/attachments/847193443411165214/1230953424078770276/photo_2024-04-19_20-49-09.jpg?ex=669b5df6&is=669a0c76&hm=92f1322f79f82c89cb91a8f859cb563ab10d18fc356f34b4a004821503c9e5e2&",
    "https://cdn.discordapp.com/attachments/847193443411165214/1201246964344442930/e4c81853-5c14-4e54-ab52-80f7dabe2017.png?ex=669b66aa&is=669a152a&hm=05daa06f15696828c7dfa7e2152bafd24bc11706c2e041f9a929b9206a0857c9&",
    "https://cdn.discordapp.com/attachments/847193443411165214/1185200744916336660/IMG_3976.jpg?ex=669b0875&is=6699b6f5&hm=636bfbe4bf20cecae8912c8bed96e47bada8790b488733d1aa18e1c6087345ff&",
    "https://cdn.discordapp.com/attachments/847193443411165214/1096143281567576164/IMG_20230413_204051.jpg?ex=669b5c3b&is=669a0abb&hm=20d2d387d8d8bf6d49427b6d8e94f6342b4d308324056683cf177a29142a4fad&",
    "https://cdn.discordapp.com/attachments/847193443411165214/1092516239374569522/20230403_202606.jpg?ex=669b5949&is=669a07c9&hm=f120d2abd3873879afdd3d56fd2f17d2c4a5987d9d911209aa170d61233a7905&",
    "https://www.laweekly.com/wp-content/uploads/2024/07/howies1-759x500.jpg",
    "https://www.laweekly.com/wp-content/uploads/2024/07/L1054819-360x240.jpg",
    "https://i.ibb.co/vH8GbsJ/IMG-20240719-123618422.jpg",
    "https://i.ibb.co/k3jGrnR/IMG-20240719-122815563.jpg",
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

    await bot.process_commands(message)


bot.run(TOKEN)
