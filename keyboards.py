from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Mahsulotlarni ko'rish", callback_data='get_all_product')],
    [InlineKeyboardButton(text="Mahsulot qo'shish", callback_data='add_product')]
])

kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='/products')]
], resize_keyboard=True)
