from data import database_instance, Product, Stock

database_instance.connect()

database_instance.create_tables([Product, Stock])

s: Stock = Stock.get_by_id(2)
s.save()

print(s.product.name)

database_instance.close()
