from card import makeStandardDeck, shuffleDeck, dealHand

def is_flush(hand):
    suits = [card.suit for card in hand]
    return len(set(suits)) == 1

def is_straight(hand):
    values = [int(card.value) for card in hand]
    values.sort()
    return values == list(range(values[0], values[0] + 5))

def is_straight_flush(hand):
    return is_flush(hand) and is_straight(hand)

def is_royal_flush(hand):
    values = [int(card.value) for card in hand]
    return is_straight_flush(hand) and values[0] == 1 and values[-1] == 13

def is_three_of_a_kind(hand):
    values = [int(card.value) for card in hand]
    for value in values:
        if values.count(value) == 3:
            return True
    return False

def is_four_of_a_kind(hand):
    values = [int(card.value) for card in hand]
    for value in values:
        if values.count(value) == 4:
            return True
    return False

def is_five_of_a_kind(hand):
    values = [int(card.value) for card in hand]
    for value in values:
        if values.count(value) == 5:
            return True
    return False

def is_full_house(hand):
    values = [int(card.value) for card in hand]
    for value in values:
        if values.count(value) == 3:
            for value in values:
                if values.count(value) == 2:
                    return True
    return False

def is_two_pair(hand):
    values = [int(card.value) for card in hand]
    pairs = 0
    for value in values:
        if values.count(value) == 2:
            pairs += 1
    return pairs == 2

def is_one_pair(hand):
    values = [int(card.value) for card in hand]
    pairs = 0
    for value in values:
        if values.count(value) == 2:
            pairs += 1
    return pairs == 1

def is_high_card(hand):
    values = [int(card.value) for card in hand]
    pairs = 0
    for value in values:
        if values.count(value) == 1:
            pairs += 1
    return pairs == 5

# Create a deck, shuffle it, and deal a hand
testDeck = makeStandardDeck()
shuffleDeck(testDeck)

# Deal a hand and print it
hand = dealHand(testDeck)
print("Hand: ", [str(card) for card in hand])

# Test hand comparisons
print("Is Flush? ", is_flush(hand))
print("Is Straight? ", is_straight(hand))
print("Is Straight Flush? ", is_straight_flush(hand))
print("Is Royal Flush? ", is_royal_flush(hand))
print("Is Three of a Kind? ", is_three_of_a_kind(hand))
print("Is Four of a Kind? ", is_four_of_a_kind(hand))