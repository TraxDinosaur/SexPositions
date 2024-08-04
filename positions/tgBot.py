import asyncio
import logging
from .funcs import *
from config import Config
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    num = 1
    counter = 0
    while True:
        url = f"https://sexpositions.club/positions/{num}.html"
        response = requests.get(url)
        soup = bs(response.text, 'html.parser')

        positionNumber = getNumber(soup)
        positionName = getName(soup)
        positionDescription = getDescription(soup)
        positionImageUrl = getImageUrl(soup)
        positionSimilar = getSimilar(soup)
        sft = getSft(soup)
        photo_url = positionImageUrl

        caption = f"<b>Position: </b>{positionNumber}\n"
        caption += f"<b>Name: </b> {positionName}\n"
        caption += f"\n\n<b>Description: </b>{positionDescription}\n"
        caption += f"\n<b>Similar: </b> {positionSimilar}\n"
        caption += f"\n<b>Safety: </b> {sft}\n"
        caption += "@PositionInSex"

        await context.bot.send_photo(chat_id=Config.TELEGRAM_CHAT_ID, photo=photo_url, caption=caption, parse_mode='HTML')
        num += 1
        counter += 1

        if counter >= 20:
            counter = 0
            await asyncio.sleep(90)

tgapp = ApplicationBuilder().token(Config.TELEGRAM_TOKEN).build()
photo_handler = CommandHandler('photo', photo)
tgapp.add_handler(photo_handler)

if __name__ == '__main__':
    tgapp.run_polling()
