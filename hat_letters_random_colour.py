#!/usr/bin/env python 
# this scipt will display leters with random colors on the Pi HAT
from sense_hat import SenseHat
import time 
import random 
sense = SenseHat() 
# assign a random integer between ) and 255 to a variable named r 
r = random.randint(0,255)

sense.show_letter("N", (r, 0, 0))
time.sleep(1)
sense.show_letter("o", (0, r, 0))
time.sleep(1)
sense.show_letter("o", (0, 0, r))
time.sleep(1)
sense.clear()
