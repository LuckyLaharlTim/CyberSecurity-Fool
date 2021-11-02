##################################
# Team Name:    The Fool
# Assignment:   Binary Decoder
# Date:         24 September 2021
##################################

##################################
# Manual
# python BinaryDecoder.py <flags> < input > output
# Flags:
# -7 | will force 7 bit decoding
# -8 | will force 8 bit decoding
# -e | will print out which bit method is used.
# Notes:
# If the bits provided to the program are not divisible 
# by 7 or 8, or by whichever flag used, no output will be
# given.
##################################

import sys # import sys for standard input from command line

DEBUG = False
DEBUG2 = False

# Simple function for checking arguments, like -e or similar.
def argCheck(flag):
    for i in sys.argv:
        if (i == flag):
            return True
    return False

# making a ciphertext list to
# we can split up bits easily
#  as well as strings for individual characters and the final output
ciphertext = []
ciphertext2 = []
outputString = []
charString = "0b"


text = sys.stdin.read()
#text.strip("\n")
if DEBUG:
    print(text)

# put the actual bits of encoded message in the 'ciphertext' list
for bit in text:

# removes the new line character from the end of each bitstring;
#   should be alternative to text.strip("\n") (though the latter fails for some reason
    if (bit != "\n"):  

    #puts individual bits in the ciphertext list
        ciphertext.append(bit)
        ciphertext2.append(bit)

if (DEBUG):
    # checking current status of ciphertext; should be full of 0 or 1 chars
    print(ciphertext)
    

if DEBUG2:
    print(len(ciphertext))
    print((len(ciphertext)%7==0))
    print((len(ciphertext2)%8==0))

# following while loop iterates if the bitstring is has 7 bit ASCII and prints such
if ((len(ciphertext)%7==0) and not argCheck('-8')):

    #print("7 bit ASCII:\n")
    # making sectets of the binary characters
    while len(ciphertext) != 0:
        for i in range(0,7):
            charString+=ciphertext.pop(0)
            if (i==6):
                if (chr(int(charString,2)) == '\b'):
                    outputString.pop(len(outputString)-1)
                else:
                    outputString+=chr(int(charString,2))
                if DEBUG:
                    print(outputString+"\n\n")
                charString = "0b"
    #print(''.join(outputString))
    if argCheck('-e'):
        sys.stdout.write("7 bit ASCII:\n")
    sys.stdout.write(''.join(outputString) + "\n")
    outputString = []


# following while loop iterates if the bitstring is has 8 bit ASCII
#   if the bitstring length is divisible by 7 & 8, both iterate
#   (so far the messages have been the same,regardless of length)
if ((len(ciphertext2)%8==0)and not argCheck('-7')):

    ##print("8 bit ASCII:\n")
    # making octets of the binary characters
    while len(ciphertext2) != 0:
        for i in range(0,8):
            charString+=ciphertext2.pop(0)
            if (i==7):
                if (chr(int(charString,2)) == '\b'):
                    outputString.pop(len(outputString)-1)
                else:
                    outputString+=chr(int(charString,2))
                if DEBUG:
                    print(outputString+"\n\n")
                charString = "0b"
    ##print(''.join(outputString))
    if argCheck('-e'):
        sys.stdout.write("8 bit ASCII:\n")
    sys.stdout.write(''.join(outputString) + "\n")

#########################################
####    In response to infection.txt . . .
##########################################
## Message:
##  /*
##  Code, compile, and execute the following code on a variety of operating systems
##      at the very least try a version of Linux and a version of Windows). Comment
##      on your obeservations. Then comment on what you think the code is, what it
##      does, how an attacker might use it, and what you might do to deal with such
##      an attack.
##  */
##
##  int main(int argc, char** argv)
##  {
##      for (;;)
##          system(argv[0]);
##  }
##
##
## Comments:
##  On Linux VM:
##    Top running on a seperate terminal shows 85% of CPU resources are used by the
##    terminal running this program. After a while of execution, an error stating
##    forking has failed is repeated in the terminal. Closing the terminal removed
##    all trace of the program.
##  On Windows:
##    CPU(i7-8700k) usage slowly climbed to 25% (appeared to keep climbing, but even
##    slower). When the terminal was closed, the forked programs started spamming an
##    error message that would reappear as soon as it was dismissed. Task manager
##    was unable to be interacted with while the error message was on screen. A full
##    restart was needed. "The worst part about this program was it made me sit
##    through a Windows update." - Zach.
##
##  This program obviously forks itself over and over again in an attempt to hog
##  computer resources. It can very easily cripple a system, either by using
##  resources, or causing other adverse effects. An attacker can use this as a
##  tactic to annoy and slowdown a user, and if a restart is in order, the user
##  loses valuable time and may have to run another program that wasn't done
##  with it's task. Always using a terminal emulator that can be closed manually
##  seems to be a good protection against this specific program, but if another
##  malicious program opened its own terminals, the only good option would seem
##  to be restarting.



## Git Changes
    
# Format:
##  Name of coder; Date of change
##  Description of changes

##  Timothy Oliver; 9/20/2021
##  - I coded an initial working version of the Binary Decoder
##      * there are a few points I believe can work better, i.e.,
##      * removing the new line character at the end of files from stdin
##      * which I accomplished by having an if statement that ignores the
##      * character (might cause issues if there is an actual line break, though I believe it will not)
##  - also started description of plaintext infection.txt (pretty sure it's Bacteria in C


##  Zachery, John, Anuj; 9/21/21
##  Made backspaces work properly (if a backspace was piped into another program it could cause issues)
##  Output now goes through STDOUT instead of print
##  Added arguments for the program
##    -e will show what bit ASCII is being shown
##    -7 will force 7 bit ASCII
##    -8 will force 8 bit ASCII
##  7/8 bit will still not show up if the bits are not divisible by 7/8
