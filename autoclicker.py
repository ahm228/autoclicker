import pyautogui
import time
import threading
import keyboard

clickInterval = 0.00001
button = 'left'
start_stop_key = 'f6'
exit_key = 'f10'

clicking = False
exit_flag = False

def clicker():
    global exit_flag
    while not exit_flag:
        if clicking:
            pyautogui.click(button=button)
        time.sleep(clickInterval)

def toggle_autoclicker():
    global clicking
    clicking = not clicking
    if clicking:
        print("Autoclicker started. Press F6 to stop.")
    else:
        print("Autoclicker stopped. Press F6 to start.")

def exit_autoclicker():
    global clicking, exit_flag
    clicking = False
    exit_flag = True
    print("Exiting autoclicker.")

keyboard.add_hotkey(start_stop_key, toggle_autoclicker)
keyboard.add_hotkey(exit_key, exit_autoclicker)

click_thread = threading.Thread(target=clicker)
click_thread.start()

print("Autoclicker running (press F6 to start/stop, F10 to exit).")

while not exit_flag:
    time.sleep(0.1)

click_thread.join()
print("Script exited.")
