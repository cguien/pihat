#!/usr/bin/env python 
# this script will show a scrolling message on the Pi HAt
from sense_hat import SenseHat
sense = SenseHat()

# send the text Hello World! to the show_message() function 
sense.show_message("Cross is a silly goose.")
sense.show_message("Ryan is just a goose")
#This code displays the messages you write on the pihat using the command sense.show_message

