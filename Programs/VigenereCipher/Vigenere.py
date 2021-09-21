##################################
# Team Name:    The Fool
# Assignment:   Vigenere Cipher
# Date:         24 September 2021
##################################

import sys # import sys for standard input from command line

DEBUG = False
DEBUG2 = False    

# check if a letter is uppercase or lowercase
def checkCase(letter):
    if ((ord(letter) > 64) and (ord(letter) < 91)):
        return "upper"
    elif ((ord(letter) > 96) and (ord(letter) < 122)):
        return "lower"

# encoding message function
def encode(plaintext):

    text = []
    keyList = []
    currIndex = 0
    outputString = ""

    # put each individual character in a list (for comparison w/ characters in key)
    for char in plaintext:
        text.append(char)
    
    # get key and compare length to that of text; repeat key if key is smaller
    key = sys.argv[2]
    for char in key:
        if char != " ":
            keyList.append(char)

    while (len(keyList) < len(text)):
        keyList.append(keyList[currIndex])
        currIndex += 1

    for i in range(0,len(text)):
        # plaintext character is a capital letter
        if checkCase(text[i]) == "upper":
            if checkCase(keyList[i]) == "lower":
                encodedChar = chr(((((ord(text[i])-65) + (ord(keyList[i])-32-65))) % 26) + 65)  # need getting the correct character when the cases of the text and key are different - T.O.
            else:
                encodedChar = chr(((((ord(text[i])-65) + (ord(keyList[i])-65))) % 26) + 65)
            outputString += encodedChar
        # plaintext character is a lowercase letter
        elif checkCase(text[i]) == "lower":
            if checkCase(keyList[i]) == "upper":
                encodedChar = chr(((((ord(text[i])-97) + (ord(keyList[i])+32-97))) % 26) + 65)  # need getting the correct character when the cases of the text and key are different - T.O.
            else:
                encodedChar = chr(((((ord(text[i])-97) + (ord(keyList[i])-97))) % 26) + 97)
            outputString += encodedChar  
        # plaintext character is anything else, just repeat the character      
        else:
            outputString += text[i]

    # output the appropriate message
    print(outputString)


# decoding message function
def decode(ciphertext):

    text = []
    keyList = []
    currIndex = 0
    outputString = ""

    for char in ciphertext:
        text.append(char)

    # get key and compare length to that of text; repeat key if key is smaller
    key = sys.argv[2]
    for char in key:
        if char != " ":
            keyList.append(char)

    currIndex = 0

    while (len(keyList) < len(text)):
        keyList.append(keyList[currIndex])
        currIndex += 1

    for i in range(0,len(text)):
        # plaintext character is a capital letter
        if checkCase(text[i]) == "upper":
            if checkCase(keyList[i]) == "lower":
                encodedChar = chr(((((ord(text[i])-65) - (ord(keyList[i])-97))) % 26) + 65)  # need getting the correct character when the cases of the text and key are different - T.O.
            else:
                encodedChar = chr(((((ord(text[i])-65) - (ord(keyList[i])-65))) % 26) + 65)
            outputString += encodedChar
        # plaintext character is a lowercase letter
        elif checkCase(text[i]) == "lower":
            if checkCase(keyList[i]) == "upper":
                encodedChar = chr((((ord(text[i])-97) - (ord(keyList[i])+32-97)) % 26) + 65)  # need getting the correct character when the cases of the text and key are different - T.O.
            else:
                encodedChar = chr((((ord(text[i])-97) - (ord(keyList[i])-97)) % 26) + 97)
            outputString += encodedChar  
        # plaintext character is anything else, just repeat the character      
        else:
            outputString += text[i]

    # output the appropriate message
    print(outputString)


########
### MAIN
########


# differentiate between arguments of encoding or decoding
if sys.argv[1] == "-e":
    encode(sys.stdin.read())
elif sys.argv[1] == "-d":
    decode(sys.stdin.read())
else:
    print("Should I encode (python -e) or decode (python -d)?")



## Git Changes
    
# Format:
##  Name of coder; Date of change
##  Description of changes

##  Timothy Oliver; 9/20/2021
##  - I coded an initial working version of the Vigenere Cipher, encoding and ##    decoding
##
##




    

