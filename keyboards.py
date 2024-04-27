from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

admin_ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Mahsulotlarni ko'rish", callback_data='get_all_product')],
    [InlineKeyboardButton(text="Mahsulot qo'shish", callback_data='add_product')]
])

ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Mahsulotlarni ko'rish", callback_data='get_all_product')],
])

kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='/products')]
], resize_keyboard=True)

buy_ikb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='🛒', callback_data='savatchaga'),
         InlineKeyboardButton(text='❤', callback_data='sevimlilar')]

    ])

delete_order_ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🚮', callback_data='delete_order')],
], resize_keyboard=True)

delete_favorites_ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🛒', callback_data='savatchaga'),
     InlineKeyboardButton(text='🚮', callback_data='delete_favorite')],
], resize_keyboard=True)
