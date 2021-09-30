##################################
# Team Name:    The Fool
# Assignment:   Binary Decoder
# Date:         29 September 2021
##################################

# use Python 3
  
from ftplib import FTP

# specifies the number of bits the cipher will be broken down into
METHOD = "10"

# FTP server details
IP = "138.47.157.5"
PORT = 21
USER = "anonymous"
PASSWORD = ""
FOLDER = "/" + METHOD + "/"
USE_PASSIVE = False # set to False if the connection times out

# connect and login to the FTP server
ftp = FTP()
ftp.connect(IP, PORT)
ftp.login(USER, PASSWORD)
ftp.set_pasv(USE_PASSIVE)

# navigate to the specified directory and list files
ftp.cwd(FOLDER)
files = []
ftp.dir(files.append)

# exit the FTP server
ftp.quit()

# String that will hold the decoded message
outputString = ""

# String that will hold the characters from the permissions 
permissions = ""

# String that will hold the binary equivalent of the permissions string 
binary = ""

# display the folder contents
for f in files:

        # 7 bit message
	if METHOD == "7":

            if f[:3] == "---": # JC added this line to omit all files with anything in the first 3 spaces

                # Getting the 7 rightmost bits from the permissions  
	        permissions = f[3:10]      

                # The resulting binary string cannot be converted unless it is preceded by '0b' (at least in python)
		binary = "0b"

		for i in range(len(permissions)):

                    # If the character in permissions is a dash then store a 0 in the binary string
		    if permissions[i] == "-":
		        binary += "0"

                    # Any other character in permissions will be stored as a 1 in the binary string 
		    else:
			binary += "1"

                # Converting the binary string back to a character and storing it in the output string 
		outputString += chr(int(binary, 2))

        # 10 bit message 
	elif METHOD == "10":

                # Getting all ten characters from permissions 
		permissions += f[:10]
		for i in range(len(permissions)):
                 
                    # If the character in permissions is a dash then store a 0 in the binary string
		    if permissions[i] == "-":
		        binary += "0"

                    # Any other character in permissions will be stored as a 1 in the binary string
		    else:
		        binary += "1"

                    # Once the binary string reaches 7 bits 
		    if len(binary) == 7:

                        # Prepend the '0b' to the binary string for proper conversion
		        binary  = "0b{}".format(binary)

                        # Converting the binary string back to a character and storing it in the output string
			outputString += chr(int(binary, 2))

                        # Clearing the binary string 
			binary = ""

# Printing out the decoded message
print(outputString)


## Git Changes
    
# Format:
##  Name of coder; Date of change
##  Description of changes

##  Josh, John, Jason; 9-29-21
##  Added 7 bit method and got it to work

##  Jason; 9-30-21
##  Attempted to add 10 bit method, message will print out but with a lot of "noise" before and after

## Josh; 9-30-21
## Commented large portion of the code and made a few minor improvements
