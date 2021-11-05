'''
==============================
MANUAL
==============================
python steg.py -<sr> -<bB> -o<val> [-i<val>] -w<val> [-h<val>]
-s      store
-r      retrieve
-b      bit mode
-B      byte mode
-o<val> set offset (default is 0)
-i<val> set interval (default is 1)
-w<val> set wrapper file. (this is the file you are storing something into or pulling something from)
-h<val> set hidden file. (this is the file that is being hidden in the wrapper)
======================================================
NOTES
======================================================
- Retrieval will only require a wrapper file so -h is not needed.
- Storage requires a wrapper file, and this file must be able to 
contain the hidden file.
'''





##############################
## Team Name:   The Fool
## Program:     Steg
## Date:        29 October 2021
###############################

import sys

def sentinelCheck(wrapper, offset, interval, index = 0):
    global SENTINEL

    #Run a while loop that checks for the sentinel bytes.
    ##print(f"{wrapper[offset]} = {SENTINEL[index]}")
    ##print(f"{offset} | {index}")
    while (index < len(SENTINEL)):
        if(wrapper[offset] == SENTINEL[index]):
            index += 1
            offset += interval
        else:
            return False
    return True



def storeByte(wrapper, hidden, offset, interval):
    global SENTINEL
    i = 0

    #For byte in hidden file
    while (i < len(hidden)):

        #Store the byte in the offset index
        wrapper[offset] = hidden[i]

        #increment by offset
        offset += interval
        i += 1
    i = 0

    #Repeat above for the sentinel.
    while (i < len(SENTINEL)):
        wrapper[offset] = SENTINEL[i]
        offset += interval
        i += 1
    return wrapper


def storeBit(wrapper, hidden, offset, interval):
    i = 0
    while (i < len(hidden)):
        for j in range(0,8):
            wrapper[offset] &= 0b11111110
            wrapper[offset] |= ((hidden[i] & 0b10000000) >> 7)
            hidden[i] = ((hidden[i] << 1) & 0b011111111)
            offset += interval
        i += 1
    i = 0
    while (i < len(SENTINEL)):
        for j in range(0,8):
            wrapper[offset] &= 0b11111110
            wrapper[offset] |= ((SENTINEL[i] & 0b10000000) >> 7)
            SENTINEL[i] = ((SENTINEL[i] << 1) & 0b011111111)
            offset += interval
        i += 1
    return wrapper

def retriBit(wrapper, offset, interval):

    global SENTINEL
    SEN_L = len(SENTINEL)
    found = False
    hidden = bytearray() # empty byte array


    #loop until the sentinel is found or once there is not enough bytes left
    while(not found and offset + 7 < len(wrapper)):

        hiddenByte = 0
        for j in range(8):
            # and the wrapper byte with 1 to get the value of the least significant bit
            bit = (wrapper[offset] & 0b00000001)

            # or the wrapper byte with the current hiddenByte to change the LSB
            # of the hiddenByte to the proper bit without changing the remaning bits
            hiddenByte |= bit

            # expect for the 8th bit, shift the hiddenByte 1 to the left
            if(j < 7):
                hiddenByte <<= 1

            offset += interval
        #add
        hidden.append(hiddenByte)
        # check if b matches a sentinel byte
        if (len(hidden) >= SEN_L):
            for i in range(SEN_L):
                if (hidden[i-SEN_L] != SENTINEL[i]):
                    break

                elif(i == SEN_L-1):
                    hidden = hidden[:-SEN_L]
                    found = True

    return hidden


def retriByte(wrapper, offset, interval):
    global SENTINEL
    hidden = bytearray()
    i = 0
    while (i < len(wrapper)):

        #if the sentinel bytes haven't been reached yet
        if (not sentinelCheck(wrapper, offset, interval)):

            #add the byte at the offset to the result file and increment by interval
            hidden.append(wrapper[offset])
            offset += interval
        else:

            #sentinel byte was found, EOF
            return hidden
    return hidden


offset = 0
interval = 1
wrapper_file = ""
hidden_file = ""

# Default method will be storing using the byte method
storing = True
byte_method = True

global SENTINEL
SENTINEL = bytearray([0, 255, 0, 0, 255, 0])


# Looking through the parameters given by the user 
for i in range(len(sys.argv)):

    # User wants to use retrieve data instead of store 
    if (sys.argv[i][0:2] == "-r"):
        storing = False

    # User wants to use bit method instead of byte method
    if (sys.argv[i][0:2] == "-b"):
        byte_method = False

    # Grabbing and storing the offset value
    if (sys.argv[i][0:2] == "-o"):
        offset = int(sys.argv[i][2:len(sys.argv[i])])

    # Grabbing and storing the interval value
    if (sys.argv[i][0:2] == "-i"):
        interval = int(sys.argv[i][2:len(sys.argv[i])])

    # Grabbing and storing the name of the wrapper file 
    if (sys.argv[i][0:2] == "-w"):
        wrapper_file = sys.argv[i][2:len(sys.argv[i])]

    # Grabbing and storing the name of the hidden file 
    if (sys.argv[i][0:2] == "-h"):
        hidden_file = sys.argv[i][2:len(sys.argv[i])]


# Reading into the wrapper file and storing its bytes into a bytearray
f = open(wrapper_file, 'rb')
wrapper_bytes = bytearray(f.read())
f.close()

# Reading into the hidden file and storing its bytes into a bytearray
# if a we are using the storing method
if (storing):
    f = open(hidden_file, 'rb')
    hidden_bytes = bytearray(f.read())
    f.close()

# If the parameters specified storage using the byte method
if (storing and byte_method):
    sys.stdout.buffer.write(storeByte(wrapper_bytes, hidden_bytes,
                                      offset, interval))

# If the parameters specified storage using the bit method
elif (storing and not byte_method):
    sys.stdout.buffer.write(storeBit(wrapper_bytes, hidden_bytes,
                                      offset, interval))

# If the parameters specified retrieval using the byte method
elif (not storing and byte_method):
    sys.stdout.buffer.write(retriByte(wrapper_bytes, offset, interval))

# ByteRetrieve
elif (not storing and not byte_method):
    sys.stdout.buffer.write(retriBit(wrapper_bytes, offset, interval))
