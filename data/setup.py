from instance import db
from models import Product, Stock

db.connect()

db.create_tables([Product, Stock])

db.close()
