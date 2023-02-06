from datetime import datetime

from data import DateTimeField, ForeignKeyField
from models import BaseModel, product


class Sales(BaseModel):
    timestamp = DateTimeField(default=datetime.now())
    products = ForeignKeyField(product.Product, backref="sales")
