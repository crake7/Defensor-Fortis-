## BACKDOOR 

Contains two files: a Listener and a Backdoor file. 
You will need to run the `listener.py` to run a bind shell and  `reverse_backdoor.py` file will create a reverse
connection so the target computer will connect back to the hacker using port 4444.

First, let's have a look at how the Listener.py file works:

1. Input your **IP address** and the **PORT** number you will use to connect to the victim computer. 
Currently, the backdoor file is using port 4444. Remember to use a port that is not being used by your system, otherwise it will not work.

2. This program allows the following features:
3. 
-Downloading files (Uses serialization converting files into JSON objects.) Type in: `download ___`
-Uploading files (Uses serialization converting files into JSON objects.) Type in: `upload _____`
-Navegate throught the file system. Type in: `cd ____` #Do not use relative paths. 

3. When you want to close the connection, simply type in the terminal:
"exit" 


Now, to set up the reverse_backdoor.py program:

1. You need to input your system's <IP> and the <PORT> number you wish to use. Currently, it is setup to listen on port 4444.

2. This program has been set up to provide persistence, this means that the program will start whenever the system starts. Should you decide
to modify the location of this setting, use "cat reverse_backdoor.py" to inspect it. 
