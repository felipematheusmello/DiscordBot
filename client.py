from discord import Client
from config import TOKEN

client = Client()

@client.event
async def on_ready():
    print('logado no {0.user}'.format(client))


client.run(TOKEN)