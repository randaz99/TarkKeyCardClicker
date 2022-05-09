#Importing Libraries
from pynput.mouse import Button, Controller
mouse = Controller()

while mouse.click != 1:
    print(str(mouse.position))