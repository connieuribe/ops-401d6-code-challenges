from zipfile import ZipFile
# Script: Ops 401 Class 18 Ops Challenge Solution
# Author: ChatGPT edited, tested and completed by Connie Uribe Chavez
# Date of latest revision: 10 May 2023
# Purpose: Automated Brute Force Wordlist Attack Tool Part 3 of 3
# Purpose: develop a custom tool that performs brute force attacks.
# Reference: Used code from ChatGPT And CodeFellows 401d6 Class Demo class repo
# add a new mode to your Python brute force tool that allows you to brute force attack a password-locked zip file.

# Define function to perform a brute force attack using a wordlist
def brute_force_zip(zip_file, wordlist):
    with open(wordlist, 'r', encoding='utf-8') as f:
        for line in f:
            password = line.strip()
            try:
                with ZipFile(zip_file) as zf:
                    zf.extractall(pwd=password.encode())
                    print(f"Password found: {password}")
                    return password
            except:
                pass
    print("Password not found")
    return None

zip_file = input("Enter the Zip file path: \n")
wordlist  = input("Enter the path to the wordlist: ")
brute_force_zip(zip_file, wordlist)