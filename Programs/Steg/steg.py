import sys

def sentinelCheck(wrapper, offset, interval, index = 0):
    global SENTINEL
    
    #If the byte equals the sentinel at the current index, return the result of calling the function with index + 1
    if (wrapper[offset] == SENTINEL[index]):
        
        #If the index is out of the range of the sentinel, it has found the entire sentinel, return true.
        if (index < len(SENTINEL)):
            
            #If not, increment offset and index and run the function again.
            index += 1
            offset += interval
            return sentinelCheck(wrapper, offset, interval, index)
        else:
            return True
    else:
        return False

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
    while (i< len(SENTINEL)):
        wrapper[offset] = SENTINEL[i]
        offset += interval
        i += 1
    return wrapper

def storeBit(wrapper, hidden, offset, interval):
    i = 0
    j = 0
    while(i < len(hidden)):
        while(j < 7):
            wrapper[offset] &= 11111110
            wrapper[offset] |= ((hidden[i] & 10000000) >> 7)
            hidden[i] <<= 1
            offset += interval
            j += 1
        i += 1

    i = 0
    j = 0
    while(i < len(SENTINEL)):
        while(j < 7):
            wrapper[offset] &= 11111110
            wrapper[offset] |= ((SENTINEL[i] & 10000000) >> 7)
            SENTINEL[i] <<= 1
            offset += interval
            j += 1
        i += 1


def retriByte(wrapper, offset, interval):
    global SENTINEL
    hidden = bytearray()
    i = 0
    while (i < len(wrapper)):
        
        #if the sentinel bytes haven't been reached yet
        if (not sentinelCheck(wrapper, offset, interval)):
            
            #add the byte at the offset to the result file and increment by interval
            hidden.extend(wrapper[offset])
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
SENTINEL = bytearray([0x0, 0xff, 0x0, 0x0, 0xff, 0x0])


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
