import pyautogui
import time
import threading
import keyboard  # Requires the 'keyboard' library, which can be installed using 'pip install keyboard'

# Configuration
click_interval = 0.1  # Interval between clicks, in seconds
button = 'left'  # The mouse button to click, can be 'left', 'right' or 'middle'
start_stop_key = 'f6'  # The key to start/stop the autoclicker
exit_key = 'f10'  # The key for exiting the script

# Variable to keep track of the clicker state
clicking = False

def clicker():
    while True:
        if clicking:
            pyautogui.click(button=button)
        time.sleep(click_interval)

def toggle_autoclicker():
    global clicking
    clicking = not clicking
    if clicking:
        print("Autoclicker started. Press F6 to stop.")
    else:
        print("Autoclicker stopped. Press F6 to start.")

def exit_autoclicker():
    print("Exiting autoclicker.")
    listener.stop()

# Setup hotkeys
keyboard.add_hotkey(start_stop_key, toggle_autoclicker)
keyboard.add_hotkey(exit_key, exit_autoclicker)

# Create and start the clicker thread
click_thread = threading.Thread(target=clicker)
click_thread.start()

print("Autoclicker running (press F6 to start/stop, F10 to exit).")
listener = keyboard.wait(exit_key)
