from random import choice

class Game:

    @staticmethod
    def get_user_item():
        item = input("Please choose (r)ock, (p)aper or (s)cissors ").strip().lower()[0]
        while (item != 'r' and item != 'p' and item != 's'):
            print(item)
            print("Your input isn't 'rock' 'paper' or 'scissors'")
            item = input("Please choose (r)ock, (p)aper or (s)cissors ").strip().lower()[0]
        return item
    @staticmethod
    def get_computer_item():
        comp_item = choice(["r", "p", "s"])
        return comp_item
    @staticmethod
    def get_game_result(user_item, computer_item):
        if (user_item == computer_item):
            return "draw"
        elif (user_item == 'r' and computer_item == "s") or (user_item == 's' and computer_item == "p") or (user_item == 'p' and computer_item == "r"):
            return "win"
        else:
            return "loss"
        
    def play(self):
        description = {"r": "rock",
                       "p": "paper",
                       "s": "scissors"}
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)
        user_choice = description[user_item]
        computer_choice = description[computer_item]
        if result == 'draw':
            result_verb = 'drew'
        if result == 'win':
            result_verb = 'won'
        if result == 'loss':
            result_verb = 'lost'
        print(f"You selected {user_choice}, computer selected {computer_choice}, you {result_verb}!")
        return result