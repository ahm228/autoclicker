This script is a simple autoclicker written in Python. It allows the user to start and stop an autoclicker with a hotkey and exit the script with another hotkey.

## Dependencies
To run this script, you need to have the following Python libraries installed:
- `pyautogui`: Used for simulating mouse clicks.
- `keyboard`: For registering and handling hotkeys.

You can install these dependencies using pip:
    pip install pyautogui keyboard

## Features
- Start/stop the autoclicker with a hotkey (default F6).
- Exit the script with a different hotkey (default F10).

## Usage
1. Modify the `clickInterval`, `button`, `startKey`, and `exitKey` variables in the script to your preferences.
2. Run the script in a Python environment.
3. Press F6 to start the autoclicker and F6 again to stop it.
4. Press F10 to exit the script.

## Notes
- Be cautious with the click interval setting to avoid overwhelming your system.