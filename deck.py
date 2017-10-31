import random
from card import Card 

class Deck(object):
    def __init__(self):
        self.cards = []
        self._build()

    def _build(self):
        card_faces = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        suites = ['heart', 'diamond', 'club', 'spade']
        value = 0

        for face in card_faces:
            value = self._cardValue(face)
            for suite in suites:
                card = Card(face, value, suite)

                self.cards.append(card)

    def _cardValue(self, value):
        return {
            'A': 1,
            'J': 10,
            'Q': 10,
            'K': 10,
        }.get(value, value)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, player):
        card = self.cards.pop(0)

        player.addCard(card)

    def display(self):
        for card in self.cards:
            print card