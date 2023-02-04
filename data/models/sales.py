from datetime import datetime

from data import BaseModel, DateTimeField, ForeignKeyField, Product


class Sales(BaseModel):
    timestamp = DateTimeField(default=datetime.now())
    products = ForeignKeyField(Product, backref="sales")
