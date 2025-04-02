# **Poker Bot**
We are trying to make a functional Poker bot. The game uses standard poker hand rankings to evaulate the strength of each player's hand.

## **Features**
1) Deck Creation: A standard 52-card deck is created with suits (Hearts, Clubs, Spades and Diamonds) and values (Ace, 2-10, J, Q and K). This deck is created randomly everytime the program is run.

2) **Shuffling**: The deck is shuffled using 'random' before dealing the cards to the players.

3) **Dealing**: Each player is dealt two cards, and three community cards are dealt on the table

4) **Hand Evaluatio**n: Hands are evaluated using standard poker hand ranking (for Texas Hold'Em style)

<div align="center">

| Hand Ranking   | Description                              | Example Hand          |
|:--------------:|:----------------------------------------:|:---------------------:|
| Royal Flush    | A, K, Q, J, 10, all the same suit        | A♥ K♥ Q♥ J♥ 10♥       |
| Straight Flush | Five consecutive cards of the same suit  | 9♣ 8♣ 7♣ 6♣ 5♣        |
| Four of a Kind | Four cards of the same rank              | Q♦ Q♠ Q♥ Q♣ 5♠        |
| Full House     | Three of a kind + a pair                 | J♠ J♥ J♦ 8♣ 8♥        |
| Flush          | Five cards of the same suit (not consecutive) | A♠ J♠ 8♠ 5♠ 3♠    |
| Straight       | Five consecutive cards (mixed suits)     | 10♦ 9♠ 8♥ 7♣ 6♦       |
| Three of a Kind| Three cards of the same rank             | 7♣ 7♥ 7♦ K♠ 4♥        |
| Two Pair       | Two different pairs                      | A♣ A♠ 9♥ 9♦ J♣        |
| One Pair       | One pair of cards with the same rank     | K♠ K♦ Q♣ 10♠ 4♥       |
| High Card      | No matching cards (highest card plays)   | A♦ Q♣ 10♠ 5♥ 3♣       |

</div>

6) **Winning**: The combined value of each hand is evaluated, and the player with the stronger hand wins. If both hands are equally strong, it is considered a tie.
