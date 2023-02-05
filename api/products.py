from data import Product


def new_product(
    name: str, brand: str, reference: str, price: float
) -> Product | Exception:
    try:
        product = Product.create(
            name=name, brand=brand, reference=reference, price=price
        )
        product.save()
        return product
    except Exception as e:
        print(e)
        return e


def get_products():
    return [item.__data__ for item in Product.select()]
