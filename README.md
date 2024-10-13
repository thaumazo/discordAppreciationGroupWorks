# Group Works Appreciation Bot

**Group Works Appreciation Bot** is a Discord bot that allows users to send appreciation messages to each other using the **Group Works deck**. Users can tag someone, select a card from the deck, and send a personalized appreciation message. The bot posts the appreciation publicly in a channel, with the selected card and the personalized message, and also sends a direct message to the appreciated user.

---

## Features

- Select a card from the Group Works deck and send an appreciation.
- Tag a user in your server, along with a custom message, to show your appreciation.
- Post the appreciation publicly in a specific channel (e.g., `#appreciations` or `#general`).
- The recipient also receives a private direct message with the appreciation details.
- Supports card images and rich embeds for visual presentation.

---

## How to Use

After installing and running the bot, use the following command format to send appreciation:

```
!appreciate @User CardName Custom Message
```

- `@User`: The user you want to appreciate (mention the user).
- `CardName`: The name of the card from the Group Works deck (case-insensitive).
- `Custom Message`: Your personalized message of appreciation.

### Example Command:

```
!appreciate @Daniel Lindenberger Emergence You're literally emerging things right now!
```

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
{
  "Card1": {
    "name": "Invitation",
    "image": "cards/Invitation.jpg"
  },
  "Card2": {
    "name": "Emergence",
    "image": "cards/Emergence.jpg"
  }
}
```

Each card should have a `name` (the card title) and an `image` (the relative path to the image file). The `cards/` folder should contain the corresponding images (e.g., `Invitation.jpg`, `Emergence.jpg`).

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

That's the complete **README** with installation instructions! Be sure to adjust the repository name, `git` URLs, and any relevant details before publishing. Let me know if you'd like any further modifications or clarifications!
