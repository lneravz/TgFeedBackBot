from aiogram.types import Message
from traceback import format_exc
from datetime import datetime
from bot import REPORT_URL


def chat_type_control(msg: Message ,chat_types: list):
    chat_type: str = msg.chat.type
    if chat_type in chat_types:
        return True
    else:
        return False


def user_check(msg: Message, db):
    user_id, full_name, date = str(msg.from_user.id), msg.from_user.full_name, int(msg.date.timestamp())
    dt = msg.date
    id_list = list(db.find().distinct("_id"))
    new_index = len(id_list)
    if user_id not in id_list:
        db.insert_one({
            "_id": user_id,
            "index": new_index,
            "full_name": full_name,
            "datetime": dt,
            "feedback_number": 0,
            "status": 1,
            "last_feedback_time": 0
        })


def get_traceback(info: str):
    tb = format_exc()
    file_name = "error.log"
    with open(file_name, "w") as file:
        file.write(info + "\n\n" + "/\\"*10 + "\n\n")
        file.write(tb)
        file.write("\n" + "\\/"*10)
        file.close()
    return file_name
    

def line_by_line_text(*args):
    return "".join([line + "\n" for line in args])
    

def report_url(msg: Message):
    return REPORT_URL + msg.document.file_id


def get_obj(object_id: str, db):
    return dict(db.find_one({"_id": object_id}))
