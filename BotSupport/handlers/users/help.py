from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/support_call - Написать сообщение техподдержку",
            "/help - Получить справку",
            "/start - Начать диалог",
    )
    await message.answer("\n".join(text))
