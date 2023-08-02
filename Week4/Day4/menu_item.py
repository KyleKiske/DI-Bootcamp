import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'postgres'
DATABASE = 'Restaurant'

def manage_connection(query, type) :
    connection = None
    try : 
        connection = psycopg2.connect(
            database="Restaurant", 
            user='postgres',
            password='postgres',
            host='localhost', 
            port='5432'
        )

        with connection:
            with connection.cursor() as cursor: 
                cursor.execute(query)
                if type == "insert" :
                    connection.commit()
                elif type == "select" :
                    return cursor.fetchall()
    except Exception as e :
        print(e)
    finally :
        if connection != None:
            connection.close() 

class MenuItem:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
    def save(self):
        query = f"""INSERT INTO menu_items(item_name, item_price)
                VALUES ('{self.name}', {self.price})"""
        manage_connection(query, "insert")
    def update(self, new_name, new_price):
        query = f"""UPDATE menu_items
                SET item_name = '{new_name}', item_price = {new_price}
                WHERE item_name = '{self.name}' AND item_price = {self.price}"""
        manage_connection(query, "insert")
    def delete(self):
        query = f"""DELETE FROM menu_items
                WHERE item_name = '{self.name}' AND item_price = {self.price}"""
        manage_connection(query, "insert")