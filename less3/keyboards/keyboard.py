from aiogram import types


button1 = types.KeyboardButton(text='/start')
button3 = types.KeyboardButton(text='/fox')
button2 = types.KeyboardButton(text='/info')
button4 = types.KeyboardButton(text='num')
button5 = types.KeyboardButton(text='/bye')
button6 = types.KeyboardButton(text='/prof')

keyboard1 = [
    [button1, button2, button3, button5]
]
keyboard2 = [
    [button4, button6],
]

kb1 = types.ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)
kb2 = types.ReplyKeyboardMarkup(keyboard=keyboard2, resize_keyboard=True)