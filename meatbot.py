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


def exitNice(signum, frame):
  global running
  running = False


def run_left(sec):
    pyautogui.keyDown('shift')
    pyautogui.keyDown('left')
    time.sleep(sec)
    pyautogui.keyUp('shift')
    pyautogui.keyUp('left')


def run_right(sec):
    pyautogui.keyDown('shift')
    pyautogui.keyDown('right')
    time.sleep(sec)
    pyautogui.keyUp('shift')
    pyautogui.keyUp('right')


def go_left(sec):
    pyautogui.keyDown('left')
    time.sleep(sec)
    pyautogui.keyUp('left')


def go_right(sec):
    pyautogui.keyDown('right')
    time.sleep(sec)
    pyautogui.keyUp('right')


def jump(sec):
    pyautogui.keyDown('space')
    time.sleep(sec)
    pyautogui.keyUp('space')

def keyEvent(e):
    global running
    global time_stamp
    print("Key " + e.event_type + ": " + str(e.name))
    now = datetime.now()
    print(now - time_stamp)
    time_stamp = now

    #if e.name == "q":
    #    exitNice("", "")
    #    print("Quitting")


time_stamp = datetime.now()
running = True
signal.signal(signal.SIGINT, exitNice)
keyboard.hook(keyEvent)


while running:
    time.sleep(1)
