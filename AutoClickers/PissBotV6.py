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

graceTime = int(input("!IMPORTANT! Enter grace period > 0 in seconds: "))
time.sleep(0.2)

#HUMAN RANDOM
humanSeed = int(graceTime*totalTimeSec)
print("\n Seed: " + str(humanSeed) + "\n")
seed(humanSeed)

#Calcualting total iteration (2 per second)
totalIterations = totalTimeSec*2.03
print(" Starting iteration 1 of " + str(int(totalIterations)) + " in " + str(graceTime) + " seconds...\n")

#Grace Period + Countdown
if graceTime > 5:
    time.sleep(graceTime - 5)
    countdown = 5
else:
    time.sleep(1)
    countdown = graceTime - 1
    
while countdown > 0:
    print("                               " + str(countdown) + "..")
    time.sleep(1)
    countdown -= 1

print("                               Go!\n")
        

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
    
    #waiting
    randTime = random()/2
    timeLeft -= randTime
    timeSum += randTime
    time.sleep(randTime)

    #randomizing (x,y) for the deal button
    randDealX = randint(1130, 1430)
    randDealY = randint(220, 260)
    mouse.position = (randDealX, randDealY)
    mouse.click(Button.left, 1)
    
    #waiting
    randTime = random()/2
    timeLeft -= randTime
    timeSum += randTime
    print(str(timeSum))
    time.sleep(randTime)
    
    #pee break
    randBreak = randint(1200, 1500)
    if timeSum > randBreak:
        randBreakLength = randint(6, 12)
        print("\n Taking a piss break..")
        
        #clicking random spot on labs entry card
        randEntryX = randint(100, 170)
        randEntryY = randint(355, 420)
        mouse.position = (randEntryX, randEntryY)
        mouse.click(Button.left, 1)
        
        randTime = random()*2
        time.sleep(randTime)
        
        #clicking random spot on BLACK KEYCARD
        randBlackX = randint(15, 75)
        randBlackY = randint(355, 420)
        mouse.position = (randBlackX, randBlackY)
        mouse.click(Button.left, 1)
        
        time.sleep(randBreakLength)
        print(" Total Updated!\n")
        timeLeft -= randBreakLength + 1
        pissSum += 1
        totalIterations -= (randBreakLength + 1) * 2.03
        pissLength += randBreakLength + 1
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