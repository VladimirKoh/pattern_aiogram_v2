import asyncio
import json
import logging
import ssl
from aiogram import Bot, Dispatcher, executor, types
from loader import dp, bot
import handlers, middlewares
from utils.notify_admins import on_startup_notify, on_shutdown_notify
from utils.set_bot_commands import set_default_commands
# from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiohttp import web
from data import config


WEBHOOK_HOST = config.WEBHOOK_HOST
WEBHOOK_PATH = config.WEBHOOK_PATH
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

WEBHOOK_SSL_CERT = config.WEBHOOK_SSL_CERT
WEBHOOK_SSL_PRIV = config.WEBHOOK_SSL_PRIV
WEBAPP_HOST = config.WEBAPP_HOST
WEBAPP_PORT = config.WEBAPP_PORT


async def on_startup(app):
    await set_default_commands(dp)
    await on_startup_notify(dp)
    await bot.set_webhook(url=WEBHOOK_URL, drop_pending_updates=True)
    # logging.info(await bot.get_webhook_info())
    # scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
    # scheduler.add_job(check_balance_and_debits_money, trigger='cron', hour=19, args=(dp,))
    # scheduler.start()
    

async def on_shutdown(app):
    await on_shutdown_notify(dp)
    await bot.delete_webhook(drop_pending_updates=True)


async def aiogram(request):
    try:
        data = await request.json()
        Bot.set_current(bot)
        asyncio.create_task(dp.process_update(types.Update(**data)))
        return web.Response(status=200)
    except Exception as e:
        logging.exception(e)
        return web.Response(status=200)


if __name__ == '__main__':
    Bot.set_current(bot)
    Dispatcher.set_current(dp)
    # executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown, skip_updates=True)
    app = web.Application()
    app.router.add_route('POST', '/webhook', aiogram)
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)
    # ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    # ssl_context.load_cert_chain(WEBHOOK_SSL_CERT, WEBHOOK_SSL_PRIV)
    web.run_app(app, host=WEBAPP_HOST, port=WEBAPP_PORT)#, ssl_context=ssl_context)