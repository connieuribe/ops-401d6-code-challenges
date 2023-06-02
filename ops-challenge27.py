#!/usr/bin/python3
from zipfile import ZipFile
import logging
import logging.handlers as handlers
# Script: Ops 401 Class 27 Ops Challenge Solution
# Author: Connie Uribe Chavez
# Date of latest revision: 23 May 2023
# Purpose: Event Logging Tool Part 2 of 3
# Purpose: logging capabilities into one of your existing Python tools
# Reference: https://github.com/codefellows/seattle-ops-401d6/blob/main/class-27/challenges/DEMO.md
######################################################
# On the Python tool you added logging capabilities to:
# Add a log rotation feature based on size
######################################################

# Configure logger
logger = logging.getLogger('my_app')
logger.setLevel(logging.INFO)

# Configure log rotation
logHandler = handlers.RotatingFileHandler('app.log', maxBytes=500, backupCount=2)
logHandler.setLevel(logging.INFO)
logger.addHandler(logHandler)

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
wordlist  = input("Enter the path to the wordlist: ")

# Call the brute_force_zip function
brute_force_zip(zip_file, wordlist)
