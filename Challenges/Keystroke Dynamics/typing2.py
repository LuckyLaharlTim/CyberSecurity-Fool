from pynput.keyboard import Controller
from time import sleep
from random import uniform
from termios import tcflush, TCIFLUSH
from sys import stdin, stdout

###############################################################
## get string and timings that we'll use for the dynamic typing
###############################################################

password = input()
timings = input()

#print(f"Features = {password}")
#print(f"Timings = {timings}")

password = password.split(",")
password = password[:len(password) // 2 + 1]
password = "".join(password)
#print(f"Sample = \"{password}\"")

timings = timings.split(",")
timings = [ float(a) for a in timings ]
keypress = timings[:len(timings) // 2 + 1]
keyinterval = timings[len(timings) // 2 + 1:]
#print(f"KHTs = {keypress}")
#print(f"KITs = {keyinterval}")

########################
## start typing password
########################
keyboard = Controller()

## sleep line so we can move cursor to appropriate place
sleep(5.0)

for x in range(len(password)):
    keyboard.press(password[x])

    if (x < len(keypress) - 1):
        sleep(keyinterval[x])
        
    keyboard.release(password[x])

tcflush(stdout, TCIFLUSH)
print()
