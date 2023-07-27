from game import Game

def get_user_menu_choice():
    print("\tMenu")
    print("(g) Play a new game")
    print("(i) Show scores")
    print("(x) Show scores and exit")
    menu_choice = input(":  ").strip().lower()[0]
    while (menu_choice != 'g' and menu_choice != 'i' and menu_choice != 'x'):
            print(menu_choice)
            print("Your input isn't 'g' 'i' or 'x'")
            print("\tMenu")
            print("(g) Play a new game")
            print("(i) Show scores")
            print("(x) Show scores and exit")
            menu_choice = input("  :  ").strip().lower()[0]
    return menu_choice
def print_results(results):
    print("Current score:")
    print(results)
    
def main():
    results = {"win" : 0,
               "loss" : 0,
               "draw" : 0}
    while True:
        choice = get_user_menu_choice()
        if (choice == 'x'):
            break
        elif (choice == 'g'):
            new_Game = Game()
            result = new_Game.play()
            results[result] += 1
        elif (choice == 'i'):
             print_results(results)
    print_results(results)
    print("Thank you for playing")

main()