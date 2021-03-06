##################################
# Team Name:    The Fool
# Assignment:   Vigenere Cipher
# Date:         24 September 2021
##################################

##################################
# Manual
#
# python(3) Vigenere.py <flags> < input > output
#
# Flags:
# -e | will encode input and write to output
#      or terminal if input/output not provided
# -d | will decode input and write to output
#      or terminal if input/output not provided 
##################################

import sys # import sys for standard input from command line

DEBUG = False
DEBUG2 = False

# check if a letter is uppercase or lowercase
def checkCase(letter):
    if ((ord(letter) > 64) and (ord(letter) < 91)):
        return "upper"
    elif ((ord(letter) > 96) and (ord(letter) < 123)):
        return "lower"

# encoding message function
def process(message):

    text = []
    keyList = []
    currIndex = 0
    outputString = ""

    # put each individual character in a list (for comparison w/ characters in key)
    for char in message:
        text.append(char)

    # get key and compare length to that of text; repeat key if key is smaller
    key = sys.argv[2]
    for char in key:
        if char != " ":
            keyList.append(char)

    while (len(keyList) < len(text)):
        keyList.append(keyList[currIndex])
        currIndex += 1
    currIndex = 0

    if sys.argv[1] == "-e":
        for i in range(0,len(text)):
            # plaintext character is a capital letter
            if checkCase(text[i]) == "upper":
                if checkCase(keyList[currIndex]) == "lower":
                    encodedChar = chr(((((ord(text[i])-65) + (ord(keyList[currIndex])-32-65))) % 26) + 65)  # need getting the correct character when the cases of the text and key are different - T.O.
                else:
                    encodedChar = chr(((((ord(text[i])-65) + (ord(keyList[currIndex])-65))) % 26) + 65)
                outputString += encodedChar
                currIndex += 1
            # plaintext character is a lowercase letter
            elif checkCase(text[i]) == "lower":
                if checkCase(keyList[currIndex]) == "upper":
                    encodedChar = chr(((((ord(text[i])-97) + (ord(keyList[currIndex])-65))) % 26) + 97)  # need getting the correct character when the cases of the text and key are different - T.O.
                else:
                    encodedChar = chr(((((ord(text[i])-97) + (ord(keyList[currIndex])-97))) % 26) + 97)
                outputString += encodedChar
                currIndex += 1
            # if the plaintext character is a newline character
            elif (text[i] == "\n"):
                outputString += "\n"
                currIndex = 0
            # plaintext character is anything else, just repeat the character
            else:
                outputString += text[i]


    elif sys.argv[1] == "-d":
        for i in range(0,len(text)):
        # plaintext character is a capital letter
            if checkCase(text[i]) == "upper":
                if checkCase(keyList[currIndex]) == "lower":
                    encodedChar = chr(((((ord(text[i])-65) - (ord(keyList[currIndex])-32-65))) % 26) + 65)  # need getting the correct character when the cases of the text and key are different - T.O.
                else:
                    encodedChar = chr(((((ord(text[i])-65) - (ord(keyList[currIndex])-65))) % 26) + 65)
                outputString += encodedChar
                currIndex += 1
            # plaintext character is a lowercase letter
            elif checkCase(text[i]) == "lower":
                if checkCase(keyList[currIndex]) == "upper":
                    encodedChar = chr(((((ord(text[i])-97) - (ord(keyList[currIndex])+32-97))) % 26) + 97)  # need getting the correct character when the cases of the text and key are different - T.O.
                else:
                    encodedChar = chr(((((ord(text[i])-97) - (ord(keyList[currIndex])-97))) % 26) + 97)
                outputString += encodedChar
                currIndex += 1
            # if the plaintext character is a newline character
            elif (text[i] == "\n"):
                outputString += "\n"
                currIndex = 0
            # plaintext character is anything else, just repeat the character
            else:
                outputString += text[i]


    # output the appropriate message
    sys.stdout.write(outputString)


########
### MAIN
########


# differentiate between arguments of encoding or decoding
if __name__ == "__main__":
    message = sys.stdin.read()
    if (sys.argv[1] in ["-e", "-d"]):
        process(message)
    else:
        sys.stdout.write("Should I encode (python -e) or decode (python -d)?")



## Git Changes

# Format:
##  Name of coder; Date of change
##  Description of changes

##  Timothy Oliver; 9/20/2021
##  - I coded an initial working version of the Vigenere Cipher, encoding and
##    decoding
##  - There is an issue with properly en/de-coding when the key and plain/cipher-text
##    are different cases
##
##
##  Jason, Josh, and Timothy; 9/22/2021
##  - fixed errors when text and key were different cases by
##    changing incorrect range in checkCase and corecting number added to
##    final value before using char function
##    (had +65 instead of +97 for lowercase and vice versa)
##  - noticed error in output when there was a newline character;
##    list holding key characters would continue from index rather than treating
##    new lines like a new text
##  - fixed by increasing use of currIndex variable, new line characters also
##    set currIndex to 0 (next read character matches with beginning of key)
##
##
##  Timothy Oliver; 9/24/2021
##  - refactored encode and decode functions into one process function
##    with only the building of outputString running depending on the flag
##  - made the outputString be written from stdout rather than printed