from data import database_instance
from models.product import Product
from models.stock import Stock

database_instance.connect()

database_instance.create_tables([Product, Stock])

database_instance.close()
