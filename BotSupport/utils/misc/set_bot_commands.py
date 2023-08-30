from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("support_call", "Написать сообщение техподдержку"),
        types.BotCommand("help", "Помощь"),
    ])
