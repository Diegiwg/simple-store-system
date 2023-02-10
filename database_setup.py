from data import session
from models.models import Product, Stock

products = session.query(Product).all()
print(products)

# Create a new stock
new_stock = Stock(quantity=10, product_id=products[0].id, product=products[0])
session.add(new_stock)
session.commit()

# Get all with stock
stocks = session.query(Stock).all()
print(stocks)
