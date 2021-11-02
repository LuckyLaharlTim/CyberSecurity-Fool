##################################
# Team Name:    The Fool
# Assignment:   XOR Crypto
# Date:         29 October 2021
##################################

##################################
# Manual
# python xor.py (-k key_file) < input > output
# Flags:
# -k | specifies the key file; can also be done
#    | in the KEY_DIR variable
# Notes:
#   Use notepad or similar to try to determine the
# file type after decoding.
#   Make sure to set the correct KEY_DIR or use -k
##################################

import sys

DEBUG = False
KEY_DIR = "key"

#If -k argument exists, replace KEY_DIR with text behind -k
for i in range(0,len(sys.argv)):
    if (sys.argv[i] == '-k'):
        KEY_DIR = sys.argv[i+1]

#Read STDIN
message = bytearray(sys.stdin.buffer.read())

#Read key file
f = open(KEY_DIR,'rb')
key = bytearray(f.read())
f.close()

#Debug print
if DEBUG:
    print(message)
    print(key)

#If key isn't long enough, wrap it until it is.
while len(key) < len(message):
    key = key*2

#XOR Cipher
result = bytearray(len(message))
for i in range(0, len(message)):
    result[i] = message[i] ^ key[i]

#Print result
sys.stdout.buffer.write(result)

## Git Changes
    
# Format:
##  Name of coder; Date of change
##  Description of changes

##  Zach and Josh; 10/12/2021
##  -Initial commit, comments, and -k flag.
