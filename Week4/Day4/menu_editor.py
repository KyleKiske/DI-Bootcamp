from menu_manager import MenuManager
from menu_item import MenuItem

menu_manager = MenuManager()
def show_user_menu():
    menu = """
\tMenu
View an Item (V)
Add an Item (A)
Delete an Item (D)
Update an Item (U)
Show the Menu (S)
Exit (X)"""
    while True :
        print(menu)
        menu_choice = input("  :  ").strip().lower()[0]
        if menu_choice not in ('v', 'a', 'd', 'u', 's', 'x') :
            continue
        else :
            break
    
    if menu_choice == 'a':
        add_item_to_menu()
    elif menu_choice == 'd':
        remove_item_from_menu()
    elif menu_choice == 'u':
        update_item_from_menu()
    elif menu_choice == 's':
        show_restaurant_menu()
    elif menu_choice == 'v':
        view_item()
    else:
        return False
    return True

def add_item_to_menu():
    name = input("Please write item name: ")
    value =int(input("Please write item cost: "))
    m_item = MenuItem(name, value)
    m_item.save()
def remove_item_from_menu():
    name = input("Please write item name: ")
    value =int(input("Please write item cost: "))
    m_item = MenuItem(name, value)
    m_item.delete()
def update_item_from_menu():
    name = input("Please write item name to find: ")
    value =int(input("Please write item cost to find: "))
    new_name = input("Please write new item name: ")
    new_value =int(input("Please write new item cost: "))
    m_item = MenuItem(name, value)
    m_item.update(new_name ,new_value)
def show_restaurant_menu():
    menu_manager.all_items()
def view_item():
    name = input("Please write item name to find: ")
    menu_manager.get_by_name(name)

while True:
    loop = show_user_menu()
    if not loop:
        break
