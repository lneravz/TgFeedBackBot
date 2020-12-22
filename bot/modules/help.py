from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from bot import ADMIN_ID, LANG, users_coll
from bot.handler import handler
import bot.utils as util
from os import remove


@handler(lambda m: util.chat_type_control(m, ["private"]), commands=["start"])
async def start_command(msg: Message):
    try:
        util.user_check(msg, users_coll)
        await msg.answer(LANG["START_MESSAGE"], disable_web_page_preview=True)
    except:
        text = util.line_by_line_text(
            "file: bot/modules/help.py",
            "function: start_command", 
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
    
    
@handler(lambda m: util.chat_type_control(m, ["private"]), commands=["help"])
async def help_command(msg: Message):
    try:
        util.user_check(msg, users_coll)
        if str(msg.from_user.id) == str(ADMIN_ID):
            return await msg.answer(LANG["HELP_OWNER_MESSAGE"])
        await msg.answer(LANG["HELP_MESSAGE"])
    except:
        text = util.line_by_line_text(
            "file: bot/modules/help.py",
            "function: help_command", 
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