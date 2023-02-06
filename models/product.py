from data import CharField, FloatField
from models import BaseModel


class Product(BaseModel):
    name = CharField(unique=True)
    brand = CharField()
    reference = CharField()
    price = FloatField()
