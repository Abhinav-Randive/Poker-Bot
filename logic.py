from card import makeStandardDeck, shuffleDeck, dealHand, deal
from chips import Chips
import random

botBank = Chips(0, 0, 0, 0)
playerBank = Chips(0, 0, 0, 0)
opponentChips = input("How many chips do you want your opponent to have?: \n")
playerChips = input("How many chips do you want to start with?: \n")
botBank.add(int(opponentChips))
playerBank.add(int(playerChips))
botBank.printChips()
botBank.printTotal()
playerBank.printChips()
playerBank.printTotal()


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

def decide(min, pot):
    decide = random.randint(min,20)
    if decide > 10: 
        val = botBank.giveTotal()
        count = val /1.5
        botBank.playChips(random.randint(1, count))
        print("Bot bet: ", count)
        pot = pot + count
    if decide < 15:
        val = playerBank.giveTotal()
        pot = pot + val
        botBank.allIn()
        print("Bot went all in")
    return pot


def playGame():
    # Creates bot odds a value used to determine actions
    BotOdds = 0
    # Create a deck, shuffle it, and deal hands
    testDeck = makeStandardDeck()
    shuffleDeck(testDeck)

    # Deal 2 cards to each player
    hand1 = dealHand(testDeck, 2)
    hand2 = dealHand(testDeck, 2)

    # Deal 3 community cards
    card_on_table = dealHand(testDeck, 3)

    print("Hand 1: ", [str(card) for card in hand1])
    #print("Hand 2: ", [str(card) for card in hand2])
    print("Table Cards: ", [str(card) for card in card_on_table])

    # Combine hands with community cards
    combined_hand1 = hand1 + card_on_table
    combined_hand2 = hand2 + card_on_table

    # Evaluate hand values
    value1 = hand_value(combined_hand1)
    value2 = hand_value(combined_hand2)

    print("Hand 1 Value: ", value1)
    #print("Hand 2 Value: ", value2)
    BotOdds = value2[0] + BotOdds
    print("Bot Odds: ", BotOdds)

    BetCheck = input("Player Would you like to bet or fold?(bet/fold): ")
    if BetCheck == "fold":
        print("Player Folded")
        print("Nothing happened")
        return
    elif BetCheck == "bet":
        print("Player Bets")
        BotOdds = BotOdds - 1
    else:
        print("Invalid Input")
        return
    BetValue = input("How much would you like to bet?: (allin, or number)")
    pot = 0
    if BetValue == "allin":
        val = playerBank.giveTotal()
        pot = pot + val
        playerBank.playChips(playerBank.allIn())
        print("Player went all in")
    else:
        pot = pot + int(BetValue)
        playerBank.playChips(int(BetValue))
        print("Player bet: ", BetValue)
    
    pot = decide(BotOdds, pot)
    print("Current Pot: ", pot)

    
    
    print("Hand 1: ", [str(card) for card in hand1])
    print("Hand 1 Value: ", value1)
    print("Hand 2: ", [str(card) for card in hand2])

    print("Hand 2 Value: ", value2)

    # Determine the winner
    if value1[0] > value2[0]:
        print("Hand 1 wins!")
        playerBank.add(pot)
        playerBank.printTotal()
        print("Bot then Player")
        botBank.printTotal()
        playerBank.printTotal()
    elif value1[0] < value2[0]:
        print("Hand 2 wins!")
        botBank.add(pot)
        print("Bot then Player")

        botBank.printTotal()
        playerBank.printTotal()
    else:
        print("It's a tie!")
        playerBank.add(pot / 2)
        botBank.add(pot / 2)
        print("Bot then Player")

        botBank.printTotal()
        playerBank.printTotal()

# Run the game
playGame()