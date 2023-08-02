from menu_item import MenuItem
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

class MenuManager:
    def get_by_name(self, name):
        try:
            with connection:
                with connection.cursor() as curs:
                    query = f"""SELECT item_name, item_price FROM menu_items
                        WHERE item_name = '{name}'
                        LIMIT 1"""
                    curs.execute(query)
                    data = curs.fetchall()
                    if len(data) == 0:
                        return None
                    else:

                        print(data)
                        return data
        except Exception as err:
            print(err)

    def all_items(self):
        try:
            with connection:
                with connection.cursor() as curs:
                    query = f"""SELECT * FROM menu_items"""
                    curs.execute(query)
                    data = curs.fetchall()
                    print(data)
                    return data
        except Exception as err:
            print(err)

# item = MenuItem('Burger', 35)
# item.save()
# item.delete()
# item.update('Veggie Burger', 37)
# item2 = MenuManager.get_by_name('Veggie Burger')
# items = MenuManager.all_items()

# connection.close()