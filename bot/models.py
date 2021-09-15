from peewee import Model, IntegerField, BooleanField, CharField
from playhouse.sqliteq import SqliteQueueDatabase
from configparser import ConfigParser


# parse config
config = ConfigParser()
config.read('config.ini')
database_path = config.get('database', 'sqlite')


# database connection
database = SqliteQueueDatabase(database_path)


# base model for other models
class BaseModel(Model):
    class Meta:
        database = database


# model that represents user
class User(BaseModel):
    user_id = IntegerField(primary_key=True, unique=True)
    active = BooleanField(default=True)
    requests = IntegerField(default=0)


class Source(BaseModel):
    name = CharField(max_length=40)
    users = IntegerField(default=0)
