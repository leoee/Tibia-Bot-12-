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
## How to install?
- To install PyAutoGUI: ```pip install pyautogui```
- To install Pyscreenshot: ```pip3 install pyscreenshot```
- To install Pynput: ```pip install pynput```
## How does it work?
 It uses PyAutoGUI to manage the mouse clicks and keys clicks, as the F keys (F1, F2, etc). Pyscreenshot allows to identify objects on screen, as Life Bar and Mana Bar. Pynput is used to trigger a listener to save our coordinates (x, y) from mouse when the user is settings objects location on your own screen.
## How to configure?
First of all, you need to configure your screen. For that, you need to set your coordinates from Life Bar, Mana Bar, Tools and Battle.<br>
Click on "Config Screen" in the bot. After the click, a listener will be started and will save your coordinates when clicked with the left button mouse.<br> 
![alt text](https://github.com/leoee/bot_for_tibia12.01/blob/master/images/botRD.png)
Click in 2 points to cut an image. When finished the clicks, click with right button and the listener will be stopped and an image will be showed o your. If the image is right, copy the coordinates from pop-up message and save into "config_screen.txt". There are some images examples below to help you in the cutting.<br>
![alt text](https://github.com/leoee/bot_for_tibia12.01/blob/master/images/lifeRD.png)<br>
![alt text](https://github.com/leoee/bot_for_tibia12.01/blob/master/images/manaRD.png)<br>
![alt text](https://github.com/leoee/bot_for_tibia12.01/blob/master/images/toolsRD.png)<br>
![alt text](https://github.com/leoee/bot_for_tibia12.01/blob/master/images/battleRD.png)<br>
In the project, there is a txt file with the coordinates. The content file is the following:
```
***Life Bar*****
x:"P1.x" - y:"P1.y"
x:"P2.x" - y:"P2.y"
***Mana Bar*****
x:"P1.x" - y:"P1.y"
x:"P2.x" - y:"P2.y"
***Tools*****
x:"P1.x" - y:"P1.y"
x:"P2.x" - y:"P2.y"
***Battle*****
x:"P1.x" - y:"P1.y"
x:"P2.x" - y:"P2.y"
```
That is the pattern, please don't change.<br>

After all of these steps, you can check your coordinates with the button "Check Config Screen". If is ok, the button will be painted with green color.<br>

## How to use?
After the configuration, you can use. The way how this bot works is analyzing your screen, then the features will be work ***IF YOU KEEP ON GAME SCREEN***. You can change the screen, but the functionalities will be executed when the game screen be seeing.
