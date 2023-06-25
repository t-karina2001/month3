from apscheduler.schedulers.asyncio import AsyncIOScheduler
from config import bot, ADMINs


async def wash_your_car():
    for user in ADMINs:
        bot.send_message(user, 'Тачку на мойку, срроооочноооо!!!')


async def set_scheduler():
    scheduler = AsyncIOScheduler(timezone="Asia/Bishkek")
    scheduler.add_job(wash_your_car, 'cron', day_of_week='sat', hour=18, minute=0)
    scheduler.start()

    scheduler.start()
