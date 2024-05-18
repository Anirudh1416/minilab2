import time
time.sleep(0.1) # Wait for USB to become ready

print("Hello, Pi Pico!")

from ClockController import *
from Displays import LCDDisplay
from Button import *
from Clock import *
from Counters import *

mydisplay = LCDDisplay(sda=0, scl=1, i2cid=0)

myclock = ClockController()

mydisplay.showText("tick tock")

while True:
  myclock.showTime()
  time.sleep(1)

