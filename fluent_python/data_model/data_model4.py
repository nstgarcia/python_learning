from data_model import FrenchDeck

suite_values = dict(spades=3, hearts=2,diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suite_values) + suite_values[card.suit]

deck= FrenchDeck()

for card in sorted(deck, key=spades_high):
    print(card)