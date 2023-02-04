from data import BaseModel, CharField, IntegerField, FloatField


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
