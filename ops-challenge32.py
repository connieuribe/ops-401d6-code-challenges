#!/usr/bin/python3
import platform
import os
import hashlib
from datetime import datetime
# Script: Ops 401 Class 33 Ops Challenge Solution
# Author: Used Demo code, edited by Connie Uribe Chavez
# Date of latest revision: 01 Jun 2023
# Purpose: Signature-based Malware Detection Part 2 of 3
# Purpose: development of my own basic antivirus tool in Python.
# Reference: https://www.programiz.com/python-programming/examples/hash-file
##############################################################
# Alter your search code to recursively scan each file and folder in the user input directory path and print it to the screen.
# For each file scanned within the scope of your search directory:
# Generate the file’s MD5 hash using Hashlib.
# Assign the MD5 hash to a variable.
# Print the variable to the screen along with a timestamp, file name, file size, and complete (not symbolic) file path.
# TIP: You may need to bring in additional Python modules to complete today’s objective.

# "You get a directory from the user and your code will search for all files in that directory and any directories within the 
# user provided directory and print out all files found and returning the hashes of all of them"
#############################################################

fileList = []
hashList = [] 

def searchForFileInDir(dirName):
    for root, dirs, files in os.walk(dirName):
        for file in files:
            filePath = os.path.join(root, file)
            fileList.append(filePath)
            hashList.append(hash_file(filePath))

# The following Function was obtained from https://www.programiz.com/python-programming/examples/hash-file
def hash_file(filename):
   """"This function returns the MD5 hash
   of the file passed into it"""

   # make a hash object
   h = hashlib.sha256()

   # open file for reading in binary mode
   with open(filename,'rb') as file:

       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)

   # return the hex representation of digest
   return h.hexdigest()

def main():
    userDir = input("Type a directory to search in: ")
    searchForFileInDir(userDir)
    currenttime = datetime.now()
    if len(fileList) == 0:
        print("No files found.")
    else:
        for i in range(len(fileList)):
            file_stats = os.stat(fileList[i])
            # Print the variable to the screen along with a timestamp, file name, file size, and complete (not symbolic) file path.
            print(f"{currenttime}. \nThe file name is {os.path.basename(fileList[i])}, \nFile size in Bytes is {file_stats.st_size}, \nFile path is {fileList[i]} \nThe file MD5 hash is {hashList[i]}\n")

main()