#!/usr/bin/env python3
from cryptography.fernet import Fernet
import os
# Script: Ops 401 Class 07 Ops Challenge Solution
# Author: Connie Uribe Chavez
# Date of lates revision: 26 Apr 2023
# Purpose: File Encryption Script Part 2 of 3
# Reference: 
# ------------------------------- 

# Add a feature capability to your script to:
# for each file in the files list, encrypt the data.
# Recursively encrypt a single folder and all its contents.
startDir = "/temp"
for root, dirs, files in os.walk(startDir):
    for fileName in files:
        print("File name: " + fileName)
        # Encrypt files
    for dirName in dirs:
        print("Directory name: " + dirName)


# Recursively decrypt a single folder that was encrypted by this tool.