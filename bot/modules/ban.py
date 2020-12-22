from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from bot import ADMIN_ID, LANG, users_coll
from bot.handler import handler
import bot.utils as util
from os import remove


@handler(lambda m: util.chat_type_control(m, ["private"]) and str(m.from_user.id) == str(ADMIN_ID), commands=["ban"])
async def ban_user(msg: Message):
    try:
        if len(msg.text.split()) != 2:
            return await msg.answer(LANG["WRONG_FORMAT_BAN"])
        user_id = msg.text.split(" ", 1)[-1]
        if user_id not in list(users_coll.find().distinct("_id")):
            return await msg.answer(LANG["USER_ID_NOT_FOUND"])
        user_db = util.get_obj(user_id, users_coll)
        if user_db.get("status", 1) == 0:
            return await msg.answer(LANG["ALREADY_BANNED"])
        users_coll.update_one({"_id": user_id}, {"$set": {"status": 0}})
        await msg.answer(LANG["BAN_COMPLETED"].format(uid=user_id))
    except:
        text = util.line_by_line_text(
            "file: bot/modules/ban.py",
            "function: ban_user", 
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


@handler(lambda m: util.chat_type_control(m, ["private"]) and str(m.from_user.id) == str(ADMIN_ID), commands=["unban"])
async def unban_user(msg: Message):
    try:
        if len(msg.text.split()) != 2:
            return await msg.answer(LANG["WRONG_FORMAT_UNBAN"])
        user_id = msg.text.split(" ", 1)[-1]
        if user_id not in list(users_coll.find().distinct("_id")):
            return await msg.answer(LANG["USER_ID_NOT_FOUND"])
        user_db = util.get_obj(user_id, users_coll)
        if user_db.get("status", 1) == 1:
            return await msg.answer(LANG["ALREADY_NOT_BANNED"])
        users_coll.update_one({"_id": user_id}, {"$set": {"status": 1}})
        await msg.answer(LANG["UNBAN_COMPLETED"].format(uid=user_id))
    except:
        text = util.line_by_line_text(
            "file: bot/modules/ban.py",
            "function: unban_user", 
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
