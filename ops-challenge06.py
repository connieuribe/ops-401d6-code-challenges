#!/usr/bin/env python3
from cryptography.fernet import Fernet
import os
# Script: Ops 401 Class 06 Ops Challenge Solution
# Author: Connie Uribe Chavez
# Date of lates revision: 26 Apr 2023
# Purpose: File Encryption Script Part 1 of 3
# Reference: https://towardsdatascience.com/encrypt-and-decrypt-files-using-python-python-programming-pyshark-a67774bbf9f4
# Reference: https://www.geeksforgeeks.org/encrypt-and-decrypt-files-using-python/
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
    
# Prompt the user to select a mode:
def userSelection():
    mode = input("Select a mode:\
           \n   [1] Encrypt a file\
           \n   [2] Decrypt a file\
           \n   [3] Encrypt a message\
           \n   [4] Decrypt a message\n")
    match mode:
        case "1":
            # Encrypt a file
            filePath = input("Enter the path of a file: ")
            # opening the original file to encrypt
            with open(filePath, 'rb') as file:
                content = file.read()
            encrypted = encrypt(content)
            # opening the file in write mode and
            # writing the encrypted data
            with open(filePath, 'wb') as encrypted_file:
                encrypted_file.write(encrypted)
        case "2":
            #Decrypt a file
            filePath = input("Enter the path of a file: ")
            # opening the encrypted file
            with open(filePath, 'rb') as enc_file:
                content = enc_file.read()
            decrypted = decrypt(content)
            # opening the file in write mode and
            # writing the decrypted data
            with open(filePath, 'wb') as dec_file:
                dec_file.write(decrypted)
        case "3":
            #Encrypt a message
            msg = input("Enter a message: ")
            encrypted = encrypt(msg.encode())
            print("The encrypted message is " + str(encrypted))
        case "4":
            #Decrypt a message
            msg = input("Enter a message: ")
            decrypted = decrypt(msg.encode('utf-8'))
            print("the decrypted message " + str(decrypted.decode('utf-8')))
        case _:
            print("Invalid input")


key = generateKey()# generate and write a new key
while True:
    userSelection() # Run the user GUI