import discord

class MyClient(discord.Client):
    async def on_ready(self): # <-- on_ready Event
        print('Logged on as {0}!'.format(self.user)) # print statement to show it logged in

    async def on_message(self, message): # <-- on_message Event 
        print('Message from {0.author}: {0.content}'.format(message)) # A little print statement to show that the bot can read the messages 
        if message.author != 829807333570773083: #Stops the bot replying to itself
            if message == "Ping": #Checks to see if the message sent is "Ping"
                await message.channel.send("Pong") # Replys with "Pong"

            if message == "Pong": #Checks to see if the message sent is "Pong"
                await message.channel.send("Ping") # Replys with "Ping"

            

client = MyClient() 
client.run('ODI5ODA3MzMzNTcwNzczMDgz.GmD5Fq.b7M-WGB_r1plWjld_X0to2ojeIAHJZkokhhIrI')