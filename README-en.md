# TibiaBot12+
Bot for Tibia 12+. <br>
It doesn't work on TibiaGlobal, just in OTservers. <br>
It was tested with OtServers 12+. The OtServers allowed bots.<br>

## Features
- Auto Heal
- Auto Speed
- Auto Food
- Auto Utamo
- Auto Utito Tempo
- Anti Idle
- Auto SSA
- Auto Equip Ring (Might and Energy)
- Auto Sio (90%, 70% and 50%)

## Dependencies
- Python 3.7+
- PyAutoGUI
- Pyscreenshot
- Pynput
- OpenCv
## How to install?
- Downloading Python: https://www.python.org/downloads/release/python-372/
- After downloaded python, you're able to use "pip". Open terminal and use the follow commands:
    - Installing PyAutoGUI: ```pip install pyautogui```
    - Installing Pyscreenshot: ```pip3 install pyscreenshot```
    - Installing Pynput: ```pip install pynput```
    - Installing OpenCv: ```pip install opencv-python```
## How does it work?
 It uses PyAutoGUI to manage the mouse clicks and keys clicks, as the F keys (F1, F2, etc). Pyscreenshot allows to identify objects on screen, as Life Bar and Mana Bar. Pynput is used to trigger a listener to save our coordinates (x, y) from mouse when the user is settings objects location on your own screen.
## How to configure?
First of all, you need to configure your screen. For that, you need to set your coordinates from Life Bar, Mana Bar, Tools and Battle.<br>
Click on "Config Screen" in the bot. After the click, a listener will be started and will save your coordinates when clicked with the left button mouse.<br> 
![alt text](https://github.com/leoee/bot_for_tibia12.01/blob/master/images/bot.png)<br>
Click in 2 points to cut an image. When finished the clicks, click with right button and the listener will be stopped and an image will be showed. If the image is right, copy the coordinates from pop-up message and save into "config_screen.txt". There are some images examples below to help you in the cutting. I recommend you to cut with space after the value of life and mana. This because as you up level, the numbers that represents your life and mana will increase. If the image is not enought to see all the numbers, the bot won't work.<br>
![alt text](https://github.com/leoee/bot_for_tibia12.01/blob/master/images/lifeRD.png)<br>
![alt text](https://github.com/leoee/bot_for_tibia12.01/blob/master/images/manaRD.png)<br>
![alt text](https://github.com/leoee/bot_for_tibia12.01/blob/master/images/toolsRD.png)<br>
![alt text](https://github.com/leoee/bot_for_tibia12.01/blob/master/images/equipmentRD.png)<br>
![alt text](https://github.com/leoee/bot_for_tibia12.01/blob/master/images/battleRD.png)<br>
In the project, there is a txt file with the coordinates. The content file is the following:
```
***Life Bar*****
***Life Bar*****
x:"P1.x" - y:"P1.y"
x:"P2.x" - y:"P2.y"
***Mana Bar*****
x:"P1.x" - y:"P1.y"
x:"P2.x" - y:"P2.y"
***Tools*****
x:"P1.x" - y:"P1.y"
x:"P2.x" - y:"P2.y"
***Equipments*****
x:"P1.x" - y:"P1.y"
x:"P2.x" - y:"P2.y"
***Party List*****
x:"P1.x" - y:"P1.y"
x:"P2.x" - y:"P2.y"
```
Outro exemplo<br>
```
***Life Bar*****
x:"1193" - y:"138"
x:"1344" - y:"154"
***Mana Bar*****
x:"1193" - y:"148"
x:"1357" - y:"167"
***Tools*****
x:"1197" - y:"310"
x:"1313" - y:"327"
***Equipments*****
x:"1194" - y:"168"
x:"1307" - y:"324"
***Party List*****
x:"1190" - y:"400"
x:"1357" - y:"477"
```
That is the pattern, please don't change.<br>

After all of these steps, you can check your coordinates with the button "Check Config Screen". If is ok, the button will be painted with green color. I recommend you see the topic ***Warning*** below<br>

## How to use?
After the configuration, you can use. The way how this bot works is analyzing your screen, then the features will be work ***IF YOU KEEP ON GAME SCREEN***. You can change the screen, but the functionalities will be executed when the game screen be seeing.

- You must config your total life and mana with the length of your life/mana. Then, the bot will identify which
is your real life/mana. When you up your level, the values will be updated automatically.
- You can use "Insert" to start and stop the bot.
- You can use "Delete" to close the bot anytime.
- For Auto sio works, you need to open Party List and filter by the ***ONLY*** person who you want to cure. Fill all the life bar of this person and click on "Check Party List". In this moment, make sure the person life is 100% before use the button. After that, you the bot identify the life bar the button will be printed to green color and you're able to use this funcionality. Also make sure you added the location on the config_screen file.
- For functionalities that doesn't have any checkbox to active, you just need to choose a empty hotkey to deactivate the functionality.
- Auto SSA must have a hotkey that equip the amulet to work.
- Auto Equip Ring also must have a hotkey that equip the ring to work.
- In case Auto SSA and Auto Equip Ring are configured, by default Tibia doesn't allow to equip both on the same time, therefore the priority will be Auto SSA.


## Warning
If you're trying to use the bot, but always you get fail on the "Check Config Screen", you should try to cut the numbers of the your Tibia. As you can see, inside images folder, we have a lot of images that represents the numbers. Cut all of your numbers inside the tibia and try again. Just the numbers are needed.
