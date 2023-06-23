from aiogram import types, Dispatcher
from config import bot, ADMINs
import random


async def send_dice(message: types.Message):
    if message.from_user.id in ADMINs:
        if message.text.startswith('game'):
            dice_emojis = ['⚽', '🏀', '🎲', '🎯', '🎳', '🎰']
            random_dice_emoji = random.choice(dice_emojis)
            await bot.send_message(message.chat.id, random_dice_emoji)


async def pin(message: types.Message):
    if message.from_user.id in ADMINs:
        await bot.pin_chat_message(message.chat.id, message.message_id)


def register_handler_admins(dp: Dispatcher):
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!/')
    dp.register_message_handler(send_dice)
