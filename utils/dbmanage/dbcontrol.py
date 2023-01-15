from .models import Users, Position
from py_log import *


def add_user_to_db(user_id: int, user_name: str, position: int) -> None:
    """save master or client user in DB"""
    if not user_exists(user_id):
        master = Users(user_tg_id=user_id, user_name=user_name, position=position, profile=None)
        master.save()


def user_exists(user_id: int) -> bool:
    """return True if user exists"""
    try:
        query = Users.select().where(Users.user_tg_id == user_id)
        master_ex = query.dicts().execute()
        return len([k for k in master_ex]) > 0
    except Exception as ex:
        logger.exception('error in searching for an existing user in the database', ex)


def get_position(user_id: int) -> str:
    """return user position from DB"""
    try:
        query = Users.select().where(Users.user_tg_id == user_id)
        user_pos = query.dicts().execute()
        return [k for k in user_pos][0]['position']
    except Exception as ex:
        logger.exception('error in searching for an existing user in the database', ex)
