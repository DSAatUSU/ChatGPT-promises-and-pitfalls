import random

class Deck:
    def __init__(self):
        self.cards = []

        # Generating a standard deck of cards
        for suit in ['Spades', 'Hearts', 'Diamonds', 'Clubs']:
            for value in range(1, 14):
                card = (value, suit)
                self.cards.append(card)

    def shuffle(self):
        # Shuffle the deck using random.shuffle
        random.shuffle(self.cards)

    def draw(self):
        # Draw a card from the top of the deck
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None

# Test the Deck class
if __name__ == "__main__":
    deck = Deck()
    print("Initial deck of cards:")
    print(deck.cards)

    deck.shuffle()
    print("\nShuffled deck of cards:")
    print(deck.cards)

    print("\nDrawing two cards:")
    print(deck.draw())
    print(deck.draw())

    print("\nRemaining cards in the deck:")
    print(deck.cards)
