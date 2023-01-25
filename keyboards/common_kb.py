from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, \
    InlineKeyboardMarkup

com_btn_master = KeyboardButton("Мастер")
com_btn_client = KeyboardButton("Клиент")

com_btn = ReplyKeyboardMarkup(resize_keyboard=True).add(com_btn_master, com_btn_client)

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

"""Create button for choise user position"""
welcome_mrkup = InlineKeyboardMarkup(row_width=2)
welcome_master = InlineKeyboardButton(text='Мастер', callback_data='Мастер')
welcome_client = InlineKeyboardButton(text='Клиент', callback_data='Клиент')
welcome_mrkup.add(welcome_master, welcome_client)
