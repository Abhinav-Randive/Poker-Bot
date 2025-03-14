# deal cards

import card as c

# Create a shuffled deck
deck = c.makeStandardDeck()
c.shuffleDeck(deck)
#c.printDeck(deck)


def playGame():
    table = []

    table.append(c.deal(deck))
    table.append(c.deal(deck))

    c.printDeck(table)

