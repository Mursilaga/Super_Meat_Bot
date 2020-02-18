#!/usr/bin/python3

import signal
import keyboard
import time
from datetime import datetime
import os
import pyautogui
import time

#if not os.geteuid() == 0:
#  print("This script needs to be run as root.")
#  exit()


class MeatBot:
    def __init__(self):
        self.running = False
        self.time_stamp = datetime.now()

    def exitNice(self, signum, frame):
        self.running = False


    def keyEvent(self, e):
        print("Key " + e.event_type + ": " + str(e.name))
        now = datetime.now()
        print(now - self.time_stamp)
        self.time_stamp = now

        #if e.name == "q":
        #    exitNice("", "")
        #    print("Quitting")


    def run(self):
        self.time_stamp = datetime.now()
        self.running = True
        signal.signal(signal.SIGINT, self.exitNice)
        keyboard.hook(self.keyEvent)
        while self.running:
            time.sleep(1)


MeatBot().run()
