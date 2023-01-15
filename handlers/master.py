from aiogram import types
from aiogram.types import ReplyKeyboardRemove

from keyboards.common_kb import welcome_mrkup
from keyboards.master_kb import shedule_mrkup
from loader import dp, bot
from utils.dbmanage.dbcontrol import user_exists, add_user_to_db, get_position


async def save_user_to_db(message: types.Message):
    if not user_exists(message.from_user.id):
        add_user_to_db(message.from_user.id, message.text, 1)
        await bot.send_message(message.from_user.id, text=f"Добро пожаловать, {message.text}.\n "
                                                          f"Создайте свой профиль и расписание работы, чтобы клиенты "
                                                          f"смогли записаться к Вам",
                               reply_markup=shedule_mrkup)


@dp.callback_query_handler()
async def callback_welcome_user(callback: types.CallbackQuery):
    if callback.data == 'Мастер':
        await bot.send_message(chat_id=callback.message.chat.id, text="Как Вас зовут?")


@dp.message_handler(content_types=['text'])
async def add_user(message: types.Message):
    await save_user_to_db(message)


