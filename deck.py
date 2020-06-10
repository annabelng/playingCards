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

    def filteredDeck(self,suits,vals):
        self.clearDeck()
        for i in range (vals[0],vals[1]):
            if('hearts' in suits):
                redHearts = playingCard('red','hearts',i)
                self.deckCards.append(redHearts)
            if('diamonds'in suits):
                redDiamond = playingCard('red','diamonds',i)
                self.deckCards.append(redDiamond)
            if('spades'in suits):
                blackSpades = playingCard('black','spades',i)
                self.deckCards.append(blackSpades)
            if('clubs' in suits):
                blackClubs = playingCard('black','clubs',i)
                self.deckCards.append(blackClubs)

#testing methods
def singleCardTest(self, testNum, attributes):
    cntr = 0
    check = 0
    for i  in range(testNum):
        temp = self.drawCardWithReplace()
        if(temp.getColor() in attributes):
            check+=1
        if(temp.getSuit() in attributes):
            check+=1
        if(temp.getValue() in attributes):
            check+=1
        if('of' in attributes):
            check+=1

        if check == len(attributes):
            cntr +=1
        check = 0

    probability = cntr/testNum
    return probability

def doubleCardTest(self, testNum, card1, card2):
    cntr = 0

    for i  in range(testNum):
        temp1 = self.drawCardNoReplace()
        temp2 = self.drawCardNoReplace()

        if(temp1.showCard() == card1 and temp2.showCard() == card2):
            cntr +=1

        self.fillDeck()

    probability = cntr/testNum
    return probability

def doubleCardColor(self, testNum,card,color):
    cntr = 0
    for i  in range(testNum):
        temp1 = self.drawCardNoReplace()
        temp2 = self.drawCardNoReplace()
        if(temp1.showCard() == card) and (temp2.getColor() == color):
            cntr += 1
        self.fillDeck()

    probability = cntr/testNum
    return probability

def twoColors(self, testNum,color1, color2):
    cntr = 0
    for i  in range(testNum):
        temp1 = self.drawCardNoReplace()
        temp2 = self.drawCardNoReplace()
        if(temp1.getColor() == color1) and (temp2.getColor() == color2):
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

def threeColors(self, testNum, color1, color2, color3):
    cntr = 0
    for i  in range(testNum):
        temp1 = self.drawCardNoReplace()
        temp2 = self.drawCardNoReplace()
        temp3 = self.drawCardNoReplace()
        if(temp1.getColor() == color1) and (temp2.getColor() == color2) and (temp3.getColor() == color3):
            cntr += 1
        self.fillDeck()

    probability = cntr/testNum
    return probability

def minColor(self,testNum, color):
    cntr = 0
    for i  in range(testNum):
        temp1 = self.drawCardNoReplace()
        temp2 = self.drawCardNoReplace()
        temp3 = self.drawCardNoReplace()
        if(temp1.getColor() == color) or (temp2.getColor() == color) or (temp3.getColor() == color):
            cntr += 1
        self.fillDeck()

    probability = cntr/testNum
    return probability

def atLeastTwoColor(self, testNum,color):
    cntr = 0
    check = 0
    for i  in range(testNum):
        temp1 = self.drawCardNoReplace()
        temp2 = self.drawCardNoReplace()
        temp3 = self.drawCardNoReplace()
        if(temp1.getColor() == color):
            check += 1
        if(temp2.getColor() == color):
            check+=1
        if(temp3.getColor() == color):
            check += 1
        if(check>=2):
            cntr +=1
        self.fillDeck()
        check = 0

    probability = cntr/testNum
    return probability

def pair(self,testNum,value):
    cntr = 0
    for i  in range(testNum):
        temp1 = self.drawCardNoReplace()
        temp2 = self.drawCardNoReplace()
        temp3 = self.drawCardNoReplace()
        if(temp1.getValue() == temp2.getValue()):
            cntr += 1
        elif(temp1.getValue() == temp3.getValue()):
            cntr += 1
        elif(temp2.getValue() == temp3.getValue()):
            cntr += 1
        self.fillDeck()

    probability = cntr/testNum
    return probability

def threeVal(self, testNum, value):
    cntr = 0
    for i  in range(testNum):
        temp1 = self.drawCardNoReplace()
        temp2 = self.drawCardNoReplace()
        temp3 = self.drawCardNoReplace()
        if(temp1.getValue() == temp2.getValue() and temp1.getValue() == temp3.getValue()):
            cntr +=1
        self.fillDeck()

    probability = cntr/testNum
    return probability

def singleCardGiven(self, testNum, givenSuits, givenValues, target):
    cntr = 0
    self.filteredDeck(givenSuits,givenValues)
    for i  in range(testNum):
        temp = self.drawCardWithReplace()
        if(temp.getValue() == target):
            cntr += 1

    probability = cntr/testNum
    return probability

def doubleCardGiven(self, testNum, givenSuit, target):
    cntr = 0
    i=0
    while i < testNum:
        temp1 = self.drawCardNoReplace()
        temp2 = self.drawCardNoReplace()
        if(temp1.getSuit() == givenSuit or temp2.getSuit()==givenSuit):
            i += 1
            if(temp1.getSuit() == givenSuit and temp2.getSuit()==givenSuit):
                cntr +=1
        self.fillDeck()

    probability = cntr/testNum
    return probability

def consecutiveGivenVal(self,testNum,givenVal):
    cntr = 0
    i=0
    while i < testNum:
        temp1 = self.drawCardNoReplace()
        temp2 = self.drawCardNoReplace()
        if(temp1.getValue() == givenVal or temp2.getSuit()==givenVal):
            i += 1
            if(temp2.getValue()-temp1.getValue()==1):
                cntr +=1
        self.fillDeck()

    probability = cntr/testNum
    return probability

if __name__ == "__main__":
    test = deck()
    '''print(doubleCardTest(test,100000,'6 of black spades','5 of red diamonds'))
    print(doubleCardColor(test,100000,'6 of black spades','red'))
    print(twoColors(test,100000,'black','red'))'''
    #print(minColor(test, 1000000, 'red'))
    #print(atLeastTwoColor(test,10000000,'red'))
    #print(pair(test,10000000,8))
    #print(threeVal(test,1000000,2))
    #test.filteredDeck(['diamonds','hearts'],[1,14])
    #test.printDeck()
    #print(singleCardGiven(test,1000000,['diamonds','hearts'],[1,14],13))
    #print(doubleCardGiven(test,1000000,'spades',13))
    print(consecutiveGivenVal(test,1000000,4))
