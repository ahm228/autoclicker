import pyautogui
import time
import threading
import keyboard

clickInterval = 0.00001 #Time, in seconds, between clicks
button = 'left' #Mouse button to click: can be set to left, right, and middle
startKey = 'f6' #Key to start/stop the autoclicker
exitKey = 'f10' #Key to exit the script

clicking = False #On/off state of autoclicker
exitFlag = False #Flag for script termination

def clicker():
    global exitFlag
    while not exitFlag:
        if clicking:
            pyautogui.click(button=button)
        time.sleep(clickInterval)

def toggleAutoclicker():
    global clicking
    clicking = not clicking #Toggle clicking
    if clicking:
        print("Autoclicker started. Press F6 to stop.")
    else:
        print("Autoclicker stopped. Press F6 to start.")

def exitAutoclicker():
    global clicking, exitFlag
    clicking = False #Stop clicking
    exitFlag = True #Set flag to terminate script
    print("Exiting autoclicker.")

#Sets keybindings for start/stop and exit
keyboard.add_hotkey(startKey, toggleAutoclicker)
keyboard.add_hotkey(exitKey, exitAutoclicker)

#Create and start clicker thread
clickThread = threading.Thread(target=clicker)
clickThread.start()

print("Autoclicker running (press F6 to start/stop, F10 to exit).")

#Run until exitFlag is thrown
while not exitFlag:
    time.sleep(0.1)

#ensure that clicker threat properly finishes before exiting
clickThread.join()
print("Script exited.")
