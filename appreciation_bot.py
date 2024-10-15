import discord
from discord.ext import commands
import json
from dotenv import load_dotenv
import os

# Load environment variables (Discord token)
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Load card data from cards.json
with open('cards.json', 'r') as f:
    group_works_deck = json.load(f)

# Load category data from categories.json
with open('categories.json', 'r') as f:
    categories = json.load(f)

# Set up intents
intents = discord.Intents.default()
intents.messages = True  # Bot needs to listen to messages
intents.guilds = True    # Bot interacts with guild (server) events
intents.members = True   # TEMPORARY: Allows bot to access member data (important for @mentions)
intents.message_content = True  # Enables bot to read message content

# Set up bot with command prefix and intents
bot = commands.Bot(command_prefix='!', intents=intents)

# On bot ready
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

# Function to get or create the #appreciations channel
async def get_or_create_appreciations_channel(guild):
    appreciation_channel = discord.utils.get(guild.text_channels, name="appreciations")
    if appreciation_channel is None:
        # Create the #appreciations channel
        appreciation_channel = await guild.create_text_channel("appreciations")
    return appreciation_channel

# Command to list category names with numbers (sent to private DM)
@bot.command(name='list_categories')
async def list_categories(ctx):
    category_list = "\n".join([f"{index + 1}. {category['name']}" for index, category in enumerate(categories)])
    await ctx.author.send(f"**Available Categories**:\n{category_list}")

# Command to get details of a specific category by number or name (sent to private DM)
@bot.command(name='category_info')
async def category_info(ctx, identifier: str):
    # If the identifier is a number, fetch by index
    if identifier.isdigit():
        index = int(identifier) - 1
        if 0 <= index < len(categories):
            category = categories[index]
        else:
            await ctx.author.send("Invalid category number. Please select a valid number from the list.")
            return
    # If the identifier is not a number, assume it's a category name
    else:
        normalized_category_name = identifier.strip().lower()
        category = next((cat for cat in categories if cat['name'].strip().lower() == normalized_category_name), None)

        if not category:
            await ctx.author.send(f"Category '{identifier}' not found. Please select a valid category.")
            return

    # Send category information
    await ctx.author.send(f"**{category['name']}**: {category['description']}")

# Command to list cards in a specific category by number or name (sent to private DM)
@bot.command(name='list_cards_by_category')
async def list_cards_by_category(ctx, identifier: str):
    # Handle identifier as number or name
    if identifier.isdigit():
        index = int(identifier) - 1
        if 0 <= index < len(categories):
            category_name = categories[index]['name']
        else:
            await ctx.author.send("Invalid category number. Please select a valid number from the list.")
            return
    else:
        category_name = identifier.strip().lower()

    # Find cards in the selected category
    cards_in_category = [f"{index + 1}. {card['name']}" for index, card in enumerate(group_works_deck) if card['category'].strip().lower() == category_name.lower()]
    
    if not cards_in_category:
        await ctx.author.send(f"No cards found in the '{category_name}' category.")
        return

    # List cards with global numbering
    card_list = "\n".join(cards_in_category)
    await ctx.author.send(f"**Cards in '{category_name}'**:\n{card_list}")

# Command to show a card's image and details without appreciation (sent to private DM)
@bot.command(name='show_card')
async def show_card(ctx, card_identifier: str):
    # If the identifier is a number, fetch by index
    if card_identifier.isdigit():
        index = int(card_identifier) - 1
        if 0 <= index < len(group_works_deck):
            card = group_works_deck[index]
        else:
            await ctx.author.send("Invalid card number. Please select a valid number from the list.")
            return
    # If the identifier is not a number, assume it's a card name
    else:
        normalized_card_name = card_identifier.strip().lower()
        card = next((c for c in group_works_deck if c['name'].strip().lower() == normalized_card_name), None)

        if not card:
            await ctx.author.send(f"Card '{card_identifier}' not found. Please select a valid card.")
            return

    # Create embed to show the card details
    embed = discord.Embed(title=card['name'], description=card['heart'], color=0x00ff00)
    embed.set_image(url=card['pic'])

    # Send the card details in an embed (via DM)
    await ctx.author.send(embed=embed)

# Command to show card list and tag someone with appreciation (public, in #appreciations)
@bot.command(name='appreciate')
async def appreciate(ctx, user: discord.Member, card_name: str, *, custom_message: str):
    print(f"Appreciation command received from {ctx.author}. Card: {card_name}, Message: {custom_message}")  # Debugging

    # Normalize card name: strip whitespace and convert to lowercase
    normalized_card_name = card_name.strip().lower()

    # Check if normalized card exists in the group_works_deck
    matched_card = None
    for card_data in group_works_deck:
        if card_data['name'].strip().lower() == normalized_card_name:
            matched_card = card_data
            break

    if not matched_card:
        await ctx.send("Card not found! Please select a valid card.")
        return

    # Fetch card data
    card_image = matched_card["pic"]

    # Get or create the #appreciations channel
    appreciation_channel = await get_or_create_appreciations_channel(ctx.guild)

    # Create embed for the public appreciation message
    embed = discord.Embed(title="Appreciation!", description=f"{ctx.author.mention} appreciates {user.mention}", color=0x00ff00)
    embed.add_field(name="Card", value=matched_card["name"], inline=False)
    embed.add_field(name="Message", value=custom_message, inline=False)
    embed.set_image(url=card_image)  # URL of the image, as specified in your new format

    # Send the appreciation in the #appreciations channel
    await appreciation_channel.send(f"@everyone", embed=embed)
    
    # Send a direct message to the user
    await user.send(f"You've been appreciated by {ctx.author.mention}!\nCard: {matched_card['name']}\nMessage: {custom_message}")

# Run bot
bot.run(TOKEN)
