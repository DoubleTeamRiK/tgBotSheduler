import os
from peewee import *

basedir = os.path.abspath(os.path.dirname(__file__))

db = SqliteDatabase(os.path.join(basedir, 'dbmassage.db'))


class BaseModel(Model):
    class Meta:
        database = db


class Masters(BaseModel):
    pass


class Clients(BaseModel):
    pass


class SheduleMassage(BaseModel):
    pass
