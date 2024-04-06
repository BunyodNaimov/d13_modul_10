import os
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from dotenv import load_dotenv

from db import db_get_all_products, db_insert_product
from keyboards import kb, ikb
from states import ProductStatesGroup

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer("Assalomu Aleykum!\n Do'konimizga xush kelibsiz!", reply_markup=kb)


@dp.message(Command('products'))
async def cmd_products(message: types.Message):
    await message.answer("Mahsulotlarni boshqarish!", reply_markup=ikb)


@dp.callback_query(F.data == 'get_all_product')
async def get_all_product(call: types.CallbackQuery):
    product = db_get_all_products()
    await call.message.delete()
    if not product:
        await call.message.answer("Mahsulot mavjud emas!")
    for product in product:
        print(product)
        await call.message.answer_photo(photo=product[3],
                                        caption=f"Mahsulot nomi: {product[1]}\n"
                                                f"Mahsulot narxi: {product[2]}\n")


@dp.callback_query(F.data == 'add_product')
async def add_product(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(ProductStatesGroup.title)
    await call.message.answer("Mahsulot nomini kiriting: ")


@dp.message(ProductStatesGroup.title)
async def create_product_title(message: types.Message, state: FSMContext):
    await state.update_data(title=message.text)
    await state.set_state(ProductStatesGroup.price)
    await message.answer("Mahsulot narxini kiriting: ")


@dp.message(ProductStatesGroup.price)
async def create_product_price(message: types.Message, state: FSMContext):
    await state.update_data(price=message.text)
    await state.set_state(ProductStatesGroup.photo)
    await message.answer("Mahsulot rasmini yuboring: ")


@dp.message(ProductStatesGroup.photo)
async def create_product_photo(message: types.Message, state: FSMContext):
    await state.update_data(photo=message.photo[-1].file_id)
    data = await state.get_data()
    await message.answer("Mahsulot yaratildi!")
    await db_insert_product(data['title'], data['price'], data['photo'])


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
