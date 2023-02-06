from data import ForeignKeyField, IntegerField
from models import BaseModel, product


class Stock(BaseModel):
    product = ForeignKeyField(product.Product, unique=True, backref="stock")
    quantity = IntegerField()
