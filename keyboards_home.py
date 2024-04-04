from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton,
                           ReplyKeyboardMarkup, KeyboardButton)


def get_products_ikb():
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Mahsulot qo'shish", callback_data="create_product")],
        [InlineKeyboardButton(text="Mahsulotlarni ko'rish", callback_data="all_products")]

    ], resize_keyboard=True)

    return ikb


def get_start_kb():
    kb = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='/products')]
    ], resize_keyboard=True)
    return kb
