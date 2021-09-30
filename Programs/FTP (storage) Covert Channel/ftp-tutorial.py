##################################
# Team Name:    The Fool
# Assignment:   Binary Decoder
# Date:         29 September 2021
##################################

# use Python 3
  
from ftplib import FTP
import sys
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
outputString = ""
permissions = ""
binary = ""
# display the folder contents
for f in files:
	if METHOD == "7":
		if f[0] == "-" and f[1] == "-" and f[2] == "-": # JC added this line to omit all files with anything in the first 3 spaces
			permissions = f[3:10]      
			binary = "0b"
			for i in range(len(permissions)):
				if permissions[i] == "-":
					binary += "0"
				else:
					binary += "1"
			outputString += chr(int(binary, 2))
	elif METHOD == "10":
		permissions += f[:10]
		for i in range(len(permissions)):
			if permissions[i] == "-":
				binary += "0"
			else:
				binary += "1"
			if len(binary) == 7:
				newBinary = "0b{}".format(binary)
				outputString += chr(int(newBinary, 2))
				binary = ""

print(outputString)


## Git Changes
    
# Format:
##  Name of coder; Date of change
##  Description of changes

##  Josh, John, Jason; 9-29-21
##  Added 7 bit method and got it to work

##  Jason; 9-30-21
##  Attempted to add 10 bit method, message will print out but with a lot of "noise" before and after