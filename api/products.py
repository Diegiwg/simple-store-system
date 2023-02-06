from models.product import Product


def new(name: str, brand: str, reference: str, price: float) -> Product | Exception:
    try:
        product = Product.create(
            name=name, brand=brand, reference=reference, price=price
        )
        product.save()
        return product
    except Exception as e:
        print(e)
        return e


def delete(stock_id: int) -> None:
    try:
        Product.delete_by_id(stock_id)
    except Exception as e:
        print(e)


def get_all():
    return [item.__data__ for item in Product.select()]
