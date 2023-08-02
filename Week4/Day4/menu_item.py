import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'postgres'
DATABASE = 'Restaurant'

connection = psycopg2.connect(
    host = HOSTNAME,
    user = USERNAME,
    password = PASSWORD,
    database = DATABASE
)

cursor = connection.cursor()

class MenuItem:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
    def save(self):
        try:
            with connection:
                with connection.cursor() as curs:
                    query = f"""INSERT INTO menu_items(item_name, item_price)
                            VALUES ('{self.name}', {self.price})"""
                    curs.execute(query)
                    connection.commit()
        except Exception as err:
            print(err)
    def update(self, new_name, new_price):
        try:
            with connection:
                with connection.cursor() as curs:
                    query = f"""UPDATE menu_items
                            SET item_name = '{new_name}', item_price = {new_price}
                            WHERE item_name = '{self.name}' AND item_price = {self.price}"""
                    curs.execute(query)
                    connection.commit()
        except Exception as err:
            print(err)
    def delete(self):
        try:
            with connection:
                with connection.cursor() as curs:
                    query = f"""DELETE FROM menu_items
                            WHERE item_name = '{self.name}' AND item_price = {self.price}"""
                    curs.execute(query)
                    connection.commit()
        except Exception as err:
            print(err)
    
# item = MenuItem('Burger', 35)
# item.save()

# connection.close()