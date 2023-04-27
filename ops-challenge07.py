#!/usr/bin/env python3
from cryptography.fernet import Fernet
import os
# Script: Ops 401 Class 07 Ops Challenge Solution
# Author: Connie Uribe Chavez
# Date of lates revision: 26 Apr 2023
# Purpose: File Encryption Script Part 2 of 3
# Reference: 
# ------------------------------- 


# function to handle generating key
def generateKey():
    key = Fernet.generate_key() # generate a key and save it into a file
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    return open("key.key", "rb").read() # load the key from the current file names key.key
  
# Encrypt the target 
def encrypt(target):
    # initialize the fernet class
    encryption = Fernet(key)
    # actually do the encryption
    return encryption.encrypt(target)
    
# Decrypt the target
def decrypt(target):
    # initialized the fernet class
    decryption = Fernet(key)
    # decrypt the data
    return decryption.decrypt(target)
    
key = generateKey()# generate and write a new key
startDir = "/home/connieuribe/CodeFellows/TestFile"

# Add a feature capability to your script to:
# for each file in the files list, encrypt the data.
# Recursively encrypt a single folder and all its contents.
def encryptRecur():
    for dirs, files in os.walk(startDir):
        for fileName in files:
            with open(fileName, 'rb') as file:
                original = file.read()
            encrypted = encrypt(original)
            with open(fileName, 'wb') as encrypted_file:
                encrypted_file.write(encrypted)
        for dirName in dirs:
            print("Directory name: " + dirName)


# Recursively decrypt a single folder that was encrypted by this tool.
def decryptRecur():
    for dirs, files in os.walk(startDir):
        for fileName in files:
            with open(fileName, 'rb') as enc_file:
                content = enc_file.read()
            decryptedFile = decrypt(content)
            with open(fileName, 'wb') as dec_file:
                dec_file.write(decryptedFile)
        for dirName in dirs:
            print("Directory name: " + dirName)