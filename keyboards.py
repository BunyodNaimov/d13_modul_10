from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_all_products_ikb():
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Barcha mahsulotlar!',
                              callback_data='get_all_products_ikb')]
    ], resize_keyboard=True)

    return ikb
