from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, CommandHelp
from loader import dp, bot
from keyboards.common_kb import com_btn


@dp.message_handler(CommandStart())
async def send_welcome(message: types.Message):
    await bot.send_message(message.from_user.id, "Добрый день. Я бот автоматической записи на сеанс массажа.\
            Зарегистрируйтесь в системе как мастер или клиент.", reply_markup=com_btn)
