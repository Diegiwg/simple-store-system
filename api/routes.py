import random

from nicegui import app

from data import Product, new_product, Stock


@app.get("/api/random/{max}")
def generate_random_number(max: int):
    return {"min": 0, "max": max, "value": random.randint(0, max)}


@app.get("/api/products")
def get_products():
    return [item.__data__ for item in Product.select()]


@app.get("/api/stock")
def get_stock():
    data = list()
    for item in Stock.select(Product.id, Product.name, Stock.quantity).join(Product):
        data.append(
            {
                "id": item.product.id,
                "name": item.product.name,
                "quantity": item.quantity,
            }
        )

    return data


@app.get("/api/products/create/{name}/{brand}/{reference}/{price}")
def create_product(name: str, brand: str, reference: str, price: float):
    product = new_product(name, brand, reference, price)
    return product.__data__
