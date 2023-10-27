import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# Replace YOUR_CREATOR_ID with the actual ID of the bot's creator
CREATOR_ID = YOUR_CREATOR_ID

@client.event
async def on_ready():
    print(f'Bot {client.user} is ready')

@client.event
async def on_message(message):
    # Check if the message is not from the bot and the sender is the creator
    if message.author != client.user and message.author.id == CREATOR_ID:
        await message.add_reaction('👍')

# Run the bot
client.run('your_token_here')
