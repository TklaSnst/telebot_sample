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
    [KeyboardButton(text='get all banned users'), KeyboardButton(text='add admin')],
    [KeyboardButton(text='return')]
], resize_keyboard=True)


async def get_user_actions_kb(is_active, tg_id):
    admin_unbanned_user_actions = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='ban user', callback_data=f'ban_{tg_id}')],
        [InlineKeyboardButton(text='some info', callback_data=f'get_some_user_info_{tg_id}')]
    ])
    admin_banned_user_actions = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='unban user', callback_data=f'unban_{tg_id}')],
        [InlineKeyboardButton(text='some info', callback_data=f'get_some_user_info_{tg_id}')]
    ])
    if is_active:
        return admin_unbanned_user_actions
    return admin_banned_user_actions


return_to_main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вернуться на главную')]
], resize_keyboard=True)
