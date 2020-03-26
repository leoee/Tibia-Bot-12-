# TibiaBot12+
Bot for Tibia 12+. <br>
It doesn't work on TibiaGlobal, just in OTservers. <br>
It was tested on TaleonAres. <br>

## Features
- Auto Heal
- Auto Speed
- Auto Food

## Dependencies
- Python 3.7+
- PyAutoGUI
- Pyscreenshot
- Pynput
## How to use?
- To install PyAutoGUI: ```pip install pyautogui```
- To install Pyscreenshot: ```pip3 install pyscreenshot```
- To install Pynput: ```pip install pynput```
## How does it work?
 It uses PyAutoGUI to manage the mouse clicks and keys clicks, as the F keys (F1, F2, etc). Pyscreenshot allows to identify objects on screen, as Life Bar and Mana Bar. Pynput is used to trigger a listener to save our coordinates (x, y) from mouse when the user is settings objects location on your own screen.
