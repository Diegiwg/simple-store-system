from dataclasses import dataclass
from models import Product, Stock
from database import session


def create(name: str, brand: str, reference: str, price: float):
    try:
        product = Product(name=name, brand=brand, reference=reference, price=price)
        session.add(product)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e


def delete(id: int):
    product = session.query(Product).get(id)
    if not product:
        return

    session.delete(product)
    session.commit()


def get_all():
    products = session.query(Product).order_by(Product.name).all()
    return products
