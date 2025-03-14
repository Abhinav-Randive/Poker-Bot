import random

class Card: 
    def __init__(self):
        self.suit = "defaultSuit"
        self.value = "value"
        self.inDeck = True

    def __str__(self):
        return f"{self.value} of {self.suit}"

    def printCard(self):
        print(f"Suit: {self.suit}; Value: {self.value}")

def makeStandardDeck():
    standardDeck = []
    for i in range(4):
        for j in range(1, 14):
            newCard = Card()
            match i:
                case 0:
                    newCard.suit = "heart <3"
                case 1: 
                    newCard.suit = "spade"
                case 2: 
                    newCard.suit = "club"
                case 3: 
                    newCard.suit = "diamond <>"
            
            match j: 
                case 1:
                    newCard.value = "Ace"
                case 11:
                    newCard.value = "Jack"
                case 12:
                    newCard.value = "Queen"
                case 13: 
                    newCard.value = "King"
                case default:
                    newCard.value = str(j)
            standardDeck.append(newCard)
    return standardDeck

def printDeck(deck): 
    for card in deck: 
        card.printCard()

def shuffleDeck(deck): 
    random.shuffle(deck)

def deal(deck):
    return deck.pop()

def dealHand(deck, size=5):
    return [deck.pop() for _ in range(size)]

# Create a deck, shuffle it, and deal a hand
#testDeck = makeStandardDeck()
#shuffleDeck(testDeck)
#printDeck(testDeck)

# Deal a hand and print it
#hand = dealHand(testDeck)
#print("Hand: ", [str(card) for card in hand])  
