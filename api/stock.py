from data import Product, Stock


class StockInfo:
    def __init__(self, id: int, name: str, quantity: int) -> None:
        self.id = id
        self.name = name
        self.quantity = quantity


def new(product_id: int, quantity: int) -> Stock | Exception:
    try:
        product = Product.get_by_id(product_id)
        stock = Stock.get_or_create(product=product.id, quantity=quantity)
        stock.save()
        return stock
    except Exception as e:
        print(e)
        return e


def delete(stock_id: int) -> None:
    try:
        Stock.delete_by_id(stock_id)
    except Exception as e:
        print(e)


def get_all() -> list[StockInfo]:
    data = []
    for item in Stock.select(
        Product.id, Product.name, Stock.quantity  # type: ignore
    ).join(Product):
        info = StockInfo(
            id=item.product.id, name=item.product.name, quantity=item.quantity
        )
        data.append(info.__dict__)

    return data
