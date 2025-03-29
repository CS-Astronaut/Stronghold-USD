# USD Price Telegram Bot 💲

<img src="assets/neutral.png" alt="USD Price Bot" width="300" height="300">

## Overview
This project is a Telegram bot that fetches the daily USD price from the internet, generates an image with the price displayed, converts it into a sticker, and sends it to a specified Telegram channel.

## Features
- Scrapes USD exchange rates from [alanchand.com](https://alanchand.com/currencies-price/usd)
- Stores the USD price in an SQLite database
- Generates an image with the USD price
- Converts the image into a Telegram sticker
- Sends the sticker to a Telegram channel
- Runs automatically on a daily schedule

## File Structure
```
├── assets
│   ├── EagleLake-Regular.ttf
│   └── neutral.png
├── LICENSE
├── main.py
├── mytoken.py
├── README.md
├── usd.py
└── write.py
```

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/CS-Astronaut/Stronghold-USD.git
   cd Stronghold-USD
   ```
2. Install dependencies:
   ```bash
   pip install pillow asyncio pytz python-telegram-bot requests bs4
   ```
3. Set up the `mytoken.py` file with your Telegram bot token:
   ```python
   TOKEN = "your-telegram-bot-token"
   ```


The bot will run in the background and execute the `send_sticker` function daily at 22:00.

## License
This project is licensed under the MIT License.



