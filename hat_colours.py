#!/usr/bin/env python 
from sense_hat import SenseHat
sense = SenseHat()

yellow = (0, 0, 0)
blue = (255, 255, 255)

speed = 0.05

message = "ryan is maybe a god"

sense.show_message(message, speed, text_colour=yellow, back_colour=blue)

sense.clear()
