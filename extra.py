from aiogram import Dispatcher, types
from config import bot, ADMINs
from random import choice


async def echo(message: types.Message) -> None:
    if message.text.isdigit():
        squared = int(message.text) ** 2
        await bot.send_message(message.chat.id, f'Квадрат числа {message.text} равен {squared}')

    elif message.from_user.id not in ADMINs:
        await message.answer("Ты не мой босс!")
        await bot.send_message(message.chat.id, message.text)

    else:
        if message.text.startswith('Game'):  # Игра работает для всех!
            a = ['⚽', '🎰', '🏀', '🎯', '🎳', '🎲']
            random = choice(a)
            await bot.send_dice(message.chat.id, emoji=random)
        else:
            await bot.send_message(message.from_user.id, message.text)




async def echo_text(message: types.Message) -> None:
    await bot.send_message(message.chat.id, message.text)


def register_extra_handlers(dp: Dispatcher):
    dp.register_message_handler(echo)
    dp.register_message_handler(echo_text, commands='text')
