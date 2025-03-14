from card import makeStandardDeck, shuffleDeck, dealHand

def card_value(card):
    face_card_values = {'Ace': 1, 'Jack': 11, 'Queen': 12, 'King': 13}
    return face_card_values.get(card.value, int(card.value) if card.value.isdigit() else card.value)

def is_flush(hand):
    suits = [card.suit for card in hand]
    return len(set(suits)) == 1

def is_straight(hand):
    values = [card_value(card) for card in hand]
    values.sort()
    return values == list(range(values[0], values[0] + 5))

def is_straight_flush(hand):
    return is_flush(hand) and is_straight(hand)

def is_royal_flush(hand):
    values = [card_value(card) for card in hand]
    return is_straight_flush(hand) and values[0] == 1 and values[-1] == 13

def is_three_of_a_kind(hand):
    values = [card_value(card) for card in hand]
    for value in values:
        if values.count(value) == 3:
            return True
    return False

def is_four_of_a_kind(hand):
    values = [card_value(card) for card in hand]
    for value in values:
        if values.count(value) == 4:
            return True
    return False

def is_five_of_a_kind(hand):
    values = [card_value(card) for card in hand]
    for value in values:
        if values.count(value) == 5:
            return True
    return False

def is_full_house(hand):
    values = [card_value(card) for card in hand]
    for value in values:
        if values.count(value) == 3:
            for value in values:
                if values.count(value) == 2:
                    return True
    return False

def is_two_pair(hand):
    values = [card_value(card) for card in hand]
    pairs = 0
    for value in values:
        if values.count(value) == 2:
            pairs += 1
    return pairs == 2

def is_one_pair(hand):
    values = [card_value(card) for card in hand]
    pairs = 0
    for value in values:
        if values.count(value) == 2:
            pairs += 1
    return pairs == 1

def is_high_card(hand):
    values = [card_value(card) for card in hand]
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
hand2 = dealHand(testDeck)
#print("Hand: ", [str(card) for card in hand])



def handvalue(hand):
    if is_royal_flush(hand):
        return 10
    elif is_straight_flush(hand):
        return 9
    elif is_four_of_a_kind(hand):
        return 8
    elif is_full_house(hand):
        return 7
    elif is_flush(hand):
        return 6
    elif is_straight(hand):
        return 5
    elif is_three_of_a_kind(hand):
        return 4
    elif is_two_pair(hand):
        return 3
    elif is_one_pair(hand):
        return 2
    elif is_high_card(hand):
        return 1
    else:
        return 0

# Test hand comparisons

hand = dealHand(testDeck)
hand2 = dealHand(testDeck)

print("Hand 1: ", [str(card) for card in hand])
print("Hand 2: ", [str(card) for card in hand2])

value1 = handvalue(hand)
value2 = handvalue(hand2)

if value1 > value2:
    print("Hand 1 wins!")
elif value1 < value2:
    print("Hand 2 wins!")
else:
    print("It's a tie!")    