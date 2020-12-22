from bot import BOT_TOKEN, bot, executor, dp
from importlib import import_module
from os import listdir


modules = [module for module in listdir("./bot/modules/") if module.endswith(".py")]
for i in modules:
    import_module("bot.modules." + i.split(".")[0])


executor.start_polling(dp, skip_updates=True)
