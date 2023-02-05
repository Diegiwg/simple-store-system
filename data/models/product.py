from data import BaseModel, CharField, FloatField


class Product(BaseModel):
    name = CharField(unique=True)
    brand = CharField()
    reference = CharField()
    price = FloatField()
