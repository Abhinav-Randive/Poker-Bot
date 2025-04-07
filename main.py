# deal cards

import card as c

# Create a shuffled deck
deck = c.makeStandardDeck()
c.shuffleDeck(deck)
#c.printDeck(deck)

def playGame():



    #Deal cards to each player


    round()

    table = []

    #Deal flop
    table.append(c.deal(deck))
    table.append(c.deal(deck))
    table.append(c.deal(deck))

    #Deal turn
    table.append(c.deal(deck))

    #Deal river
    table.append(c.deal(deck))

    c.printDeck(table)

def round():
    #prompt each player to bet
    print("test")


def fold():
    print("Folded.")

def check():
    print("Check.")

def bet(int):
    print("bet", int)

def call():
    print("Called.")

def raisePoker():
    print("Raised.")