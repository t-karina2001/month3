from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
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
    await message.answer("Введите направление ментора")


async def load_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['direction'] = message.text
    await FSMAdmin.next()
    await message.answer("Сколько лет?")


async def load_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Пишите числа!")
    elif not 14 < int(message.text) < 35:
        await message.answer("Доступ запрещен!")
    else:
        async with state.proxy() as data:
            data['age'] = message.text
        await FSMAdmin.next()
        await message.answer('Введите группу')


async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text
    await FSMAdmin.next()
    await message.answer(f"Имя ментора {data['name']}\n"
                         f"Направление {data['direction']}\n"
                         f"Возраст {data['age']}\n"
                         f"Группа {data['group']}\n")
    await message.answer("Все верно?")


async def load_submit(message: types.Message, state: FSMContext):
    if message.text.lower() == 'да':
        await state.finish()
        await message.answer('Ментор записан в базе данных')
    elif message.text.lower() == 'начать заново':
        await FSMAdmin.name.set()
        await message.answer('Введите имя ментора')


def register_handlers_fsm_anketa(dp: Dispatcher):
    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_direction, state=FSMAdmin.direction)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_group, state=FSMAdmin.group)
    dp.register_message_handler(load_submit, state=FSMAdmin.submit)

