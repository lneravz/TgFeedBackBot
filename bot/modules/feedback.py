from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, InputFile
from bot import ADMIN_ID, LANG, users_coll, bot, config_coll
from bot.handler import handler
import bot.utils as util
from os import remove


@handler(lambda m: util.chat_type_control(m, ["private"]) and m.reply_to_message, commands=["send"])
async def send_feedback(msg: Message):
    try:
        util.user_check(msg, users_coll)
        user_db = util.get_obj(str(msg.from_user.id), users_coll)
        if user_db.get("status", 1) == 0:
            return await msg.answer(LANG["YOU_BANNED"])
        interval = config_coll.find_one({"_id": "config"}).get("interval", 0)
        if interval > int(int(msg.date.timestamp()) - user_db["last_feedback_time"]):
            return await msg.answer(
                LANG["TIME_INTERVAL"].format(
                    m=int(interval/60) - int((int(msg.date.timestamp()) - user_db["last_feedback_time"])/60) + 1))
        reply_id = msg.reply_to_message.message_id
        fb = await bot.copy_message(ADMIN_ID, msg.chat.id, reply_id)
        await bot.send_message(ADMIN_ID, "<a href='tg://user?id=" + user_db["_id"] +"'>" + LANG["SENDER"] + "</a>\nid: <code>" + user_db["_id"] + "</code>",
                               reply_to_message_id=fb.message_id)
        users_coll.update_one({"_id": user_db["_id"]}, {"$set": {"last_feedback_time": int(msg.date.timestamp())}})
        await msg.answer(LANG["FEEDBACK_SENT"])
    except:
        text = util.line_by_line_text(
            "file: bot/modules/feedback.py",
            "function: send_feedback", 
            "date: " + str(msg.date),
            "chat id: " + str(msg.chat.id),
            "user id: " + str(msg.from_user.id)
        )
        file_name = util.get_traceback(text)
        try:
            new_msg = await msg.answer_document(InputFile(file_name))
            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton(LANG["REPORT"], util.report_url(new_msg)))
            await new_msg.edit_reply_markup(markup)
        except:
            with open(file_name, "r") as file:
                print(file.read())
                file.close()
        finally:
            remove(file_name)



@handler(lambda m: util.chat_type_control(m, ["private"]) and m.reply_to_message and str(m.from_user.id) == ADMIN_ID, commands=["answer"])
async def answer_function(msg: Message):
    try:
        util.user_check(msg, users_coll)
        if len(msg.text.split()) != 2:
            return await msg.answer(LANG["WRONG_FORMAT_ANSWER"])
        reply_id = msg.reply_to_message.message_id
        user_id = msg.text.split(" ", 1)[-1]
        try:
            await bot.copy_message(user_id, msg.chat.id, reply_id)
        except:
            return await msg.answer(LANG["WRONG_USER_ID"])
        await msg.answer(LANG["ANSWER_SENT"].format(uid=user_id))
    except:
        text = util.line_by_line_text(
            "file: bot/modules/feedback.py",
            "function: answer_feedback", 
            "date: " + str(msg.date),
            "chat id: " + str(msg.chat.id),
            "user id: " + str(msg.from_user.id)
        )
        file_name = util.get_traceback(text)
        try:
            new_msg = await msg.answer_document(InputFile(file_name))
            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton(LANG["REPORT"], util.report_url(new_msg)))
            await new_msg.edit_reply_markup(markup)
        except:
            with open(file_name, "r") as file:
                print(file.read())
                file.close()
        finally:
            remove(file_name)
