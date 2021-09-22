import sys

def encrypt(plaintext, key):
    cipher = ""
    keyIndex = 0
    for i in range(len(plaintext)):
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
        if not cipher[i].isalpha():
            plaintext += cipher[i]
        else:
            keyIndexInAlphabet = letters.index(key[keyIndex].lower())
            if cipher[i].isupper():
                cipherIndex = letters.index(cipher[i]) - 26
                plaintext += letters[((26 + cipherIndex - keyIndexInAlphabet) % 26)]
            else:
                cipherIndex = letters.index(cipher[i])
                plaintext += letters[((26 + cipherIndex - keyIndexInAlphabet) % 26)]
            keyIndex += 1
    
    return plaintext

def main():
    numOfArgs = len(sys.argv)

    if numOfArgs == 2:
        print("Please provide a key")
        sys.exit()
    elif numOfArgs == 1:
        print("Please specify encryption ('-e') or decryption ('-d), and provide a key")
        sys.exit()

    key = sys.argv[2]
    if len(key) < len(sys.argv[1]):
        key_index = 0
        for i in range(len(sys.argv[1]) - len(key)):
            key += key[key_index]
            if key_index >= len(key):
                i = 0
            else:
                i += 1 

    if sys.argv[1] == '-e':
        for line in sys.stdin:
            cipher = encrypt(line, sys.argv[2])
            print(cipher)
    elif sys.argv[1] == '-d':
        for line in sys.stdin:
            plaintext = decrypt(line, sys.argv[2])
            print(plaintext)
    else:
        print("Not a valid option")
        sys.exit()

letters = list(map(chr, range(97, 123)))
letters += list(map(chr, range(65, 91)))

if __name__ == "__main__":
    main()


