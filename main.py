import discord
class MyClient(discord.Client):
    message_storage = []
    async def on_ready(self): # <-- on_ready Event
        print('Logged on as {0}!'.format(self.user)) # print statement to show it logged in

    async def on_message(self, message): # <-- on_message Event 
        print('Message from {0.author}: {0.content}'.format(message)) # A little print statement to show that the bot can read the messages
        message_storage = []
        if message.author.bot == False: # Check if the message sent was from a bot or not (It will not reply to a bot)
            if message.content == "Ping": #Checks to see if the message sent is "Ping"
                print("The bot should say Pong") # <-- This is meant for debugging reasons
                await message.channel.send("Pong") # Sents a message with the content "Pong"

            if message.content == "Pong": #Checks to see if the message sent is "Pong"
                print("The bot should say Pong") # <-- This is meant for debugging reasons
                await message.channel.send("Ping") # Sents a message with the content "Ping"

            if message.content == "Reply": #Checks to see if the message sent is "Reply"
                print("The bot should add a reaction onto the message") # <-- This is meant for debugging reasons
                await message.reply("I have replied") # It replys to that message

            if message.content == "Pin me": #Checks to see if the message sent is "Pin me"
                print("The bot should pin this message")
                await message.pin() # pins that message
                f = open("message_storage.txt", "w")
                f.write(str(message.id))
                f.close


client = MyClient() 
client.run('ODI5ODA3MzMzNTcwNzczMDgz.GVo7ci.CLvC_FWxx2O6_otQSQR6JfbHmxf-_iubfo0LII')
