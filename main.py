import os
import asyncio
from telegram import Bot
from telegram.constants import ParseMode
from PIL import Image
from mytoken import TOKEN
from usd import main as get_usd_price 
from write import make_image
import pytz
from datetime import datetime

CHANNEL_ID = "@stronghold_usdollar"

INPUT_IMAGE = "assets/cache.png"  
STICKER_IMAGE = "sticker.webp"

def convert_to_sticker(input_path, output_path):
    image = Image.open(input_path)
    image = image.convert("RGBA")
    image.thumbnail((512, 512))  
    image.save(output_path, "WEBP", quality=100)

async def send_sticker():
    print('hello')

    bot = Bot(TOKEN)

    try:
        usd_price = get_usd_price()  
    except requests.exceptions.RequestException as e:
        print(f"Error fetching USD price: {e}")
        usd_price = '.'

    make_image(usd_price)  
    convert_to_sticker(INPUT_IMAGE, STICKER_IMAGE)

    async with bot:
        with open(STICKER_IMAGE, "rb") as sticker:
            try:
                await bot.send_sticker(chat_id=CHANNEL_ID, sticker=sticker)
            except requests.exceptions.RequestException as e:
                print(f"Error sending USD price sticker: {e}")
                
    print("Sticker sent successfully!")
    os.remove(STICKER_IMAGE)

async def check_time_and_run():
    # Define the Tehran timezone
    tehran_tz = pytz.timezone('Asia/Tehran')
    
    while True:
        # Get the current time in Tehran
        tehran_time = datetime.now(tehran_tz)
        
        # Check if it's 10 PM in Tehran
        if tehran_time.hour == 22 and tehran_time.minute == 0:
            await send_sticker()
            # Sleep for a minute to avoid multiple triggers within the same minute
            await asyncio.sleep(60)
        else:
            # Sleep for a short time before checking again
            await asyncio.sleep(30)

async def main():
    print("Bot is running and waiting for the scheduled task...")
    await check_time_and_run()

if __name__ == "__main__":
    asyncio.run(main())
