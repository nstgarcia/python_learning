from random import choice
from data_model import FrenchDeck

#using standard python library to randomly select an item from a sequence

print("using choice ..")
deck = FrenchDeck()
print(choice(deck))
print(choice(deck))