#using standard Python libraries to do slicing


from data_model import FrenchDeck, Card


if __name__ == '__main__':
    deck = FrenchDeck()
    print(deck[:3])
    print(deck[12::13])
    print("*************")

    # We can iterate through the deck
    # because we implemented __getitem__ special method
    for card in deck:
        print(card)

    print("*************")
    for card in reversed(deck):
        print(card)
    print("*************")
    assert Card('Q','hearts') in deck 
    assert Card('7','beasts') in deck