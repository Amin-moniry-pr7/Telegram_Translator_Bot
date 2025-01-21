# Translate_BOT
Telegram Translation Bot 🌍

This is a Telegram bot built using Python that allows users to translate text between 9 different languages.

Features

Translate text between the following languages:

🇺🇸 English

🇮🇷 Persian (فارسی)

🇫🇷 French

🇰🇷 Korean

🇪🇸 Spanish

🇸🇪 Swedish

🇨🇳 Chinese

🇹🇷 Turkish

🇸🇦 Arabic


Automatic language detection for the input text.

Interactive and easy-to-use Telegram interface.


Requirements

To run the bot, you need:

1. Python 3.12.4 (or later)


2. The following Python libraries:

pyTelegramBotAPI

googletrans




Install them using:

pip install pyTelegramBotAPI googletrans==4.0.0-rc1

3. A Telegram Bot token from BotFather.



Setup

1. Clone this repository:

git clone https://github.com/username/repository_name.git
cd repository_name


2. Set the bot token as an environment variable:

export BOT_TOKEN=your_bot_token


3. Run the bot:

python translator 🌍.py



Usage

1. Start the bot in Telegram by sending /start.


2. Select the source and target languages.


3. Send the text you want to translate.



Notes

Ensure you keep your BOT_TOKEN secure and do not expose it in public repositories.

Use .env files and .gitignore for better security.


Contributing

Feel free to open issues or submit pull requests to improve the bot.
