from models.product import Product
from models.stock import Stock
import api


class StockInfo:
    def __init__(self, id: int, name: str, quantity: int) -> None:
        self.id = id
        self.name = name
        self.quantity = quantity


def new(product_id: int, quantity: int) -> Stock:
    product = Product.get_by_id(product_id)
    stock = Stock.get_or_create(product=product.id, quantity=quantity)
    return stock


def delete(stock_id: int) -> None:
    Stock.delete_by_id(stock_id)


def get_all() -> list[StockInfo]:
    data = []
    for item in Stock.select(Stock.id, Product.name, Stock.quantity).join(Product):
        data.append(
            StockInfo(
                id=item.id, name=item.product.name, quantity=item.quantity
            ).__dict__
        )

    return data


def get_all_products_without_stock():
    products_in_stock = Product.select().join(Stock)
    products = Product.select()

    data = []
    for product in products:
        in_stock = False
        for stock in products_in_stock:
            if product == stock:
                in_stock = True

        if in_stock == False:
            data.append(
                api.products.ProductInfo(
                    product.id,
                    product.name,
                    product.brand,
                    product.reference,
                    product.price,
                ).__dict__
            )

    return data
