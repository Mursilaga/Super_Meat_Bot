#!/usr/bin/python3

import signal
import keyboard
import time
import os
import pyautogui
import time

if not os.geteuid() == 0:
  print("This script needs to be run as root.")
  exit()


def exitNice(signum, frame):
  global running
  running = False


def keyEvent(e):
    global running
    # if e.event_type == "up":
    # print("Key up: " + str(e.name))
    # if e.event_type == "down":
    # print("Key down: " + str(e.name))
    if e.event_type == "down" and e.name == "a":
        routine1_2x()
    if e.name == "q":
        exitNice("", "")
        print("Quitting")


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


def routine1_1x():
    print('start routine1_1x')
    run_right(1)
    pyautogui.keyDown('space')
    pyautogui.keyDown('right')
    time.sleep(0.5)
    pyautogui.keyUp('space')
    pyautogui.keyUp('right')
    time.sleep(0.2)
    pyautogui.keyDown('left')
    time.sleep(0.3)
    pyautogui.keyDown('space')
    time.sleep(0.6)
    pyautogui.keyUp('left')
    pyautogui.keyUp('space')
    pyautogui.keyDown('right')
    time.sleep(0.6)
    pyautogui.keyUp('right')

def routine1_2x():
    print('start routine1_2x')
    pyautogui.keyDown('right')
    time.sleep(0.9)
    jump(0.21)  # jump over the first saw
    time.sleep(0.5)
    jump(0.25)  # jump on the wall
    pyautogui.keyUp('right')
    time.sleep(0.05)
    jump(0.5)
    time.sleep(0.2)
    jump(0.5)
    time.sleep(0.3)
    jump(0.5)
    time.sleep(0.3)



running = True
signal.signal(signal.SIGINT, exitNice)
keyboard.hook(keyEvent)

print("Press 'q' to quit")
fps = 1/24
while running:
  time.sleep(fps)
