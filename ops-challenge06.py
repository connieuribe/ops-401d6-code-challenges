#!/usr/bin/env python3
from cryptography.fernet import Fernet
# Script: Ops 401 Class 06 Ops Challenge Solution
# Author: Marco Vazquez, edited by Connie Uribe Chavez
# Date of lates revision: 24 Apr 2023
# Purpose: File Encryption Script Part 1 of 3
# Reference: 
# -------------------------------

# Prompt the user to select a mode:
# Encrypt a file (mode 1)
# Decrypt a file (mode 2)
# Encrypt a message (mode 3)
# Decrypt a message (mode 4)
# If mode 1 or 2 are selected, prompt the user to provide a filepath to a target file.
# If mode 3 or 4 are selected, prompt the user to provide a cleartext string.
# Depending on the selection, perform one of the below functions. You’ll need to create four functions:

# Encrypt the target file if in mode 1.
# Delete the existing target file and replace it entirely with the encrypted version.
# Decrypt the target file if in mode 2.
# Delete the encrypted target file and replace it entirely with the decrypted version.
# Encrypt the string if in mode 3.
# Print the ciphertext to the screen.
# Decrypt the string if in mode 4.
# Print the cleartext to the screen.
###################################




#function to handle writing key
def write_key():
    #generate a key and save it into a file
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
            key_file.write(key)

def load_key():
    #load the key from the current file names key.key
    return open("key.key", "rb").read()

#main
#generate and write a new key
write_key()
#load the previously generate key
key = load_key()
#test
print("The key is " + str(key))