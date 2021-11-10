#!/bin/sh
HOST='localhost'
USER='anonymous'
PASSWD='\n'
#FILE='file.txt'

ftp -inv $HOST << EOF
user $USER  $PASSWD
#COMMANDS HERE

EOF