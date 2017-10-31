from deck import Deck 
from player import Player 

deck = Deck()
deck.shuffle()

# deck.display()

player1 = Player("Felicia")
player2 = Player("Boberella")

for i in range(2):
    deck.deal(player1)
    deck.deal(player2)

player1.showHand()
print "====="
player2.showHand()
print "====="
