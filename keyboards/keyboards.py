from aiogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup
)


start_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='option1', callback_data='op1'),
        InlineKeyboardButton(text='option2', callback_data='op2')
    ],
    [
        InlineKeyboardButton(text='option3', callback_data='op3'),
        InlineKeyboardButton(text='option4', callback_data='op4')
    ],
    [
        InlineKeyboardButton(text='option5', callback_data='op5'),
    ],
])
