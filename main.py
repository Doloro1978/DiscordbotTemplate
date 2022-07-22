import discord

bot = discord.Bot()

@bot.event
async def on_connect():
    print(f"Connected to Discords servers")

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

bot.run("bot")