import pyautogui
import time
import threading
import keyboard

clickInterval = 0.00001
button = 'left'
startKey = 'f6'
exitKey = 'f10'

clicking = False
exitFlag = False

def clicker():
    global exitFlag
    while not exitFlag:
        if clicking:
            pyautogui.click(button=button)
        time.sleep(clickInterval)

def toggleAutoclicker():
    global clicking
    clicking = not clicking
    if clicking:
        print("Autoclicker started. Press F6 to stop.")
    else:
        print("Autoclicker stopped. Press F6 to start.")

def exitAutoclicker():
    global clicking, exitFlag
    clicking = False
    exitFlag = True
    print("Exiting autoclicker.")

keyboard.add_hotkey(startKey, toggleAutoclicker)
keyboard.add_hotkey(exitKey, exitAutoclicker)

clickThread = threading.Thread(target=clicker)
clickThread.start()

print("Autoclicker running (press F6 to start/stop, F10 to exit).")

while not exitFlag:
    time.sleep(0.1)

clickThread.join()
print("Script exited.")
