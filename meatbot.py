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


class Action:
    def __init__(self, action_type, action_value):
        self.type = action_type
        self.value = action_value


class MeatBot:
    def __init__(self):
        self.running = False
        self.time_stamp = datetime.now()
        self.routine = []

    def exitNice(self, signum, frame):
        self.running = False

    def keyEvent(self, e):
        if e.name == "f1":
            if e.event_type == "down":
                self.runRoutine()
            return

        if e.name == "f2":
            if e.event_type == "down":
                print("routine clear")
                self.routine.clear()
            return

        if e.name == "f3":
            if e.event_type == "down":
                print("print routine")
                for a in self.routine:
                    print(a.type + " : " + a.value)
            return

        now = datetime.now()
        seconds = (now - self.time_stamp).total_seconds()
        self.routine.append(Action('wait', str(seconds)))
        print(seconds)
        self.time_stamp = now
        self.routine.append(Action(e.event_type, str(e.name)))
        print(e.event_type + ": " + str(e.name))





        # if e.name == "q":
        #     exitNice("", "")
        #     print("Quitting")

    def runRoutine(self):
        print("runRoutine")
        for act in self.routine:
            print("bot " + act.type + ":" + act.value)
            if act.type == 'wait':
                time.sleep(float(act.value))
            elif act.type == 'down':
                pyautogui.keyDown(act.value)
            elif act.type == 'up':
                pyautogui.keyUp(act.value)



    def run(self):
        self.time_stamp = datetime.now()
        self.running = True
        signal.signal(signal.SIGINT, self.exitNice)
        keyboard.hook(self.keyEvent)
        while self.running:
            time.sleep(1)


MeatBot().run()
