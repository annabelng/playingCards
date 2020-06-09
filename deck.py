from card import playingCard
import random

class deck:

    deckCards = []

    def __init__(self):
        self.fillDeck()

    def printDeck(self):
        for i in range(len(self.deckCards)):
            print(self.deckCards[i].showCard())

    def shuffle(self):
        random.shuffle(self.deckCards)

    def drawCardNoReplace(self):
        self.shuffle()
        return self.deckCards.pop()

    def drawCardWithReplace(self):
        self.shuffle()
        return self.deckCards[0]

    def clearDeck(self):
        self.deckCards = []

    def fillDeck(self):
        self.clearDeck()
        for i in range (1,14):
            redHearts = playingCard('red','hearts',i)
            self.deckCards.append(redHearts)
            redDiamond = playingCard('red','diamonds',i)
            self.deckCards.append(redDiamond)
            blackSpades = playingCard('black','spades',i)
            self.deckCards.append(blackSpades)
            blackClubs = playingCard('black','clubs',i)
            self.deckCards.append(blackClubs)

#testing methods
def singleCardTest(self, testNum):
    cntr = 0
    for i  in range(testNum):
        temp = self.drawCardWithReplace()
        if(temp.showCard() == "1 of black spades"):
            cntr += 1

    probability = cntr/testNum
    return probability

def colorTest(self, testNum):
    cntr = 0
    for i  in range(testNum):
        temp = self.drawCardWithReplace()
        if(temp.getColor() == "black"):
            cntr += 1

    probability = cntr/testNum
    return probability

def suitTest(self, testNum):
    cntr = 0
    for i  in range(testNum):
        temp = self.drawCardWithReplace()
        if(temp.getSuit() == "spades"):
            cntr += 1

    probability = cntr/testNum
    return probability

def twoIndiv(self, card, testNum):
    cntr = 0
    for i  in range(testNum):
        temp1 = card.drawCardNoReplace()
        temp2 = card.drawCardNoReplace()
        if(temp1.showCard() == "1 of black spades") and (temp2.showCard() == "1 of red diamonds"):
            cntr += 1
        card.fillDeck()

    probability = cntr/testNum
    return probability

def twoIndivColor(self, testNum):
    cntr = 0
    for i  in range(testNum):
        temp1 = self.drawCardNoReplace()
        temp2 = self.drawCardNoReplace()
        if(temp1.showCard() == "1 of black spades") and (temp2.getColor() == "black"):
            cntr += 1
        self.fillDeck()

    probability = cntr/testNum
    return probability

def twoColors(self, testNum):
    cntr = 0
    for i  in range(testNum):
        temp1 = self.drawCardNoReplace()
        temp2 = self.drawCardNoReplace()
        if(temp1.getColor() == "black") and (temp2.getColor() == "red"):
            cntr += 1
        self.fillDeck()

    probability = cntr/testNum
    return probability

def twoNums(self, testNum):
    cntr = 0
    for i  in range(testNum):
        temp1 = self.drawCardNoReplace()
        temp2 = self.drawCardNoReplace()
        if(temp1.getValue() == temp2.getValue()):
            cntr += 1
        self.fillDeck()

    probability = cntr/testNum
    return probability

if __name__ == "__main__":
    test = deck()
    #test.shuffle()
    #test.printDeck()
    """print("first deck")
    test.shuffle()
    print("shuffle")
    test.printDeck()
    print("new deck")
    test.fillDeck()e
    test.printDeck()
    print(test.singleCardTest())"""

    print(singleCardTest(test,100000))
    print(colorTest(test,100000))
    #print(test.colorTest())
    #print(test.suitTest())
    #3print (twoIndivColor(test,1000))
    #print(test.twoColors())
    #print(test.twoNums())

    #print(test.drawCardNoReplace().showCard())
    #print(test.drawCardWithReplace().showCard())
