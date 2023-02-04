from peewee import (
    Model,
    CharField,
    FloatField,
    IntegerField,
    DateTimeField,
    ForeignKeyField,
)
from data.instance import db
from datetime import datetime


class BaseModel(Model):
    class Meta:
        database = db


class Product(BaseModel):
    name = CharField(unique=True)
    brand = CharField()
    reference = CharField()
    price = FloatField()


def new_product(name: str, brand: str, reference: str, price: float) -> Product:
    try:
        product = Product.create(
            name=name, brand=brand, reference=reference, price=price
        )
        product.save()
        return product
    except Exception as e:
        print(e)
        return Product.select().where(Product.name == name).get()


class Stock(BaseModel):
    product = ForeignKeyField(Product, unique=True, backref="stock")
    quantity = IntegerField()


def new_stock(product: Product, quantity: int) -> Stock:
    try:
        stock = Stock.create(product=product, quantity=quantity)
        stock.save()
        return stock
    except Exception as e:
        print(e)
        return Stock.select().where(Stock.product == product).get()


class Sales(BaseModel):
    timestamp = DateTimeField(default=datetime.now())
    products = ForeignKeyField(Product, backref="sales")
