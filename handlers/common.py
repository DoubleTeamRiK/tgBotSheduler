from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, CommandHelp
from loader import dp, bot
from keyboards.common_kb import com_btn, welcome_mrkup
from utils.dbmanage.dbcontrol import add_user_to_db, user_exists, get_position


@dp.message_handler(CommandStart())
async def send_welcome(message: types.Message):
    if not user_exists(message.from_user.id):
        await bot.send_message(message.from_user.id, text="Добрый день. Я бот автоматической записи.\
                    Чтобы пользоваться возможностями сервиса\
                    зарегистрируйтесь в системе как мастер или клиент.", reply_markup=welcome_mrkup)
    else:
        await bot.send_message(message.from_user.id, text="Вы уже есть в нашей БД.")
