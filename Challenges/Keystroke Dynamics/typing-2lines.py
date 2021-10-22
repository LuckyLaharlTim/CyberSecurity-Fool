from pynput.keyboard import Controller
from time import sleep
from random import uniform
from termios import tcflush, TCIFLUSH
from sys import stdin, stdout

# get the password, keypress times, and intervals --equivalent of typing-2--
def getInfo():
    password = input()
    timings = input()
    keypress = []
    keyinterval = []


    password = password.split(",")
    password = password[:len(password)//2+1]
    password = "".join(password)
    #print(f"Sample = \"{password}\"")

    
    timings = timings.split(',')
    timings = [float(a) for a in timings]
    keypress.append(timings[:len(timings)//2+1])
    keyinterval.append(timings[len(timings)//2+1:])
    #print(f"KHTs = {keypress}\nKITs = {keyinterval}")

    return password, keypress, keyinterval

if __name__ == "__main__":
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


        for index in range(0,len(string)): #[:len(string)//2+1])):
            if (index in range(1, len(string))):
                sleep(trueKeyInterval[index-1])
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


