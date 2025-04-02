# **Poker Bot**
We are trying to make a functional Poker bot. The game uses standard poker hand rankings to evaulate the strength of each player's hand.

## **Features**
1) Deck Creation: A standard 52-card deck is created with suits (Hearts, Clubs, Spades and Diamonds) and values (Ace, 2-10, J, Q and K). This deck is created randomly everytime the program is run.

2) **Shuffling**: The deck is shuffled using 'random' before dealing the cards to the players.

3) **Dealing**: Each player is dealt two cards, and three community cards are dealt on the table

4) On the basis of the player's cards and community cards, a hand ranking evaulation begins

5) **Hand Evaluatio**n: Hands are evaluated using standard poker hand ranking (for Texas Hold'Em style)
| Rank          | Example Hand          | Description                              |
|---------------|-----------------------|------------------------------------------|
| Royal Flush   | A♥ K♥ Q♥ J♥ 10♥       | Ace-high straight flush                 |
| Straight Flush| 9♣ 8♣ 7♣ 6♣ 5♣        | Five sequential cards, same suit        |
| Four of a Kind| Q♦ Q♠ Q♥ Q♣ 5♠        | All four cards of one rank              |
| Full House    | J♠ J♥ J♦ 8♣ 8♥        | Three-of-a-kind + pair ("Jacks full")   |
| Flush         | A♠ J♠ 8♠ 5♠ 3♠        | Five non-sequential cards, same suit    |
| Straight      | 10♦ 9♠ 8♥ 7♣ 6♦       | Five sequential cards, mixed suits      |
| Three of a Kind| 7♣ 7♥ 7♦ K♠ 4♥       | Three cards of one rank                 |
| Two Pair      | A♣ A♠ 9♥ 9♦ J♣        | Two different pairs                     |
| One Pair      | K♠ K♦ Q♣ 10♠ 4♥       | Single pair                             |
| High Card     | A♦ Q♣ 10♠ 5♥ 3♣       | No combinations (ace-high)              |

6) **Winning**: The combined value of each hand is evaluated, and the player with the stronger hand wins. If both hands are equally strong, it is considered a tie.
