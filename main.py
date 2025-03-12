# deal cards

import card as c
import random

# Create a shuffled deck
deck = c.makeStandardDeck()
random.shuffle(deck)

#print(deck[1].printCard())
c.printDeck(deck)