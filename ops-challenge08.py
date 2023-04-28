#!/usr/bin/env python3
from cryptography.fernet import Fernet
import subprocess
import pyautogui
import time
# Script: Ops 401 Class 08 Ops Challenge Solution
# Author: Connie Uribe Chavez
# Date of lates revision: 27 Apr 2023
# Purpose: File Encryption Script Part 3 of 3
# Reference: Create a Ransomware simulation to a Linux OS.
# Reference: ChatGPT
# Reference: https://software.codidact.com/posts/287782/287783
# ------------------------------- 
#################################################################
###### THIS CODE SHOULD BE RAN IN A LINUX ENVIRONMENT ###########
#################################################################
# Add a feature capability to your Python encryption tool to:
# Alter the desktop wallpaper on a Linux PC with a ransomware message
result = subprocess.run(['gsettings', 'get', 'org.gnome.desktop.background', 'picture-uri'], capture_output=True)
def changeBackground():
    wallpaper_path = 'https://www.secpod.com/blog/wp-content/uploads/2017/05/Screenshot-from-2017-05-14-23-42-20.png'
    subprocess.run(['gsettings', 'set', 'org.gnome.desktop.background', 'picture-uri', f'{wallpaper_path}'])

# Create a popup window on a Linux PC with a ransomware message
def pop_up():
    pyautogui.alert('Got you!!! ')
    # Press the "Enter" key to dismiss the popup window
    pyautogui.press('enter')

# restore background
def restore_background():
    original_wallpaper_path = result.stdout.decode().strip()[8:-1]
    subprocess.run(['gsettings', 'set', 'org.gnome.desktop.background', 'picture-uri', original_wallpaper_path])

# Make this feature optional. 
# ransomeware: In the user menu prompt, add this as a ransomware simulation option.
while True:
    strInput = input("Select \
                     \n (1) Ransomware simulation: change background with a ransomware message \
                     \n (2) Ransomware simulation: popup window with a ransomware message \
                     \n (3) Restore background")
    if (strInput == "1"):
        changeBackground()
    elif (strInput == "2"):
        pop_up()
    elif (strInput == "3"):
        restore_background()
    else:
        print("Invalid input, try again . . . ")     