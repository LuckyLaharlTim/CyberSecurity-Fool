##################################
# Manual
# echo "[epoch_time]" | python3 timelock-final.py
# - This method requires you to set the 'now' time in the code
#   via the 'now_str' variable
# OR
# echo "[epoch_time]" | python3 timelock-final.py -r
# - This method uses the current system time as the 'now' time
##################################

##################################
# Team Name:    The Fool
# Assignment:   Timelock
# Date:         29 October 2021
##################################

from hashlib import md5
from datetime import datetime
from sys import *
import pytz

DEBUG = False

# Relevant second interval 
INTERVAL = 60

# Local time zone 
local_time = pytz.timezone("US/Central")

def argCheck(flag):
    for i in argv:
        if (i == flag):
            return True
    return False

# add -r flag for real current time
if (argCheck("-r")):
    now = datetime.now()
    utc_now = now.astimezone(pytz.utc)
# for ease of checking with pdf, set current time to specified string    
else:
    now_str = "2021 10 29 11 41 00"

    # Converting the current time to a datetime object  
    naive_datetime = datetime.strptime(now_str, "%Y %m %d %H %M %S")

    # Localizing the current time to the timezone given in the 'local_time' variable
    local_datetime = local_time.localize(naive_datetime)

    # Converting current time from the local timezone time 
    utc_now = local_datetime.astimezone(pytz.utc)

if (DEBUG):
    print(utc_now)
    
date = []

for line in stdin:
    date =  line.split()

# Taking the epoch time given and converting it to a datetime object
epoch = datetime.strptime(" ".join(date), "%Y %m %d %H %M %S")

# Localizing the epoch time to the timezone given in the 'local_time' variable
epochLocal_datetime = local_time.localize(epoch)

# Converting epoch time from the local timezone to utc
epoch_utc = epochLocal_datetime.astimezone(pytz.utc)

if (DEBUG):
    print(epoch_utc)

# Getting the total seconds elasped between the current time and the epoch time 
difference = ((utc_now -  epoch_utc).total_seconds())

# Subtracting the differe
difference -= (difference % INTERVAL)

if (DEBUG):
    print(difference)

# Hashing the difference calculated above 
md5_1 = md5(str(int(difference)).encode('UTF-7'))

# Double hashing the difference 
md5_2 = md5(md5_1.hexdigest().encode('UTF-7'))

if (DEBUG):
    print(md5_2.hexdigest())

# Empty string that will hold the resulting code 
code = ""

# For every character in the md5_2 hash string 
for char in md5_2.hexdigest():

    # If the current character is a 'char'
    if char.isalpha():

        # Add it to the code
        code += char

        # If the length of the code is two then break out of the loop
        if (len(code) == 2):
            break

# For every character in the md5_2 hash string (in reverese order)
for char in str(md5_2.hexdigest()[::-1]):

    # If the current character is an 'int'
    if char.isnumeric():

        # Add it to the code
        code += char

        # If the length of the code is four then break out of the loop
        if (len(code) == 4):
            break

# add the middle character to the end of the code (for challenge)
#code += str(md5_2.hexdigest())[len(str(md5_2.hexdigest())) // 2]

if (DEBUG):
    print(code)

# Writing the code to standard output 
stdout.write(code + "\n")
stdout.flush()



# Format:
##  Name of coder; Date of change
##  Description of changes

##  Josh; 10/18/2021
##  -Formatted the current and epoch time correctly but was unable to
##   double hash the resulting difference in the times. 
##
##
##  Josh, Zach; 10/21/2021
##  -Correctly double hashed the resulting time difference and obtained the
##   appropriate code from the double hashed string
