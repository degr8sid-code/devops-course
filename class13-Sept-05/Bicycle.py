import random
from bicycle import Bicycle as bike

bikeList = []

for i in range(10):
    wSize = random.randint(24, 30)
    iniSpeed = random.randint(16, 20)
    bikeList.append(bike(wSize, iniSpeed))

for i in bikeList:
    print(i.getSpeed(), end="\t")

print()
print("0ld speed: ", end='\t')

for i in range(10): 
    if (1 % 2) == 0:
        print(bikeList[i].getSpeed(), end="\t\t")
        newSpeed = round((bikeList[i].getSpeed()*1.2), 0)
        bikeList[i].setSpeed(newSpeed)

print()
print("New speed: ", end='\t')

for i in range(10):
    if (1 % 2) == 0:
        print(bikeList[i].getSpeed(), end="\t")