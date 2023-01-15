from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from loader import dp, bot
from utils.dbmanage.dbcontrol import get_position


# @dp.message_handler(CommandStart())
# async def send_welcome(message: types.Message):
#     if get_position(message.from_user.id) == 'Клиент':
#         await bot.send_message(message.from_user.id, text=f"{message.from_user.username} Вы - наш самый лучший клиент.\
#                                     Хотите записаться? Выберите мастера.")
