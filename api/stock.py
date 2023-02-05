from data import Product, Stock


class StockInfo:
    def __init__(self, id: int, name: str, quantity: int) -> None:
        self.id = id
        self.name = name
        self.quantity = quantity


def new_stock(product: Product, quantity: int) -> Stock | Exception:
    try:
        stock = Stock.create(product=product, quantity=quantity)
        stock.save()
        return stock
    except Exception as e:
        print(e)
        return e


def get_stock_list() -> list[StockInfo]:
    data = []
    for item in Stock.select(
        Product.id, Product.name, Stock.quantity  # type: ignore
    ).join(Product):
        info = StockInfo(
            id=item.product.id, name=item.product.name, quantity=item.quantity
        )
        data.append(info.__dict__)

    return data
