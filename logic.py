from card import makeStandardDeck, shuffleDeck, dealHand, deal

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

def hand_value(hand):
    if is_royal_flush(hand):
        return (10, "Royal Flush")
    elif is_straight_flush(hand):
        return (9, "Straight Flush")
    elif is_four_of_a_kind(hand):
        return (8, "Four of a Kind")
    elif is_full_house(hand):
        return (7, "Full House")
    elif is_flush(hand):
        return (6, "Flush")
    elif is_straight(hand):
        return (5, "Straight")
    elif is_three_of_a_kind(hand):
        return (4, "Three of a Kind")
    elif is_two_pair(hand):
        return (3, "Two Pair")
    elif is_one_pair(hand):
        return (2, "One Pair")
    else:
        return (1, "High Card")

def playGame():
    # Create a deck, shuffle it, and deal hands
    testDeck = makeStandardDeck()
    shuffleDeck(testDeck)

    # Deal 2 cards to each player
    hand1 = dealHand(testDeck, 2)
    hand2 = dealHand(testDeck, 2)

    print("Hand 1: ", [str(card) for card in hand1])
    print("Hand 2: ", [str(card) for card in hand2])

    # Betting round 1
    bet()

    # Deal 3 community cards (The Flop)
    card_on_table = dealHand(testDeck, 3)
    print("Table Cards: ", [str(card) for card in card_on_table])

    # Betting Round 2
    bet()

    #Deal Turn (Fourth Street)
    card_on_table.append(deal(testDeck))
    bet()

    #Deal River (Fifth Street)
    card_on_table.append(deal(testDeck))
    bet()

    # Combine hands with community cards
    combined_hand1 = hand1 + card_on_table
    combined_hand2 = hand2 + card_on_table

    # Evaluate hand values
    value1 = hand_value(combined_hand1)
    value2 = hand_value(combined_hand2)

    print("Hand 1 Value: ", value1)
    print("Hand 2 Value: ", value2)

    # Determine the winner
    if value1[0] > value2[0]:
        print("Hand 1 wins!")
    elif value1[0] < value2[0]:
        print("Hand 2 wins!")
    else:
        print("It's a tie!")

def bet():
    print("filler function; will implement later")

# Run the game
playGame()