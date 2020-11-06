#!/usr/bin/env python
import requests

def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass
    except requests.exceptions.InvalidURL:
        pass

target = "10.0.2.7/mutillidae/"

#Find SUBDOMAINS
with open("/root/Downloads/Wordlists/subdomains-wordlist.txt", "r") as subdomain_wordlist:
    for line in subdomain_wordlist:
        word = line.strip()
        path = word + "." + target
#         # print(path)
        response = request(path)
        if response:
#             # print(response)
            print("Discovered subdomain: " + str(path))

#Find DIRECTORIES AND FILES
with open("/root/Downloads/Wordlists/files-and-dirs-wordlist.txt", "r") as dir_wordlist:
    for line in dir_wordlist:
        word = line.strip()
        path = target + "/" + word
        response = request(path)
        if response:
            print("Discovered directory/folder: " + str(path))

