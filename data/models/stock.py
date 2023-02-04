from data import BaseModel, ForeignKeyField, IntegerField, Product


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
