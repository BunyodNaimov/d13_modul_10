import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
from db import get_all_products

from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(token=BOT_TOKEN)

dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer('Bot ishlayapti!')


@dp.message(Command('all_product'))
async def cmd_all_product(message: types.Message):
    products = get_all_products()
    if not products:
        await message.answer("Bizda xozircha mahsulotlar mavjud emas!")
    for i in products:
        await message.answer(i.title)


async def main():
    print("Bot Started....")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
