#Created by: Evan
#Created on: Oct. 2020

#This program blinks and LED

from microbit import *

LED = pin1

while True:
   LED.write_digital(1)
   sleep(1000)
   LED.write_digital(0)
   sleep(1000)

