import pyautogui
import time
import threading
import keyboard

click_interval = 0.00001  #Interval between clicks, in seconds
button = 'left'  #The mouse button to click, can be 'left', 'right' or 'middle'
start_stop_key = 'f6'  #The key to start/stop the script
exit_key = 'f10'  #The key for exiting the script

clicking = False

def clicker():
    while True:
        if clicking:
            pyautogui.click(button=button)
        time.sleep(click_interval)
        if not clicking and not threading.main_thread().is_alive():
            break

def toggle_autoclicker():
    global clicking
    clicking = not clicking
    if clicking:
        print("Autoclicker started. Press F6 to stop.")
    else:
        print("Autoclicker stopped. Press F6 to start.")

def exit_autoclicker():
    global clicking
    clicking = False
    print("Exiting autoclicker.")
    click_thread.join()  #Wait for the click_thread to finish
    exit()

keyboard.add_hotkey(start_stop_key, toggle_autoclicker)
keyboard.add_hotkey(exit_key, exit_autoclicker)

click_thread = threading.Thread(target=clicker)
click_thread.start()

try:
    print("Script running (press F6 to start/stop, F10 to exit).")
    keyboard.wait(exit_key)
except KeyboardInterrupt:
    print("Exiting script.")
    click_thread.join()  #Ensure that the clicker thread is properly terminated
    exit()
