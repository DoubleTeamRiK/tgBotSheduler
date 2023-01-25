import os
from peewee import *

basedir = os.path.abspath(os.path.dirname(__file__))

db = SqliteDatabase(os.path.join(basedir, 'dbmassage.db'))


class BaseModel(Model):
    class Meta:
        database = db


class Position(BaseModel):
    pos_title = CharField(max_length=50)


class Theeme(BaseModel):
    theeme_title = CharField(max_length=50)


class Users(BaseModel):
    user_tg_id = IntegerField()
    user_name = CharField(max_length=50)    


class MasterProfile(BaseModel):
    name = CharField()
    theeme = ForeignKeyField(Theeme)
    about_yourself = TextField()
    location = CharField()
    user_id = ForeignKeyField(Users.user_tg_id)
    position = ForeignKeyField(Position.pos_title)


class PhotoMasters(BaseModel):
    path_to_photo = CharField()
    profile = ForeignKeyField(MasterProfile)


# class SheduleMasters(BaseModel):
#     master_id = ForeignKeyField()
#     client_id = IntegerField()
#     date_session = DateField()
#     time_session = TimeField()


db.connect()
db.create_tables([Position, Users, Theeme, MasterProfile, PhotoMasters])
# theemes = ['Косметолог', 'Визажист', 'Массаж', 'Маникюр/Педикюр', 'Брови', 'Депиляция']
# for theeme in theemes:
#     th = Theeme(theeme_title=theeme)
#     th.save()