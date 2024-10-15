Let's update the README to include the full list of commands and the recent changes. Here's the updated version of the README with explanations for all current bot commands:

---

# Group Works Appreciation Bot

**Group Works Appreciation Bot** is a Discord bot that allows users to interact with the **Group Works deck** by listing categories, selecting cards, and sending appreciation messages. Users can tag someone, select a card from the deck, and send a personalized appreciation message. The bot posts the appreciation publicly in a channel and sends a direct message to the appreciated user.

---

## Features

- List categories from the Group Works deck.
- List cards from specific categories.
- Show the image and description of any card without sending appreciation.
- Send appreciation to a tagged user with a custom message and card image.
- Post the appreciation publicly and send a direct message to the recipient.

---

## How to Use

After installing and running the bot, you can use the following commands:

### Commands

1. **List Categories**  
   Use this command to list the names of available categories.

   ```
   !list_categories
   ```

   - Example Response:  
     ```
     **Available Categories**:
     1. Context
     2. Faith
     3. Intention
     ```

2. **Show Category Details**  
   Use this command to get detailed information (description) about a specific category by its name or number.

   ```
   !category_info [number | name]
   ```

   - Example Usage:
     ```
     !category_info 1
     !category_info Faith
     ```

   - Example Response:  
     ```
     **Faith**: Faith in the process and in the participants, providing a foundation for allowing the unknown to unfold.
     ```

3. **List Cards by Category**  
   Use this command to list the cards in a specific category. You can use either the category's name or its number from the `!list_categories` command.

   ```
   !list_cards_by_category [number | name]
   ```

   - Example Usage:
     ```
     !list_cards_by_category 1
     !list_cards_by_category Context
     ```

   - Example Response:  
     ```
     **Cards in 'Context'**:
     1. Aesthetics of Space
     2. All Grist for the Mill
     ```

4. **Show Card Image and Details**  
   Use this command to show the image and description of a specific card without sending appreciation. You can reference the card by its name or number from the `!list_cards_by_category` command.

   ```
   !show_card [number | name]
   ```

   - Example Usage:
     ```
     !show_card 1
     !show_card Aesthetics of Space
     ```

   - Example Response:  
     The bot will display an embed with the card's image and "heart" description:
     ```
     **Aesthetics of Space**:
     [Card image]
     Gathering places that are beautiful, comfortable, functional, and creatively designed to serve the purpose of the meeting.
     ```

5. **Send Appreciation**  
   Use this command to send an appreciation message to another user. You can select a card by name and add a custom message to the appreciation.

   ```
   !appreciate @User CardName Custom Message
   ```

   - `@User`: The user you want to appreciate (mention the user).
   - `CardName`: The name of the card from the Group Works deck (case-insensitive).
   - `Custom Message`: Your personalized message of appreciation.

   - Example Command:
     ```
     !appreciate @Daniel Lindenberger Emergence You're literally emerging things right now!
     ```

   - Example Response:  
     The bot will send an embed with the card's image and custom message to the `#general` or designated appreciation channel, and also send a direct message to the tagged user.

---

## Installation

### 1. Clone the Repository
First, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/group-works-appreciation-bot.git
cd group-works-appreciation-bot
```

### 2. Set Up the Python Environment

Make sure you have Python 3.x installed. Create a virtual environment and install the dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Set Up the `.env` File

Create a `.env` file in the root directory to store your Discord bot token. You can get the bot token from the [Discord Developer Portal](https://discord.com/developers/applications).

In the `.env` file, add the following line:

```env
DISCORD_TOKEN=your_discord_bot_token_here
```

### 4. Set Up the Group Works Cards

Ensure you have the `cards.json` file and the corresponding images for each card in a `cards/` folder in the root directory. The `cards.json` should follow this format:

```json
[
    {
        "name": "Aesthetics of Space",
        "pic": "https://example.com/path_to_image.jpg",
        "heart": "Gathering places that are beautiful, comfortable, functional, and creatively designed to serve the purpose of the meeting call forth participants' best life energy to contribute.",
        "category": "Context"
    },
    {
        "name": "Emergence",
        "pic": "https://example.com/path_to_image2.jpg",
        "heart": "In complex systems, patterns and order emerge unexpectedly. Stay present to notice the emergence and adapt accordingly.",
        "category": "Process"
    }
]
```

Each card should have:
- `name`: The title of the card.
- `pic`: A publicly accessible URL to the image.
- `heart`: The description or key message of the card.
- `category`: The category to which the card belongs.

### 5. Enable Privileged Intents

Go to the [Discord Developer Portal](https://discord.com/developers/applications), and under the **"Bot"** section for your bot:
- Enable **Server Members Intent**.
- Enable **Message Content Intent**.

### 6. Run the Bot

Now, you can run the bot:

```bash
python appreciation_bot.py
```

### 7. Invite the Bot to Your Server

Go to the [OAuth2 URL Generator](https://discord.com/developers/applications) for your bot, and create an invite link with the necessary permissions:
- `Send Messages`
- `Read Message History`
- `Embed Links`
- `Attach Files`
- `Mention Everyone`

Invite the bot to your server by visiting the generated OAuth2 URL.

---

## Bot Permissions

Ensure the bot has the following permissions in your server:

- **Send Messages**: Allows the bot to send messages in channels.
- **Embed Links**: Allows the bot to embed rich content (such as appreciation messages).
- **Attach Files**: Allows the bot to attach card images.
- **Read Message History**: Ensures the bot can interact with previous messages if needed.
- **Mention Everyone**: Allows the bot to tag `@everyone` when sending appreciation messages.

---

## Example `cards.json` and Directory Structure

```
group-works-appreciation-bot/
├── appreciation_bot.py
├── cards.json
├── cards/
│   ├── Invitation.jpg
│   ├── Emergence.jpg
├── .env
├── requirements.txt
└── README.md
```

---

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request with your improvements or fixes.

---

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

That's the complete **README** with the latest command list and detailed instructions. Let me know if you'd like any additional tweaks or updates!
