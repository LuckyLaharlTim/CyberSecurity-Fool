'''
========
MANUAL
=========
python strip.py
===========
NOTES
===========
- All you do is replace the string with the stuff you got
from the given executuable.

- Then put it into a text file and pipe into typing-final.py

- Thats It. DONT FUCK UP!!!!! :)))))))))

'''


string = "['C', 'a', 'n', ' ', 'y', 'o', 'u', ' ', 's', 'm', 'e', 'l', 'l', ' ', 't', 'h', 'e', ' ', 'p', 'o', 'p', 'c', 'o', 'r', 'n', '?', 'Ca', 'an', 'n ', ' y', 'yo', 'ou', 'u ', ' s', 'sm', 'me', 'el', 'll', 'l ', ' t', 'th', 'he', 'e ', ' p', 'po', 'op', 'pc', 'co', 'or', 'rn', 'n?']\n['0.96', '0.39', '0.82', '0.63', '0.74', '0.38', '0.33', '0.17', '0.65', '0.28', '0.69', '0.21', '0.83', '0.59', '0.47', '0.24', '0.54', '0.28', '0.83', '0.75', '0.58', '0.27', '0.42', '0.77', '0.88', '0.45', '0.68', '0.96', '0.94', '0.75', '0.39', '0.64', '0.68', '0.83', '0.66', '0.66', '0.17', '0.62', '0.69', '0.62', '0.53', '0.19', '0.97', '0.45', '0.99', '0.77', '0.13', '0.11', '0.23', '0.19', '0.61']"
string = string.replace("[", "").replace("]","").replace(", ",",").replace("'", "")
print(string)
