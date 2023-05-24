#!/usr/bin/python3
# Script: Ops 401 Class 27 Ops Challenge Solution
# Author: ChatGPT edited, tested and completed by Connie Uribe Chavez
# Date of latest revision: 23 May 2023
# Purpose: Event Logging Tool Part 2 of 3
# Purpose: logging capabilities into one of your existing Python tools

# On the Python tool you added logging capabilities to:

# Add a log rotation feature based on size





# Create and configure logger
logging.basicConfig(filename="newfile.log",
     format='%(asctime)s %(message)s',
     filemode='w')
# Creating an object
logger = logging.getLogger()



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



zip_file = input("Enter the Zip file path: \n")
wordlist  = input("Enter the path to the wordlist: ")
brute_force_zip(zip_file, wordlist)



# Test messages
# logger.debug("Harmless debug Message")
# logger.info("Just an information")
# logger.warning("Its a Warning")
# logger.error("Did you try to divide by zero")
# logger.critical("Internet is down")