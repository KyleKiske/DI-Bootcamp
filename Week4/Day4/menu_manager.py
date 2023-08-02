from menu_item import manage_connection

class MenuManager:
    def get_by_name(self, name):
        query = f"""SELECT item_name, item_price FROM menu_items
                        WHERE item_name = '{name}'
                        LIMIT 1"""
        data = manage_connection(query, "select")
        if len(data) == 0:
            return None
        else:
            print(data)
            return data
    def all_items(self):
        query = f"""SELECT * FROM menu_items"""
        data = manage_connection(query, "select")
        print(data)
        return data