from data import database_instance, Product, Stock

database_instance.connect()

database_instance.create_tables([Product, Stock])

database_instance.close()
