class Position:
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.prevPos = [(self.x, self.y)]

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getBoth(self):
        return self.x, self.y
    
    def setX(self, x):
        self.x = x
        self.prevPos.append((self.x))

    def setY(self, y):
        self.y = y
        self.prevPos.append((self.y))

    def setBoth(self, x, y):
        self.x = x
        self.y = y
        self.prevPos.append((self.x, self.y))
    
    def incX(self, amount=1):
        self.x += amount

    def incY(self, amount=1):
        self.y += amount

    def incBoth(self, amount=1):
        self.y += amount
        self.x += amount

    def decX(self, amount=1):
        self.x -= amount

    def decY(self, amount=1):
        self.y -= amount

    def decBoth(self, amount=1):
        self.x -= amount
        self.y -= amount

    def __str__(self):
        return f"Position({self.x}, {self.y})"
    
    


def main():
    pos = Position()
    pos.setBoth(10, 20)
    pos.getBoth()
    pos.incX(5)
    pos.decY(5)
    print(pos)
    print(f"pos.prevPos: {pos.prevPos}")


if __name__== '__main__':
    main()