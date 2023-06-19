from aiogram import types, Dispatcher
from config import bot, ADMINs


async def pin(message: types.Message):
    if message.chat.type != "private":
        if message.from_user.id not in ADMINs:
            await message.answer("Ты не админ!")
        elif not message.reply_to_message:
            await message.answer("Команда должна быть ответом на сообщение!")
        else:
            await bot.pin_chat_message(message.chat.id, message.message_id)
            await message.answer(
                f"{message.from_user.first_name} закрепил, исполнено! "
                f"{message.reply_to_message.from_user.full_name}"
            )
    else:
        await message.answer("Ты пишешь в личку, пиши в группу!")



def register_handler_admins(dp: Dispatcher):
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!/')

