from sqlalchemy import update

from database import session
from models import Product, Stock


def create(product_id: int, quantity: int):
    stock = Stock(product_id=product_id, quantity=quantity)
    session.add(stock)
    session.commit()


def delete(stock_id: int):
    stock = session.query(Stock).get(stock_id)
    if not stock:
        return

    session.delete(stock)
    session.commit()


def edit(info: Stock):
    session.execute(
        update(Stock)
        .where(Stock.id == info.id)
        .values(
            quantity=info.quantity,
        )
    )
    session.commit()


def get_all() -> list[Product]:
    stocks = (
        session.query(Stock)
        .join(Product)
        .add_entity(Product)
        .order_by(Stock.product_id)
        .all()
    )
    return [stock.Product for stock in stocks]


def get_all_without_stock():
    products = (
        session.query(Product).where(Product.stock == None).order_by(Product.id).all()
    )
    return [product.to_dict() for product in products]
