#Importing Libraries
from pynput.mouse import Button, Controller
from random import seed
from random import random
from random import randint
import time

#instatiating
mouse = Controller()
seed(420)


c = 0
while c < 86400:
    #randomizing (x,y) for the refrsh button
    randFreshX = randint(340, 350)
    randFreshY = randint(115, 125)
    mouse.position = (randFreshX, randFreshY)

    randTime = random()
    time.sleep(randTime)

    #randomizing (x,y) for the deal button
    randDealX = randint(1130, 1430)
    randDealY = randint(220, 260)
    mouse.position = (randDealX, randDealY)

    randTime = random()
    time.sleep(randTime)

    #debug
    c += 1
    print("Iteration " + str(c) + " Complete")
    
print("Finished!")
