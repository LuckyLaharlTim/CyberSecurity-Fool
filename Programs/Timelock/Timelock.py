###########################
# Team Name:    The Fool
# Assignment:   Timelock
# Date:         29 October 2021
##########################


from sys import stdin, stdout
from time import time
from datetime import datetime, timedelta
from hashlib import md5
import pytz

INTERVAL = 60
MANUAL_DATETIME = "2017 04 23 18 02 30"
#MANUAL_DATETIME = stdin.read()

# general format for getting output code:
#   <position relative to other char type>
#   <number of such characters to obtain>
#   <LR = 'left to right', RL = the opposite>
#   ex: letters = "25RL" means after getting numbers, 
#       get first 5 letters in hash from right to left
letters = "12LR"
numbers = "22RL"

def getCodeLetters(hashstr, direct):
    code = ""
    letCount = 0
    if (direct[2:] == "RL"):
        hashstr = hashstr[::-1]
    for char in hashstr:
        if(char.isalpha() and (letCount < int(direct[1]))):
            if char.isalpha():
                code += char
                letCount += 1

    return code


def getCodeNumbers(hashstr, direct):
    code = ""
    numCount = 0

    if (direct[2:] == "RL"):
        hashstr = hashstr[::-1]
    for char in hashstr:
        # python2 does not include str.isnumeric()
        try:
            if ((int(char) > -1) and (numCount<int(direct[1]))):
                code += char
                numCount+=1
            elif not(numCount<direct[1]):
                break
        except ValueError:
            pass

    return code


# create epoch datetime
spaces = 0
year = ""
month = ""
day = ""
hour = ""
minute = ""
second = ""
for char in MANUAL_DATETIME:
    if (char == " "):
        spaces += 1
    elif (spaces == 0):
        year += char
    elif (spaces == 1):
        month += char
    elif (spaces == 2):
        day += char
    elif (spaces == 3):
        hour += char
    elif (spaces == 4):
        minute += char
    elif (spaces == 5):
        second += char

#epoch = 
utc = pytz.utc
fmt = '%Y-%m-%d %H:%M:%S %z'
epoch = utc.localize(datetime(int(year), int(month), int(day), int(hour), int(minute), int(second)))
#t0 = epoch.time()
t1 = utc.localize(datetime.now())#.time()

deltaTime = t1 - epoch
deltaSeconds = round(deltaTime.total_seconds())
#current_dt = utc.localize(datetime.fromtimestamp(deltaTime))

# md5 hashes
md5_1 = md5(b'(deltaSeconds - (deltaSeconds%60))').hexdigest()
md5_2 = md5(b'(md5_1)').hexdigest()

# get code using md5_2
code = ""

if (letters[0] == "1"):
    code += getCodeLetters(str(md5_2), letters)
    code += getCodeNumbers(str(md5_2), numbers)
elif (numbers[0] == "1"):
    code += getCodNumbers(str(md5_2), numbers)
    code += getCodeLetters(str(md5_2), letters)

###################
# output generation
###################
# current time
outputString = "Current {UTC}: " + t1.strftime(fmt) + "\n"

# epoch time
outputString += "Epoch {UTC}: " + epoch.strftime(fmt) + "\n"

# seconds elapsed from epoch
outputString += "Seconds: " + str(deltaSeconds) + "\n"

# seconds elapsed from epoch to nearest minute
outputString += "Seconds: " + str(deltaSeconds - deltaSeconds%60) + "\n"

# md5 #1
outputString += "MD5 #1: " + str(md5_1) + "\n"

# md5 #2
outputString += "MD5 #2: " + str(md5_2) + "\n"

# code
outputString += "CODE: " + code + "\n"


stdout.write(outputString)
stdout.flush()

#############
# git changes
#############
##
##  Timothy, 10/21/2021
##  - drafted up initial version of the file
##      from getting epoch from string or file to output
##  - current issues, 
##      ~ md5 sum hashes appear to always be the same;
##          using hexdigest() gest ride of the object description text, 
##          but looks to also be keeping it the same
##      ~ I can't figure out how to put a comma betweet the 4 zeroes of
##          the current and epoch time offsets 
##      ~ The seconds still have the first decimal point
