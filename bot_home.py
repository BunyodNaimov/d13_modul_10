import asyncio
import os

from aiogram.fsm.context import FSMContext

import db_home
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards_home import get_products_ikb, get_start_kb
from home_commands import commands
from states import ProductStateGroup

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(token=TOKEN)

dp = Dispatcher()

kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='send_contact', request_contact=True)]
], resize_keyboard=True)


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Salom, Do'konimizga xush kelibsiz! /help", reply_markup=get_start_kb())


@dp.message(Command('contact'))
async def send_contact(message: types.Message):
    await message.answer('kontact yuboring', reply_markup=kb)


@dp.message(F.contact)
async def save_phone_number(message: types.Message):
    phone = message.contact.phone_number
    if message.contact.user_id == message.from_user.id:

        await message.answer(f"{phone} to'gri kiritildi!")
    else:
        await message.answer('notogri')


@dp.message(Command('products'))
async def cmd_start(message: types.Message):
    await message.answer("Mahsulotlarni boshqarish", reply_markup=get_products_ikb())


@dp.callback_query(F.data == 'all_products')
async def cb_get_all_products(call: types.CallbackQuery):
    await call.message.delete()
    products = await db_home.db_get_all_products()
    if not products:
        await call.message.answer("Mahsulotlar yo'q")
    for product in products:
        await call.message.answer_photo(photo=product[-1],
                                        caption=f"Nomi: {product[1]}\nNarxi:{product[2]}")


@dp.callback_query(F.data == 'create_product')
async def cb_create_product(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await state.set_state(ProductStateGroup.title)
    await call.message.answer("Mahsulot nomini yuboring: ")


@dp.message(ProductStateGroup.title)
async def product_title_handler(message: types.Message, state: FSMContext):
    await state.update_data(title=message.text)
    await state.set_state(ProductStateGroup.price)
    await message.reply("Mahsulot narxini kiriting: ")


@dp.message(ProductStateGroup.price)
async def product_price_handler(message: types.Message, state: FSMContext):
    await state.update_data(price=message.text)
    await state.set_state(ProductStateGroup.photo)
    await message.reply("Mahsulot rasmini yuboring: ")


@dp.message(ProductStateGroup.photo)
async def product_photo_handler(message: types.Message, state: FSMContext):
    await state.update_data(photo=message.photo[-1].file_id)
    data = await state.get_data()
    await db_home.db_create_product(data['title'], data['price'], data['photo'])
    await message.answer(f'{data["title"]}\n {data["price"]}\n {data["photo"]}')
    await state.clear()


async def main():
    print('Bot Home started...')
    await bot.set_my_commands(commands=commands)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
