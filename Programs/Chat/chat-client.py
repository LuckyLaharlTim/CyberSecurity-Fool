###############################
## Team Name:   The Fool
## Assignment:  Chat
## Date:        15 October 2021
###############################

# use Python 3
import socket
from sys import stdout
from time import time
from binascii import hexlify, unhexlify

# enables debugging output
DEBUG = False
ZERO = 0.025
ONE = 1

# set the server's IP address and port
ip = "138.47.99.64" # "localhost" - "138.47.99.64"
port = 1337

# make list to append delays between characters
delays = []

covert_bin = ""
covert = ""

# create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
s.connect((ip, port))

# receive data until EOF
data = s.recv(4096).decode()
while (data.rstrip("\n") != "EOF"):
	# output the data
	stdout.write(data)
	stdout.flush()
	# start the "timer", get more data, and end the "timer"
	t0 = time()
	data = s.recv(4096).decode()
	t1 = time()
	# calculate the time delta (and output if debugging)
	delta = round(t1 - t0, 3)
	# get beats for covert message from delays
	if (delta >= ONE):
		covert_bin += "1"
	else:
		covert_bin += "0"
	if (DEBUG):
		print(covert_bin)
		stdout.write(" {}\n".format(delta))
		stdout.flush()


# close the connection to the server
s.close()
        
i = 0
while (i < len(covert_bin)):
        #process 1 byte at a time
        b = covert_bin[i:i+8]
        # convert it to ASCII
        n = int("0b{}".format(b), 2)
        try:
                covert += chr(ord(n))
        except TypeError:
                covert += "?"
        # stop at the string "EOF"
        i +=8

# write covert message
stdout.write(" {}\n".format(covert))
stdout.flush()


# code update
##        Timothy Oliver; 10-11-21
##
##        - I added code that added organized the delay between characters
##           into individual bits so we could the covert message.
##        - I also set up the conversion from covert_bin to the text covert message.
##        - Everything was written on Windows, so the delay times
##           do not allow for a correct covert message.
##        - My tests have appeared to leave the server open instead of closing it
##           (I get "The server is listening . . ." but not "Message sent" from
##            server-tutorial.py)
        
