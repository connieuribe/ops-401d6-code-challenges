#!/usr/bin/python3
from zipfile import ZipFile
import logging
import logging.handlers as handlers
# Script: Ops 401 Class 28 Ops Challenge Solution
# Author: Connie Uribe Chavez
# Date of latest revision: 01 June 2023
# Purpose: Event Logging Tool Part 3 of 3
# Purpose: logging capabilities into one of your existing Python tools
# Reference: ChatGPT and Class Demo ops401d6: class28
################################################################
# Use StreamHandler and FileHandler in your Python script.
# FileHandler should write to a local file.
# StreamHandler should output to the terminal.
###############################################################

# Configure logger
logger = logging.getLogger('my_app')
logger.setLevel(logging.INFO)

# Configure FileHandler to write logs to a file
fileHandler = logging.FileHandler('app.log')
fileHandler.setLevel(logging.INFO)

# Configure StreamHandler to output logs to the terminal
streamHandler = logging.StreamHandler()
streamHandler.setLevel(logging.INFO)

# Add the handlers to the logger
logger.addHandler(fileHandler)
logger.addHandler(streamHandler)

# Define function to perform a brute force attack using a wordlist
def brute_force_zip(zip_file, wordlist):
    with open(wordlist, 'r', encoding='utf-8') as f:
        for line in f:
            password = line.strip()
            try:
                with ZipFile(zip_file) as zf:
                    zf.extractall(pwd=password.encode())
                    print(f"Password found: {password}")
                    logger.info(f"Password found: {password}")
                    return password
            except Exception as e:
                logger.error(f"Error occurred: {e}")
                pass

    print("Password not found")
    logger.warning("Password not found")
    return None

# Get user input for Zip file and wordlist path
zip_file = input("Enter the Zip file path: \n")
wordlist = input("Enter the path to the wordlist: ")

# Call the brute_force_zip function
brute_force_zip(zip_file, wordlist)