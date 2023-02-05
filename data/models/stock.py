from data import BaseModel, ForeignKeyField, IntegerField, Product


class Stock(BaseModel):
    product = ForeignKeyField(Product, unique=True, backref="stock")
    quantity = IntegerField()
