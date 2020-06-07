class playingCard:

    def __init__(self, color, suit, value):
        self.color = color
        self.suit = suit
        self.value = value

    def getSuit(self):
        return self.suit

    def getValue(self):
        return self.value

    def getColor(self):
        return self.color

    def showCard(self):
        return str(self.value) + " of " + self.color + " " + self.suit

    #returns true if card value is less than val:int
    def compareValue(self, int):
        if self.value < int:
            return true
        else:
            return false
