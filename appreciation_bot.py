import discord
from discord.ext import commands
from PIL import Image
import json
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Load card data from cards.json
with open('cards.json', 'r') as f:
    group_works_deck = json.load(f)

# Set up intents
intents = discord.Intents.default()
intents.messages = True  # Bot needs to listen to messages
intents.guilds = True    # Bot interacts with guild (server) events
intents.members = True   # TEMPORARY: Allows bot to access member data (important for @mentions)
intents.message_content = True  # THIS is the critical part to read message content

# Set up bot with command prefix and intents
bot = commands.Bot(command_prefix='!', intents=intents)

# On bot ready
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

# Command to show card list and tag someone
@bot.command(name='appreciate')
async def appreciate(ctx, user: discord.Member, card_name: str, *, custom_message: str):
    print(f"Appreciation command received from {ctx.author}. Card: {card_name}, Message: {custom_message}")  # Debugging

    # Normalize card name: strip whitespace and convert to lowercase
    normalized_card_name = card_name.strip().lower()

    # Check if normalized card exists in the group_works_deck
    matched_card = None
    for card_key, card_data in group_works_deck.items():
        if card_data['name'].strip().lower() == normalized_card_name:
            matched_card = card_data
            break

    if not matched_card:
        await ctx.send("Card not found! Please select a valid card.")
        return

    # Fetch card data
    card_image = matched_card["image"]

    # Send appreciation message to general channel (or change back to #appreciations if it exists)
    appreciation_channel = discord.utils.get(ctx.guild.channels, name="general")  # Posting in #general for testing
    if appreciation_channel is None:
        await ctx.send("General channel not found!")
        return
    
    # Create embed for the public appreciation message
    embed = discord.Embed(title="Appreciation!", description=f"{ctx.author.mention} appreciates {user.mention}", color=0x00ff00)
    embed.add_field(name="Card", value=matched_card["name"], inline=False)
    embed.add_field(name="Message", value=custom_message, inline=False)
    embed.set_image(url=f"attachment://{card_image}")
    
    # Send the appreciation in the #general channel
    with open(card_image, 'rb') as img:
        await appreciation_channel.send(f"@everyone", embed=embed, file=discord.File(img, card_image))
    
    # Send a direct message to the user
    await user.send(f"You've been appreciated by {ctx.author.mention}!\nCard: {matched_card['name']}\nMessage: {custom_message}")

# Run bot
bot.run(TOKEN)
