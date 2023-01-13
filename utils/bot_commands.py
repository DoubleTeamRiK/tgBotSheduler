from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("help", "Полезная информация"),
            types.BotCommand("sign_up", "Записаться на сеанс"),
            types.BotCommand("swap", "Сменить аккаунт"),
            types.BotCommand("quit", "Выход")
        ]
    )