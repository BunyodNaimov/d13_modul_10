from aiogram.fsm.state import StatesGroup, State


class ProductStateGroup(StatesGroup):
    title = State()
    price = State()
    photo = State()
