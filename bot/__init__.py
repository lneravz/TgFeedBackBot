from pymongo.errors import ConfigurationError, DuplicateKeyError, InvalidURI, OperationFailure, WriteConcernError
from aiogram.utils.exceptions import Unauthorized
from aiogram import Bot, Dispatcher, executor
from asyncio import get_event_loop
from pymongo import MongoClient
from os import environ as env
from os import listdir
from json import load
from time import time

#LANGUAGE DICTIONARIES
TR_LANG = {}
EN_LANG = {}

#FILE PATHS
CONFIG_FILE_PATHS = "./config.json"
LANGUAGES_DIR = "./bot/languages/"

for lang_json in listdir(LANGUAGES_DIR):
    if not lang_json.endswith(".json"):
        continue
    globals()[lang_json.split(".")[0] + "_LANG"] = load(file:=open(LANGUAGES_DIR + lang_json))
    file.close()


#VARIABLES
with open(CONFIG_FILE_PATHS, "r") as file:
    config_dict = dict(load(file))
    file.close()

BOT_TOKEN = env.get("BOT_TOKEN", config_dict.get("BOT_TOKEN", None))
MONGO_STRING = env.get("MONGO_STRING", config_dict.get("MONGO_STRING", None))
MONGO_PASSWORD = env.get("MONGO_PASSWORD", config_dict.get("MONGO_PASSWORD", None))
ADMIN_ID = env.get("ADMIN_ID", config_dict.get("ADMIN_ID", None))
LANGUAGE = env.get("LANGUAGE", config_dict.get("LANGUAGE", "EN"))
MONGO = MONGO_STRING.replace("<password>", MONGO_PASSWORD)
LANG = globals()[LANGUAGE + "_LANG"]
REPORT_URL = "https://t.me/lneravzbot?start="


if None in (BOT_TOKEN, MONGO_STRING, MONGO_PASSWORD, ADMIN_ID):
    raise Exception("[!] Missing required variable")

bot = Bot(BOT_TOKEN, parse_mode="html")
try:
    get_event_loop().run_until_complete(bot.get_me())
except Unauthorized:
    raise Exception("[!] Invalid BOT_TOKEN")

dp = Dispatcher(bot)

try:
    mongo = MongoClient(MONGO)
    database = mongo["LneravzFeedBackBot"]
    config_coll = database["config"]
    users_coll = database["users"]
    if "config" not in config_coll.find().distinct("_id"):
        config_coll.insert_one({"_id": "config", "date": int(time()), "interval": 0})
except (ConfigurationError, DuplicateKeyError, InvalidURI, OperationFailure, WriteConcernError):
    raise Exception("[!] Invalid MONGO_STRING or MONGO_PASSWORD")

