from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

KeyBoard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Информация')],
    [KeyboardButton(text='Рассчитать')],
    [KeyboardButton(text="Купить")],
    [KeyboardButton(text="Регистрация")]
], resize_keyboard=True)

INKboard_1 = InlineKeyboardMarkup()
INKbutt_1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
INKbutt_2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
INKboard_1.add(INKbutt_1)
INKboard_1.add(INKbutt_2)

INKboard_2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Product1", callback_data="product_buying")],
        [InlineKeyboardButton(text="Product2", callback_data="product_buying")],
        [InlineKeyboardButton(text="Product3", callback_data="product_buying")],
        [InlineKeyboardButton(text="Product4", callback_data="product_buying")]
    ])

# kb.insert kb.row