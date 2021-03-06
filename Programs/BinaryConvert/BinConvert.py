import sys

##################################
# Manual
# python BitConvert.py <flags> < input > output
# Flags:
# -0 | will define what is considered a 0
# -1 | will define what is considered a 1
# Notes:
# The flags can be used or the variables below.
##################################

#What is a zero and what is a one? Put the characters here, or use -0 and -1.
ONE = ""
ZERO = ""

for i in range(0,len(sys.argv)):
    if (sys.argv[i] == '-1'):
        ONE = sys.argv[i+1]

for i in range(0,len(sys.argv)):
    if (sys.argv[i] == '-0'):
        ZERO = sys.argv[i+1]

string = sys.stdin.read()
binary=""
for char in string:
    if char == ZERO:
        binary += '0'
    elif char == ONE:
        binary += '1'
sys.stdout.write(binary)
