#!/usr/bin/python3
import platform
import os
# Script: Ops 401 Class 31 Ops Challenge Solution
# Author: Connie Uribe Chavez
# Date of latest revision: 01 Jun 2023
# Purpose: Signature-based Malware Detection Part 1 of 3
# Purpose: development of my own basic antivirus tool in Python.
#reference: Sierra's demo
###############################################################
# Prompt the user to type in a file name to search for.
# Prompt the user for a directory to search in.
# Search each file in the directory by name.
# TIP: You may need to perform different commands depending on what OS you’re executing the script on.

# For each positive detection, print to the screen the file name and location.
# At the end of the search process, print to the screen how many files were searched and how many hits were found.
# The script must successfully execute on both Ubuntu Linux 20.04 Focal Fossa and Windows 10.
###############################################################


def searchForFileInDir(fileName, dirName):
    countFiles = 0
    filesFound = []
    for root, dirs, files in os.walk(dirName):
        for file in files:
            countFiles += 1
            if file == fileName:
                filesFound.append(os.path.join(root,file))
    print(f"There were {countFiles} files searched")
    return filesFound

def main():
    userDir = input("Type a directory to search in: ")
    userFile = input("Type a file name to search for: ") 
    list = searchForFileInDir(userFile, userDir)
    print("This operating system is: ", platform.system())
    print("The number of hits found: ", len(list))
    if len(list) == 0:
        print("No files found.")
    else:
        for file in list:
            print("File name: ", userFile)
            print("File location: ", file)
main()