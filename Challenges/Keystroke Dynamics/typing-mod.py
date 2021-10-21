from pynput.keyboard import Controller
from time import sleep
from random import uniform
from termios import tcflush, TCIFLUSH
from sys import stdout
from typing2 import getInfo

(string, keypress, keyinterval) = getInfo()

keyboard = Controller()

index = 0
for index in range(0,len(string)):
    if (index >0):
        sleep(keyinterval[index-1])
    keyboard.press(string[index])
    sleep(keypress[index])
    keyboard.release(string[index])
    

tcflush(stdout, TCIFLUSH)
print()


