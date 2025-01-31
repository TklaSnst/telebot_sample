from aiogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
)


start_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='option1', callback_data='op1'),
     InlineKeyboardButton(text='option2', callback_data='op2')],
    [InlineKeyboardButton(text='option3', callback_data='op3'),
     InlineKeyboardButton(text='option4', callback_data='op4')],
    [InlineKeyboardButton(text='option5', callback_data='op5'),],
])

start_kb_admin = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='option1', callback_data='op1'),
     InlineKeyboardButton(text='option2', callback_data='op2')],
    [InlineKeyboardButton(text='option3', callback_data='op3'),
     InlineKeyboardButton(text='option4', callback_data='op4')],
    [InlineKeyboardButton(text='admin_panel', callback_data='admin_panel'),],
])

admin_panel_main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='get user by uid'), KeyboardButton(text='get user by tg id')],
    [KeyboardButton(text='ban user by uid'), KeyboardButton(text='ban user by tg id')],
    [KeyboardButton(text='return')]
], resize_keyboard=True)
