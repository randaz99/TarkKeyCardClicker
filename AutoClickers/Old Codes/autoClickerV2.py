#Importing Libraries
from pynput.mouse import Button, Controller
from random import seed
from random import random
from random import randint
import time

#instatiating
mouse = Controller()
seed(420)

#promting length
totalTimeSec = float(input("\nEnter time in hours: "))*60*60
totalIterations = totalTimeSec*1.16666666666666666666*2
print("Starting iteration 1 of " + str(int(totalIterations)) + "...\n")
randTime = random()
time.sleep(randTime)

#initializing loop
c = 0
timeLeft = totalTimeSec
while timeLeft > 0:
    #randomizing (x,y) for the refrsh button
    randFreshX = randint(340, 350)
    randFreshY = randint(115, 125)
    mouse.position = (randFreshX, randFreshY)
    #mouse.click(Button.left, 1)

    randTime = random()/2
    timeLeft = timeLeft - randTime
    time.sleep(randTime)

    #randomizing (x,y) for the deal button
    randDealX = randint(1130, 1430)
    randDealY = randint(220, 260)
    mouse.position = (randDealX, randDealY)
    #mouse.click(Button.left, 1)

    randTime = random()/2
    timeLeft = timeLeft - randTime
    time.sleep(randTime)

    #debug
    c += 1
    print("Iteration " + str(c) + "/" + str(int(totalIterations)) + " Complete")
    
if c > totalIterations:
    print(c + "\n extra iterations completed..")
elif c < totalIterations:
    print(c + "\n iterations skipped due to time..")
else:
    print("\nExact iterations completed..")
    
print("Finished!")
