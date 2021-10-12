##################################
# Team Name:    The Fool
# Assignment:   XOR Crypto
# Date:         Late October 2021
##################################

import sys # import sys for standard input from command line

DEBUG = True
KEY = open("key")
outputBin = b'0'

key = KEY.read()
KEY.close()
keyBytes = bytearray(key, 'utf-8')
if DEBUG:
    print("{}\n\n{}\n\n".format(key, keyBytes))

text = sys.stdin.buffer.read()
#textBytes = bytearray(text, 'utf-8')
if DEBUG:
    print(text)

for i in range(0, len(keyBytes)):   # gives an error, use 'min(len(text),len(keyBytes))' to bypass for now
    outputBin += b'{}'.format(text[i] ^ keyBytes[i])

sys.stdout.buffer.write(outputBin)    



## Git Changes
    
# Format:
##  Name of coder; Date of change
##  Description of changes

##  Timothy Oliver; 10/11/2021
##  - I made a preliminary attempt at the code
##  - Despite the fact that the ciphertext and key are
##     of the same size, their byte arrays are of different lengths
##  - Couldn't get the outputBin variable to be the appropriate type
##     for the stdout.buffer.write function






    

