from dataclasses import dataclass

from sqlalchemy import update

from database import session
from models import Product, Stock


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


def edit(info: Product):
    session.execute(
        update(Product)
        .where(Product.id == info.id)
        .values(
            name=info.name,
            brand=info.brand,
            reference=info.reference,
            price=info.price,
        )
    )
    session.commit()


def get_all():
    products = session.query(Product).order_by(Product.name).all()
    return products
