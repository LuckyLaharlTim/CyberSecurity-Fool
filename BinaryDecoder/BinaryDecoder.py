##################################
# Team Name:    The Fool
# Assignment:   Binary Decoder
# Date:         24 September 2021
##################################

import sys # import sys for standard input from command line

DEBUG = False
DEBUG2 = False


    
# making a ciphertext list to we can split up bits easily
#  as well as strings for individual characters and the final output
ciphertext = []
ciphertext2 = []
outputString = ""
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
if (len(ciphertext)%7==0):

    print("7 bit ASCII:\n")
    # making sectets of the binary characters
    while len(ciphertext) != 0:
        for i in range(0,7):
            charString+=ciphertext.pop(0)
            if (i==6):
                outputString+=chr(int(charString,2))
                if DEBUG:
                    print(outputString+"\n\n")
                charString = "0b"
    print(outputString)



# following while loop iterates if the bitstring is has 8 bit ASCII
#   if the bitstring length is divisible by 7 & 8, both iterate
#   (so far the messages have been the same,regardless of length)
if (len(ciphertext2)%8==0):

    print("8 bit ASCII:\n")
    # making octets of the binary characters
    while len(ciphertext2) != 0:
        for i in range(0,8):
            charString+=ciphertext2.pop(0)
            if (i==7):
                outputString+=chr(int(charString,2))
                if DEBUG:
                    print(outputString+"\n\n")
                charString = "0b"
    print(outputString)


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
##



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












#### seven bit ASCII if you want to manually backspace     <-- irrelevant, just left if it helps
##print("7 bit binary:\n\n")
##    # making sectets of the binary characters
##    while len(ciphertext) != 0:
##        for i in range(0,7):
##            charString+=ciphertext.pop(0)
##            if (i==6):
##                currChar = chr(int(charString,2))
##                if currChar==chr(8):
##                    outputString.rstrip(lastChar)
##                else:
##                    outputString+=currChar
##                if DEBUG:
##                    print(outputString+"\n\n")
##                charString = "0b"
##                lastChar = currChar
##    print(outputString)




    

