from pynput.keyboard import Controller
from time import sleep
from random import uniform
from termios import tcflush, TCIFLUSH
from sys import stdout
from typing2 import getInfo

(string, keypress, keyinterval) = getInfo()

keyboard = Controller()

try:
    trueKeyPress = []
    trueKeyInterval = []

    for i in range(0,len(keypress)):
        for j in range(0,len(keypress[i])):
            trueKeyPress.append(keypress[i][j])
    
    for i in range(0,len(keyinterval)):
        for j in range(0,len(keyinterval[i])):
            trueKeyInterval.append(keyinterval[i][j])

    for index in range(0,len(string)):
        if (index in range(1,len(trueKeyInterval))):
            sleep(trueKeyInterval[index])
        keyboard.press(string[index])
        sleep(trueKeyPress[index])
        keyboard.release(string[index])


except TypeError:
    for index in range(0,len(string)):
        if (index > 0):
            sleep(keyinterval[index])
        keyboard.press(string[index])
        sleep(keypress[index])
        keyboard.release(string[index])
        


tcflush(stdout, TCIFLUSH)
print()


