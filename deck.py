from card import playingCard
import random

class deck:

    deckCards = []

    def __init__(self):
        for i in range (1,14):
            redHearts = playingCard('red','hearts',i)
            self.deckCards.append(redHearts)
            redDiamond = playingCard('red','diamonds',i)
            self.deckCards.append(redDiamond)
            blackSpades = playingCard('black','spades',i)
            self.deckCards.append(blackSpades)
            blackClubs = playingCard('black','clubs',i)
            self.deckCards.append(blackClubs)

    def printDeck(self):
        for i in range(len(self.deckCards)):
            print(self.deckCards[i].showCard())

    def shuffle(self):
        random.shuffle(self.deckCards)


if __name__ == "__main__":
    test = deck()
    test.shuffle()
    test.printDeck()
