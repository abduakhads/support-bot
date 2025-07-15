# SupportBot

SupportBot is a lightweight Python-based chatbot designed to provide support and answer queries without the need for a database. All configurations and logic are handled within Python files, making it easy to set up and run.

## Features

- **No Database Required:** All data and logic are managed in code, so you don't need to set up or maintain a database.
- **Simple Setup:** Just install the dependencies and run the bot.
- **Customizable:** Easily modify the bot's behavior by editing the Python files.

## How It Works

SupportBot operates entirely from Python scripts. It uses configuration files (like `cfg.py`) to manage its settings and logic, so you can deploy and use the bot without any external database or complex infrastructure.

When a user sends a message to the bot, the message is automatically forwarded to the SUPPORT user (whose ID is set in the `.env` file). Along with the forwarded message, the bot attaches the original user's ID so the SUPPORT user knows to whom the reply should be sent.

To answer a user's message, the SUPPORT user should reply to the message id attached to forwarded message. The bot will then send the SUPPORT user's answer back to the original user, using the attached user ID to ensure the response goes to the correct recipient.

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/abduakhads/SupportBot.git

   cd SupportBot
   ```

2. **Install Dependencies**
   Make sure you have Python 3.12+ installed. Then, install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Bot**
   ```bash
   python bot.py
   ```

## Environment Variables

Before running the bot, you need to set up the following environment variables in a `.env` file in the project root:

- `BOT_TOKEN`: The token for your Telegram bot.
- `SUPPORT`: The user ID to whom messages should be forwarded.

Example `.env` file:

```env
BOT_TOKEN=your-telegram-bot-token
SUPPORT=123456789
```

## Configuration

- All configuration and logic are handled in `cfg.py`.
- You can modify `cfg.py` to change the bot's responses or add new features.

## Project Structure

```
SupportBot/
├── bot.py           # Main bot script
├── cfg.py           # Configuration and logic
├── requirements.txt # Python dependencies
└── README.md        # Project documentation
```

## Contributing

Feel free to fork the repository and submit pull requests. Suggestions and improvements are welcome!

