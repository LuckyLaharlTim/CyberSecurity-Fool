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
    if (key == Key.esc):
        return False
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
    t1 = t_0 = time()
    keypress.append(t1-t0)


with Listener(on_press=pressing, on_release=releasing) as listener:
    listener.join()

tcflush(stdin, TCIFLUSH)

for i in range(1,len(string)):
    string.append(f"{string[i-1]}{string[i]}")

for i in range(0,len(keyinterval)):
    keypress.append(keyinterval[i])
stdout.write(", ".join(string).replace(" ", ""))
stdout.write("\n")
stdout.write(str(keypress).strip("[]").replace(" ", ""))
