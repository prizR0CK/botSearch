from aiogram import types

keyBrd = [[types.KeyboardButton(text="Goods search")],]

keyBoard = types.ReplyKeyboardMarkup(keyboard=keyBrd, resize_keyboard=True, input_field_placeholder="Write /start")
