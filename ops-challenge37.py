
#!/usr/bin/env python3
import requests
import webbrowser
# Script: Ops 401 Class 37 Ops Challenge Solution
# Author: ChatGPT and demo code edited by Connie Uribe Chavez
# Date of latest revision: 07 Jun 2023
# Purpose: Cookie Capture Capades



# targetsite = input("Enter target site:") # Uncomment this to accept user input target site
targetsite = "http://www.whatarecookies.com/cookietest.asp" # Comment this out if you're using the line above
response = requests.get(targetsite)
cookie = response.cookies



def cookiesFunc():
      # Send the cookie back to the site and receive a HTTP response
    response = requests.get(targetsite, cookies=cookie)

    # Generate a .html file to capture the contents of the HTTP response
    filename = "response.html"
    with open(filename, "w") as file:
        file.write(response.text)

    # Open the HTML file with Firefox
    firefox_path = "path_to_firefox_executable"  # Replace with the actual path to your Firefox executable
    webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path), 1)
    webbrowser.get('firefox').open(filename)

def bringforthcookiemonster(): # Because why not!
    print('''

              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.

        ''')

bringforthcookiemonster()
print("Target site is " + targetsite)
print(cookie)
cookiesFunc()

# Add here some code to make this script perform the following:
# - Send the cookie back to the site and receive a HTTP response
# - Generate a .html file to capture the contents of the HTTP response
# - Open it with Firefox
