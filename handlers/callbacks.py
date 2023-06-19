from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def quiz_2(callback: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    next_button = InlineKeyboardButton("NEXT", callback_data="next_button_2")
    markup.add(next_button)

    quiestion = "Каково настоящее имя Черной Пантеры?"
    answers = [
        "Т'Чалла",
        "М'Баку",
        "Нджадака",
        "Н'Джобу",
    ]

    await callback.message.answer_poll(
        question=quiestion,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="Уят ай! Марвел коргондор билбесин!",
        open_period=10,
        reply_markup=markup
    )


async def quiz_3(callback: types.CallbackQuery):
    quiestion = "О каком городе часто вспоминают Соколиный Глаз и Черная Вдова?"
    answers = [
        "Стамбул",
        "Прага",
        "Будапешт",
        "Нью-Йорк",
        "Москва",
    ]

    await callback.message.answer_poll(
        question=quiestion,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Фанаты Марвел плачут(",
        open_period=10,
    )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="next_button_1")
    dp.register_callback_query_handler(quiz_3, text="next_button_2")
