import sys

def encrypt(plaintext, key):
    cipher = ""
    keyIndex = 0
    for i in range(len(plaintext)):
        if keyIndex >= len(key):
            keyIndex = 0
        if not key[keyIndex].isalpha():
            keyIndex += 1
        if not plaintext[i].isalpha():
            cipher += plaintext[i]
        else:
            keyIndexInAlphabet =  letters.index(key[keyIndex].lower())
            if plaintext[i].isupper():
                plaintextIndex = letters.index(plaintext[i]) - 26
                cipher += letters[((plaintextIndex + keyIndexInAlphabet) % 26)].upper()
            else:
                plaintextIndex = letters.index(plaintext[i])
                cipher += letters[((plaintextIndex + keyIndexInAlphabet) % 26)]
            keyIndex += 1

    return cipher

def decrypt(cipher, key):
    plaintext = ""
    keyIndex = 0
    for i in range(len(cipher)):
        if keyIndex >= len(key):
            keyIndex = 0
        if not key[keyIndex].isalpha():
            keyIndex += 1
        if not cipher[i].isalpha():
            plaintext += cipher[i]
        else:
            keyIndexInAlphabet = letters.index(key[keyIndex].lower())
            if cipher[i].isupper():
                cipherIndex = letters.index(cipher[i]) - 26
                plaintext += letters[((26 + cipherIndex - keyIndexInAlphabet) % 26)].upper()
            else:
                cipherIndex = letters.index(cipher[i])
                plaintext += letters[((26 + cipherIndex - keyIndexInAlphabet) % 26)]
            keyIndex += 1
    
    return plaintext
'''
def extendKey(key, plaintext):
    new_key = key
    key_index = 0
    for i in range(len(plaintext) - len(key)):
        new_key += key[key_index]
        if key_index >= len(key):
            key_index = 0
        else:
            key_index += 1

    return new_key
'''

def main():
    numOfArgs = len(sys.argv)

    if numOfArgs == 2:
        print("Please provide a key")
        sys.exit()
    elif numOfArgs == 1:
        print("Please specify encryption ('-e') or decryption ('-d), and provide a key")
        sys.exit()

    key = sys.argv[2]

    if sys.argv[1] == '-e':
        cipher = ""
        for line in sys.stdin:
            cipher += encrypt(line, key)
        print('\n'+ cipher)
                
    elif sys.argv[1] == '-d':
        plaintext = ""
        for line in sys.stdin:
            plaintext += decrypt(line, key)
        print('\n' + plaintext)
    else:
        print("Not a valid option")
        sys.exit()

letters = list(map(chr, range(97, 123)))
letters += list(map(chr, range(65, 91)))

if __name__ == "__main__":
    main()


