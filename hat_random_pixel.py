#!/usr/bin/env python

from sense_hat import SenseHat
sense = SenseHat()
import time
import random 
x = random.randint(0,7)
y = random.randint(0,7)
r = random.randint(0,255)

sense.set_pixel(x, y, (0, 0, r))

time.sleep(1)
sense.clear()
