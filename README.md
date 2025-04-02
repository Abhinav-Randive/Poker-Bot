# **Poker Bot**
We are trying to make a functional Poker bot. The game uses standard poker hand rankings to evaulate the strength of each player's hand.

## **Features**
1) Deck Creation: A standard 52-card deck is created with suits (Hearts, Clubs, Spades and Diamonds) and values (Ace, 2-10, J, Q and K). This deck is created randomly everytime the program is run.

2) **Shuffling**: The deck is shuffled using 'random' before dealing the cards to the players.

3) **Dealing**: Each player is dealt two cards, and three community cards are dealt on the table

4) On the basis of the player's cards and community cards, a hand ranking evaulation begins

5) **Hand Evaluatio**n: Hands are evaluated using standard poker hand ranking (for Texas Hold'Em style)
* Royal Flush
* Straight Flush
* Four a Kind
* Full House
* Flush
* Straight
* Three of a Kind
* Two Pair
* One Pair
* High Card

6) **Winning**: The combined value of each hand is evaluated, and the player with the stronger hand wins. If both hands are equally strong, it is considered a tie.
