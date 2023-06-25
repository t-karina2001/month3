from aiogram import executor
import logging
from config import dp, bot, ADMINs
from handlers import commands, callbacks, extra, admin, fsm_anketa, notifications
from database.bot_db import sql_create


commands.register_handlers_commands(dp)
callbacks.register_handlers_callback(dp)
fsm_anketa.register_handlers_fsm_anketa(dp)
admin.register_handler_admins(dp)
extra.register_extra_handlers(dp)


async def on_startup(dp):
    sql_create()
    await bot.send_message(ADMINs[0], 'Привет, я здесь!')
    await notifications.set_scheduler()


async def on_shutdown(dp):
    await bot.send_message(ADMINs[0], 'Не прощаюсь!')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True,
                           on_startup=on_startup,
                           on_shutdown=on_shutdown)
