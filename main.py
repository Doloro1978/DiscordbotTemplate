import discord

bot = discord.Bot()

@bot.event
async def on_connect():
    print(f"Connected to Discords servers")

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

# Basic test slash command with "autocorrect" 
@bot.slash_command(guild_ids=[...]) #This shit is ripped out of the wiki
async def hello(
    ctx: discord.ApplicationContext,
    name: discord.Option(str, "Enter your name"),
    age: discord.Option(int, "Enter your age", min_value=1, max_value=99, default=18)
    # passing the default value makes an argument optional
    # you also can create optional argument using:
    # age: Option(int, "Enter your age") = 18
):
    await ctx.respond(f"Hello! Your name is {name} and you are {age} years old.")

@bot.event
async def on_error(x, y, z):
    Doloro = bot.fetch_user(785601303773446184) # This is my user id,
    Doloro.send("The bot darn goofed, " + str(x) + str(y) + str(z))

bot.run("bot")
