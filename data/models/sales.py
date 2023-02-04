from data import BaseModel, Product, DateTimeField, ForeignKeyField
from datetime import datetime


class Sales(BaseModel):
    timestamp = DateTimeField(default=datetime.now())
    products = ForeignKeyField(Product, backref="sales")
