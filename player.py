class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def addCard(self, card):
        self.hand.append(card)

    def showHand(self):
        print "{}'s hand: ".format(self.name)
        for card in self.hand:
            print card
