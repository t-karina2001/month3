from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import ADMINs


class FSMAdmin(StatesGroup):
    name = State()
    direction = State()
    age = State()
    group = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.from_user.id not in ADMINs:
        await message.answer("Вы не являетесь админом!")
    else:
        await FSMAdmin.name.set()
        await message.answer("Введите имя ментора")


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer("Скока лет?")



#
# async def fsm_start(message: types.Message):
#     if message.chat.type == 'private':
#         await FSMAdmin.name.set()
#         await message.answer("Как звать?")
#     else:
#         await message.reply("Пиши в личке!")
#
#
# async def load_name(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['id'] = message.from_user.id
#         data['username'] = f"@{message.from_user.username}" \
#             if message.from_user.username else None
#         data['name'] = message.text
#     await FSMAdmin.next()
#     await message.answer("Скока лет?")


def register_handlers_fsm_anketa(dp: Dispatcher):
    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_name, state=FSMAdmin.name)


