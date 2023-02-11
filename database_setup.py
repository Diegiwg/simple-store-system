from database import session
from models import Product, Stock

products = session.query(Product).all()
print(products)

stocks = session.query(Stock).all()
print(stocks)
