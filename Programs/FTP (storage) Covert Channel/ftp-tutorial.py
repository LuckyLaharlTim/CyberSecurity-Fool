# use Python 3
  
from ftplib import FTP
import sys
# specifies the number of bits the cipher will be broken down into
METHOD = "7"

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
# display the folder contents
for f in files:
    if METHOD == "7": 
        permissions = f[3:10]      
        binary = "0b"
        for i in range(len(permissions)):
            if permissions[i] == "-":
                binary += "0"
            else:
                binary += "1"
        print(permissions)
        print(binary)

#    outputString += chr(int(binary, 2))


#print(outputString)


