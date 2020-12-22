from aiogram.utils.executor import start_webhook
from bot import HEROKU_APP_NAME, WEBHOOK_URL, bot, executor, dp
from importlib import import_module
from asyncio import get_event_loop
from os import listdir

#https://github.com/aiogram/aiogram/blob/dev-2.x/examples/webhook_example.py
async def on_startup():
    await bot.set_webhook(WEBHOOK_URL)


async def on_shutdown():
    await bot.delete_webhook()


modules = [module for module in listdir("./bot/modules/") if module.endswith(".py")]
for i in modules:
    import_module("bot.modules." + i.split(".")[0])

if HEROKU_APP_NAME:
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_URL,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host="0.0.0.0",
        port="5000"
    )
else:
    get_event_loop().run_until_complete(bot.delete_webhook())
    executor.start_polling(dp, skip_updates=True)
