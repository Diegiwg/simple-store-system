from models.stock import Stock
from models.product import Product
import api


class ProductInfo:
    def __init__(self, id, name, brand, reference, price) -> None:
        self.id = id
        self.name = name
        self.brand = brand
        self.reference = reference
        self.price = price


def new(name: str, brand: str, reference: str, price: float) -> Product:
    product: Product = Product.get_or_create(
        name=name, brand=brand, reference=reference, price=price
    )
    return product


def delete(id: int) -> None:
    try:
        exist = Stock.select().where(Stock.product == id).get()
        api.stock.delete(exist.id)
    except Exception:
        print("Produto não está vinculado ao estoque")

    Product.delete_by_id(id)


def get_all():
    return [item.__data__ for item in Product.select().order_by(Product.name)]
