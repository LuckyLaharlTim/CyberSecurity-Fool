'''
=================
MANUAL
=================
python3 <typing profile> > typing-final.py 
=================
NOTES
=================

- <typing profile> comes from the executable given by the 
challenge/professor.

- You will receive keys like 'a' 'c' 'f' with timings for each like 
'0.4' '0.9' '0.3'

- <typing profile> is simply a text file with the keys on 
the first row and the key timings on the second row.

- The keys and timings received from the challenge may 
be seperated by spaces and []

- These can be removed with the help of our strip program.
'''









from pynput.keyboard import Controller
from time import sleep
from random import uniform
from termios import tcflush, TCIFLUSH
from sys import stdin, stdout

sleep(10)

keyboard = Controller()

password = input()
timings = input()

##print(f"Features = {password}")
##print(f"Timings = {timings}")

password = password.split(",")
password = password[:len(password) // 2 + 1]
password = "".join(password)
##print(f"Sample = \"{password}\"")

timings = timings.split(",")
timings = [ float(a) for a in timings ]
keypress = timings[:len(timings) // 2 + 1]
keyinterval = timings[len(timings) // 2 + 1:]
##print(f"KHTs = {keypress}")
##print(f"KITs = {keyinterval}")

for x in range(len(password)):
    keyboard.press(password[x])
    sleep(keypress[x])
    keyboard.release(password[x])
    if (x < len(keypress)-1):
        sleep(keyinterval[x])
        
    

tcflush(stdout, TCIFLUSH)
print()
