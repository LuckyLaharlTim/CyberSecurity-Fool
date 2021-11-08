'''
==========================
MANUAL                   
==========================
python3 chat.py





=============
Notes
=============
This use this program first set the ip value to the
server supplied by challenge/professor. Do the same 
for the port. 

Now the values for ZERO and ONE are obtained by running
the program with DEBUG on. Doing this will list off timing
for each character. There should be a 2 distinct 
values that you can observe for the times.

- Choosing values for ZERO and ONE will require some guesswork
        ~ NOTE: you should guess around
                5/10ths below the intervals you are seeing in debug 
        ~ example: 
                you receive intervals around 0.25 and 0.5;
                 set ONE to 0.45

- Pick a time based on the distinctive values and assign one
to each

- If they don't work, first flip them and retry

- If they still don't work, choose new values
'''







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
DEBUG = True
MESSAGE = True
ZERO = 0.025
ONE = 0.05

# set the server's IP address and port
ip = "138.47.99.64" # options for assignment: "localhost" - "138.47.99.64"
port = 1337 # options for assignment: "1337" or "12000"

# make list to append delays between characters
# delays = []

covert_bin = ""
covert = ""
i = 0
checkEOF = False
piece = 0


# create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
s.connect((ip, port))

# receive data until EOF
if MESSAGE:
        stdout.write("Overt Message:\n")
        stdout.flush()
data = s.recv(4096).decode()
while (data.rstrip("\n") != "EOF"):
        # output the data
        if (MESSAGE):
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
        # display delays if in Debug Mode
        if (DEBUG):
                stdout.write("\n{}\n".format(delta))
                stdout.flush()                


# close the connection to the server
s.close()

if DEBUG:
        print(covert_bin)
        
# Convert covert_bin to a character every 8 bits
while (i < len(covert_bin)):    # maybe len(cover_bin)-8 to get rid of last character (hopefully EOF)
        #process 1 byte at a time
        b = covert_bin[i:i+8]
        # convert it to ASCII
        n = int("0b{}".format(b), 2)
        # show each character in covert (to determine if EOF is one or three
        if DEBUG:
            stdout.write(chr(n)+"\n")
            stdout.flush()
        # if not currently looking for "EOF", start process
        if ((piece == 0) and (chr(n) == "E")):
            checkEOF = True
        try:
            covert += chr(n)
        except TypeError:
            covert += "?"
        if (checkEOF):
            piece+=1
        # if 3 chars since E, see if we have EOF and stop if so
        if (piece == 3):
            if (covert[-3:] == "EOF"):
                covert = covert[:-3]
                break
            else:
                piece = 0
                checkEOF = False

        # stop at the string "EOF"
        i +=8

# write covert message
stdout.write("\nCovert Message: {}\n".format(covert))
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
##
##
##      Timothy & John; 10-12-21
##      
##      - modified value for ONE constant to 0.05 so the covert message would
##         properly display in Linux
##      - added some other constants to streamline
##         debugging and displaying overt message
##
##
##      Timothy Oliver; 10-13-21
##      - added debug lines that confirmed EOF was actually the characters 'E',
##         'O', and 'F' as apposed to an ASCII character
##      - used string operations to check for EOF at end of output
##
##


        
