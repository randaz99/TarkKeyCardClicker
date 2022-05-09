#Importing Libraries
from pynput.mouse import Button, Controller
from random import seed
from random import random
from random import randint
import time

#instatiating
mouse = Controller()

    
#promting lengths
hours = float(input("\nEnter hours: "))*60*60
time.sleep(0.2)
minutes = float(input("Enter minutes: "))*60
time.sleep(0.2)
seconds = float(input("Enter seconds: "))
time.sleep(0.3)
totalTimeSec = float(hours + minutes + seconds)

graceTime = int(input("!IMPORTANT! Enter grace period in seconds: "))
time.sleep(0.2)

#Calcualting total iteration (2 per second)
totalIterations = totalTimeSec*2.03
print("\n Starting iteration 1 of " + str(int(totalIterations)) + " in " + str(graceTime) + " seconds...\n")

#HUMAN RANDOM
humanSeed = int(graceTime*totalTimeSec)
print("Seed: " + str(humanSeed))
seed(humanSeed)

#Grace Period
time.sleep(graceTime)

#initializing loop
c = 0
timeSum = 0
timeLeft = totalTimeSec
pissSum = 0
pissLength = 0
while timeLeft > 0:
    #randomizing (x,y) for the refrsh button
    randFreshX = randint(340, 350)
    randFreshY = randint(115, 125)
    mouse.position = (randFreshX, randFreshY)
    mouse.click(Button.left, 1)

    randTime = random()/2
    timeLeft -= randTime
    timeSum += randTime
    time.sleep(randTime)

    #randomizing (x,y) for the deal button
    randDealX = randint(1130, 1430)
    randDealY = randint(220, 260)
    mouse.position = (randDealX, randDealY)
    mouse.click(Button.left, 1)

    randTime = random()/2
    timeLeft -= randTime
    timeSum += randTime
    time.sleep(randTime)
    
    #pee break
    randBreak = randint(2400, 3000)
    if timeSum > randBreak:
        randBreakLength = randint(60, 120)
        print("\n Taking a piss break..")
        time.sleep(randBreakLength)
        print(" Total Updated!\n")
        timeLeft -= randBreakLength
        pissSum += 1
        totalIterations -= randBreakLength*2.03
        pissLength += randBreakLength
        timeSum = 0
        
    #debug
    c += 1
    print("Iteration " + str(c) + "/" + str(int(totalIterations)) + " Completed")
#Fun Debug
if c > totalIterations:
    print("\n" + str(int(c - totalIterations)) + " extra iterations completed :)")
elif c < totalIterations:
    print("\n" + str(int(totalIterations - c)) + " iterations skipped due to time :(")
else:
    print("\nExact iterations completed.")    
            
#Piss Debug
randTime = random()*1.5
time.sleep(randTime)
print("\n Program Success..\n")
randTime = random()*1.5
time.sleep(randTime)
print("Pissed " + str(pissSum) + " times for a total of " + str(pissLength) + " seconds!")
randTime = random()*1.2
time.sleep(randTime)
print(str(int(pissLength*2.03)) + " ITERATIONS PISSED AWAY!!\n")
randTime = random()*1.5
time.sleep(randTime)