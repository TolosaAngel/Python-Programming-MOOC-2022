from random import *

class PlayingCard:
    def __init__(self,suit: str, value: int):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.suit} {self.value}"
    
class CardDeck:
    def __init__(self, cards = []):
        self.__cards = cards

    def __next__(self):
        if len(self.__cards) > 0:
            return self.__cards.pop(0)
        else:
            return None

    def print_cards(self):
        for card in self.__cards:
            print(card)

    def shuffle_cards(self):
        shuffle(self.__cards)

if __name__ == "__main__":
    card1 = PlayingCard("Club", 7)
    card2 = PlayingCard("Heart", 7)
    card3 = PlayingCard("Diamond", 2)
    card4 = PlayingCard("Diamond", 3)
    card5 = PlayingCard("Spade", 8)
    deck = CardDeck([card1, card2, card3, card4, card5])
    deck.shuffle_cards()
    deck.print_cards()
    print()
    print("Card drawn:", next(deck))
    print("Card drawn:", next(deck))
    print("Cards left in the deck:")
    deck.print_cards()

    print()
    for i in range(6):
        card = next(deck)
        if not card:
            print("There are no cards left in the deck. All cards have been drawn.")
            break
        print("Card drawn:", card)