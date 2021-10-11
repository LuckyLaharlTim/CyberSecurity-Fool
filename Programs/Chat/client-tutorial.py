# use Python 3
import socket
from sys import stdout
from time import time

# enables debugging output
DEBUG = False

# set the server's IP address and port
ip = 1138.47.99.64 # "localhost"
port = 1337

# make list to append delays between characters
delays = []

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
	delays.append(delta)
	if (DEBUG):
		stdout.write(" {}\n".format(delta))
		stdout.flush()

# close the connection to the server
s.close()
