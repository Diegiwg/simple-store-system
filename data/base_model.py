from peewee import Model

from data import database_instance


class BaseModel(Model):
    class Meta:
        database = database_instance
