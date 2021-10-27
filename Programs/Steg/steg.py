import sys

offset = 0
interval = 1
wrapper_file = ""
hidden_file = ""
storing = True
byte_method = True
global SENTINEL = 


for i in range(len(sys.argv)):
    if (sys.argv[i][0:2] == "-r"):
        storing = False
    if (sys.argv[i][0:2] == "-b"):
        byte_method = False
    if (sys.argv[i][0:2] == "-o"):
        offset = sys.argv[i][2:len(sys.argv[i])]
    if (sys.argv[i][0:2] == "-i"):
        interval = sys.argv[i][2:len(sys.argv[i])]
    if (sys.argv[i][0:2] == "-w"):
        wrapper_file = sys.argv[i][2:len(sys.argv[i])]
    if (sys.argv[i][0:2] == "-h"):
        hidden_file = sys.argv[i][2:len(sys.argv[i])]


f = open(wrapper_file, 'rb')
wrapper_bytes = bytearray(f.read())
f.close()

f = open(hidden_file, 'rb')
hidden_bytes = bytearray(f.read())
f.close()

if (storing and byte_method):
    sys.stdout.buffer.write(storeByte(wrapper_bytes, hidden_bytes,
                                      offset, interval))

else if (storing and not byte_method)
    sys.stdout.buffer.write(storeBit(wrapper_bytes, hidden_bytes,
                                      offset, interval))

else if (not storing and byte_method):
    sys.stdout.buffer.write(retriByte(wrapper_bytes, hidden_bytes,
                                      offset, interval))

def storeByte(wrapper, hidden, offset, interval):
    global SENTINEL
    i = 1
    while (i < len(hidden)):
        wrapper[offset] = hidden[i]
        offset += interval
        i += 1
    i = 0
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

def sentinelCheck(wrapper, offset, interval, index = 0):
    if (wrapper[offset] == SENTINEL[index]):
        if (index < 6):
            index += 1
            offset += interval
            return sentinelCheck(wrapper, offset, interval, index)
        else:
            return True
    else:
        return False

def retriByte(wrapper, offset, interval):
    global SENTINEL
    hidden = bytearray()
    i = 0
    while (i < len(wrapper)):
        if sentinelCheck(wrapper, offset, interval):
            hidden.extend(wrapper[offset])
            offset += interval
        else:
            return hidden
    return hidden


