from pynput.keyboard import Listener, Key
from termios import tcflush, TCIFLUSH
from time import time
from sys import stdin, stdout

string = []
keypress = []
keyinterval = []
keys = ""
intervals = ""
times = ""
global t_0, t_1, t0, t1

def pressing(key):
    global t_0, t_1, t0, t1
    if (len(keypress) > 0):
        t_1 = time()
        keyinterval.append(t_1-t_0)
    try:
       t0 = time()
       string.append(key.char)
       #print (key.char)#print(key.char.encode("ascii"), end = ' ')
    except AttributeError:
        t0 = time()
        string.append(str(key))


def releasing(key):
    global t_0, t_1, t0, t1
    if (key == Key.esc):
        return False
    else:
        t1 = t_0 = time()
        keyinterval.append(t1-t0)


with Listener(on_press=pressing, on_release=releasing) as listener:
    listener.join()

tcflush(stdin, TCIFLUSH)

# make first line of input file
for i in range(0,len(string)):
    keys += (f"{string[i]},")
for i in range(0,len(string)-1):
    keys += (f"{string[i]}{string[i+1]},")

# make second line of input file
for i in range(0,len(keypress)):
    times += (f"{keypress[i]},")
for i in range(0,len(keyinterval)):
    times += (f"{keyinterval[i]},")



stdout.write(f"{keys}\n{times}")

