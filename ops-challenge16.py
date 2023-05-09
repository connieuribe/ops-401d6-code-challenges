# Import libraries
import time, getpass
# Script: Ops 401 Class 16 Ops Challenge Solution
# Author: Connie Uribe Chavez
# Date of latest revision: 08 May 2023
# Purpose: Automated Brute Force Wordlist Attack Tool Part 1 of 3
# Purpose: develop a custom tool that performs brute force attacks to better understand the types of automation employed by adversaries
# Reference: ChatGPT And CodeFellows 401d6 Class Demo

# Mode 1: Offensive; Dictionary Iterator
# Accepts a user input word list file path and iterates through the word list, assigning the word being read to a variable.
# Add a delay between words.
# Print to the screen the value of the variable.
# Declare functions
def iterator ():
    try:
        filepath = input("Enter your dictionary filepath:\n")
        file = open(filepath)
    except FileNotFoundError:
        print("Invalid file path.")
        return
    line = file.readline()
    while line:
        line = line.rstrip()
        word = line
        print(word)
        time.sleep(1)
        line = file.readline()
    file.close()


# Mode 2: Defensive; Password Recognized
# Accepts a user input string.
# Accepts a user input word list file path.
# Search the word list for the user input string.
# Print to the screen whether the string appeared in the word list.
def check_password():
    try:
        filepath = input("Enter your dictionary filepath:\n")
        file = open(filepath)
    except FileNotFoundError:
        print("\nInvalid file path.\n")
        return
    search_str = input("Enter the string to search for:\n")
    with file:
        for line in file:
            if search_str in line:
                print(f"\n{search_str} found in the dictionary -- You need a stronger password!\n")
                return True
    print(f"\n{search_str} not found in the dictionary.\n")
    file.close()
    return False

# Main
# prompts the user to select one of the following modes:
while True:
    mode = input("""
Brute Force Wordlist Attack Tool Menu
1 - Offensive, Dictionary Iterator
2 - Defensive, Password Recognized
3 - Exit
    Please enter a number: 
""")
    match mode:
        case "1":
            iterator()
        case "2":
            check_password()
        case "3":
            break
        case _:
            print("Invalid choice. Please try again.")


# Note: The RockYou passwords come bundled with Kali Linux, 
# but you can also download them separately at the above link. 
# Once downloaded, use the “tar -zxvf rockyou.txt.tar.gz” to open the file.