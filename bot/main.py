import discord

from settings import API_KEY

class Client(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")

    async def on_message(self, message):
        print(f"Message from {message.author}: {message.content}")

client = Client()
client.run(API_KEY)