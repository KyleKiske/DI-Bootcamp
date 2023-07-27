import random

# Part 1 : Quizz :

# What is a class?
# A template to create complex data structures 

# What is an instance?
# A single instance of a class is object.

# What is encapsulation?
# Restriction on access to class fields and methods for better protection of data. (__ _)

# What is abstraction?
# An ability to hide complex implementation of inner workings of a class with simple user friendly interface.

# What is inheritance?
# Process by which class can inherit properties from parent class and add new features without changing parent.

# What is multiple inheritance?
# Multiple child classes for single parent class.

# What is polymorphism?
# Different classes can have similar named methods to execute them in the same place.

# What is method resolution order or MRO?
# The order in which a method is searched for in a classes hierarchy 

# Part 2: Create A Deck Of Cards Class.

class Card:
    def __init__(self, suit, value) -> None:
        self.suit = suit
        self.value = value
    def __str__(self) -> str:
        return (f"{self.value} of {self.suit}")

class Deck:

    def __init__(self) -> None:
        self.cards = []
        for x in ("Spades", "Clubs", "Diamonds", "Hearts"):
            for j in ("A","2","3","4","5","6","7","8","9","10","J","Q","K"):
                self.cards.append(Card(x, j))
        
    def shuffle(self):
        random.shuffle(self.cards) 
    def deal(self):
        card = self.cards.pop(random.randint(0, len(self.cards)-1))
        return card

deck = Deck()
for x in deck.cards:
    print(x)
deck.shuffle()
print("\nAfter shuffle\n")
for x in deck.cards:
    print(x)

print(f"Number of cards in deck {len(deck.cards)}")

card_dealt = deck.deal()

print(f"The dealt card is {card_dealt}")
print(f"Number of cards in deck after {card_dealt} was dealt = {len(deck.cards)}")
for x in range(len(deck.cards)):
    card_dealt = deck.deal()
    print(f"The dealt card is {card_dealt}")
    print(f"Number of cards in deck after {card_dealt} was dealt = {len(deck.cards)}")
