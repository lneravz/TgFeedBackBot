from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from bot import ADMIN_ID, LANG, config_coll
from bot.handler import handler
import bot.utils as util
from os import remove


@handler(lambda m: util.chat_type_control(m, ["private"]) and str(m.from_user.id) == ADMIN_ID, commands=["time"])
async def set_time_interval(msg: Message):
    try:
        if len(msg.text.split()) != 2:
            return await msg.answer(LANG["WRONG_FORMAT_TIME"])
        try:
            m = int(msg.text.split(" ", 1)[-1]) * 60
        except:
            return await msg.answer(LANG["WRONG_FORMAT_TIME"])
        config_coll.update_one({"_id": "config"}, {"$set": {"interval": m}})
        await msg.answer(LANG["INTERVAL_SET"])
    except:
        text = util.line_by_line_text(
            "file: bot/modules/config.py",
            "function: set_time_interval", 
            "date: " + str(msg.date),
            "chat id: " + str(msg.chat.id),
            "user id: " + str(msg.from_user.id)
        )
        file_name = util.get_traceback(text)
        try:
            new_msg = await msg.answer_document(file_name)
            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton(LANG["REPORT"], util.report_url(new_msg)))
            await new_msg.edit_reply_markup(markup)
        except:
            with open(file_name, "r") as file:
                print(file.read())
                file.close()
        finally:
            remove(file_name)

