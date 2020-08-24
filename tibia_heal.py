import json
import logging
import random
import os
import pyautogui
import pyscreenshot as ImageGrab
import sys
import tkinter as tk
from tkinter import *
from pynput.mouse import Listener as MouseListener
from pynput import mouse
from concur import Concur
from controller import Controller

configIndex = 0
P1 = 0
P2 = 0
firstTime = False
shouldListener = False

def checkConfigScreen():
	im=pyautogui.screenshot()
	im = im.crop((int(P1[0]), int(P1[1]), int(P2[0]), int(P2[1])))
	im.show()
	popupmsg('Please, confirm if the following points are valids\n P1' + str(P1) + ', P2' + str(P2))

def on_move(x, y):
	global firstTime
	if (firstTime == False):
		return False

def on_click(x, y, button, pressed):
	global shouldListener
	if pressed:
		if (button == mouse.Button.right and shouldListener):
			shouldListener = False
			checkConfigScreen()
			return False
		else:
			global configIndex, P1, P2
			if (configIndex == 0):
				P1 = [x, y]
				configIndex = 1
			elif (configIndex == 1):
				P2 = [x, y]
				configIndex = 0

with MouseListener(on_move=on_move, on_click=on_click) as listener:
	listener.join()

def popupmsg(msg):
	popup = tk.Tk()
	popup.wm_title("Warning")
	label = ttk.Label(popup, text=msg, font=("Verdana", 8))
	label.pack(side="top", fill="x", pady=10)
	B2 = ttk.Button(popup, text="Ok", command = popup.destroy)
	B2.pack()
	popup.mainloop()

def stopBot(concur, master):
	children_widgets = master.winfo_children()
	for child_widget in children_widgets:
		if child_widget.winfo_class() == 'Button':
			if (str(child_widget) == ".!button4"):
				child_widget.configure(bg="red")
			elif (str(child_widget) == ".!button3"):
				child_widget.configure(bg="green")
	master.title('TibiaBot - Stopped')
	concur.pause()

def loadConfig(a, b):
	print(a.get())
	print(b.get())
	
def startBot(concur, master):
	children_widgets = master.winfo_children()
	for child_widget in children_widgets:
		if child_widget.winfo_class() == 'Button':
			if (str(child_widget) == ".!button4"):
				child_widget.configure(bg="green")
			elif (str(child_widget) == ".!button3"):
				child_widget.configure(bg="red")
	valueTotalMana = concur.master["totalMana"].get()
	valueTotalLife = concur.master["totalLife"].get()
	
	if (valueTotalLife.isdigit() == False or valueTotalMana.isdigit() == False):
		popupmsg('Configure Total Life and Total Mana')
	else:
		concur.resume()
		master.title('TibiaBot - Running')

def checkIfLifeAndManaBarAreBeSeeing(master, controller, itemsFromScreen):
	children_widgets = master.winfo_children()
	valueLife = itemsFromScreen["totalLife"].get()
	valueMana = itemsFromScreen["totalMana"].get()
	im=pyautogui.screenshot()
	life = im
	mana = im
	list = controller.returnListPointsBar()
	life = life.crop((int(list[0]), int(list[1]), int(list[2]), int(list[3])))
	mana = mana.crop((int(list[4]), int(list[5]), int(list[6]), int(list[7])))
	vector_life = {}
	vector_mana = {}
		
	controller.identifyNumbers(life, mana, vector_life, vector_mana)
			
	validIndexLife = 0
	validIndexMana = 0
	lifeValue = ""
	manaValue = ""
	
	controller.changeGeneratorToList(vector_life, vector_mana)
	
	for i in range(0, 10):
		validIndexLife += (sum(x is not None for x in vector_life[i]))
		validIndexMana += (sum(x is not None for x in vector_mana[i]))

	lifeValue = controller.convertNumbersToString(validIndexLife, vector_life, lifeValue)
	manaValue = controller.convertNumbersToString(validIndexMana, vector_mana, manaValue)

	if (valueLife == "" or valueMana == ""):
		popupmsg('Set total life and total mana')
	if (validIndexLife != len(valueLife)):
		popupmsg('Length total life does not match with your length from life bar.\n'+
					'If your total life is right, please change your Life Bar points into config_screen.\n'+
					'Your life is ' + str(valueLife) + ' but the bot identify ' + str(lifeValue))
		return
	elif (validIndexMana != len(valueMana)):
		popupmsg('Length total mana does not match with your length from mana bar.\n'+
					'If your total mana is right, please change your Life Mana points into config_screen.\n'+
					'Your mana is ' + str(valueMana) + ' but the bot identify ' + str(manaValue))
		return
	else:
		for child_widget in children_widgets:
			if child_widget.winfo_class() == 'Button':
				if (str(child_widget) == ".!button2"):
					child_widget.configure(bg="green")
	master.title('Tibia Bot - Life: ' + str(lifeValue) + ' // Mana: ' + str(manaValue))


def configScreen():
	global shouldListener
	shouldListener = True
	listener.run()

def createSreen(concur, controller):
	fKeys = ('F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 
			'F9', 'F10', 'F11', 'F12', 'HOME', 'INSERT', 'DEL', ' ')
			
	tk.Label(master, 
			 text="Total Life").grid(row = 0)
	tk.Label(master, 
			 text="Total Mana").grid(row = 1)
	tk.Label(master, 
			 text="Time(s)").grid(row=5, column = 8)

	totalLife = tk.Entry(master, width=7)
	totalMana = tk.Entry(master, width=7)
	timeAutoSpell = tk.Entry(master, width=7)
	
	totalLife.grid(row=0, column=1)
	totalMana.grid(row=1, column=1)
	timeAutoSpell.grid(row=5, column = 9)

	autoUtamo = IntVar()
	Checkbutton(master, text="Auto Utamo Vita", variable=autoUtamo).grid(row=0, column = 6, sticky=W)

	autoUtitoTempo = IntVar()
	Checkbutton(master, text="Auto Utito Tempo", variable=autoUtitoTempo).grid(row=1, column = 6, sticky=W)

	autoAntiIdle = IntVar()
	Checkbutton(master, text="Anti Idle", variable=autoAntiIdle).grid(row=2, column = 6, sticky=W)

	eatFood = IntVar()
	Checkbutton(master, text="Eat Food", variable=eatFood).grid(row=3, column = 6, sticky=W)
	
	autoRun = IntVar()
	Checkbutton(master, text="Auto Run", variable=autoRun).grid(row=4, column = 6, sticky=W)

	autoSpell = IntVar()
	Checkbutton(master, text="Auto Spell", variable=autoSpell).grid(row=5, column = 6, sticky=W)

	textUtamoVita = StringVar()
	keyUtamoVita = ttk.Combobox(master, width = 6, textvariable = textUtamoVita)

	keyUtamoVita['values'] = fKeys
	  
	keyUtamoVita.grid(row = 0, column = 7, sticky=W) 
	keyUtamoVita.current()	

	textUtitoTempo = StringVar()
	keyUtitoTempo = ttk.Combobox(master, width = 6, textvariable = textUtitoTempo)

	keyUtitoTempo['values'] = fKeys
	  
	keyUtitoTempo.grid(row = 1, column = 7, sticky=W) 
	keyUtitoTempo.current()

	textHur = StringVar()
	keyPressRun = ttk.Combobox(master, width = 6, textvariable = textHur)

	keyPressRun['values'] = fKeys
	  
	keyPressRun.grid(row = 4, column = 7, sticky=W) 
	keyPressRun.current()	
	
	boxAutoSpell = StringVar()
	keyAutoSpell = ttk.Combobox(master, width = 6, textvariable = boxAutoSpell)
	
	keyAutoSpell['values'] = fKeys 
	  
	keyAutoSpell.grid(row = 5, column = 7, sticky=W) 
	keyAutoSpell.current() 

	keyPressFood = StringVar()
	keyChoosen = ttk.Combobox(master, width = 6, textvariable = keyPressFood)
	
	keyChoosen['values'] = fKeys
	  
	keyChoosen.grid(row = 3, column = 7, sticky=W) 
	keyChoosen.current()

	tk.Label(master, 
			text="Life 90%").grid(row = 3)
			
	keyPressCure90 = StringVar()
	keyChoosenCure90 = ttk.Combobox(master, width = 6, textvariable = keyPressCure90)
	
	keyChoosenCure90['values'] = fKeys
	  
	keyChoosenCure90.grid(row = 3, column = 1, sticky=W) 
	keyChoosenCure90.current()
	
	tk.Label(master, 
			text="Life 70%").grid(row = 4, column = 0)
			
	keyPressCure70 = StringVar()
	keyChoosenCure70 = ttk.Combobox(master, width = 6, textvariable = keyPressCure70) 

	keyChoosenCure70['values'] = fKeys
	  
	keyChoosenCure70.grid(row = 4, column = 1, sticky=W) 
	keyChoosenCure70.current()

	tk.Label(master, 
			text="Life 50%").grid(row = 5, column = 0)
			
	keyPressCure50 = StringVar()
	keyChoosenCure50 = ttk.Combobox(master, width = 6, textvariable = keyPressCure50) 

	keyChoosenCure50['values'] =  fKeys
	  
	keyChoosenCure50.grid(row = 5, column = 1, sticky=W) 
	keyChoosenCure50.current()
	
	tk.Label(master, 
		text="When Mana <").grid(row = 6, column = 0, sticky=W)
	
	manaPercent = tk.Entry(master, width=6)	
	manaPercent.grid(row=6, column=1, sticky=W)
	
	tk.Label(master, 
		text="% use").grid(row = 6, column = 2, sticky=W)	
	keyPressCureMana = StringVar()
	keyPressCureMana = ttk.Combobox(master, width = 6, textvariable = keyPressCureMana) 
	  
	keyPressCureMana['values'] =  fKeys
	  
	keyPressCureMana.grid(row = 6, column = 3) 
	keyPressCureMana.current()

	tk.Label(master, 
		text="When Mana >").grid(row = 7, column = 0, sticky=W)
	
	manaPercentForTrain = tk.Entry(master, width=6)	
	manaPercentForTrain.grid(row=7, column=1, sticky=W)
	
	tk.Label(master, 
		text="% use").grid(row = 7, column = 2, sticky=E)	
	keyPressTrainMana = StringVar()
	keyPressTrainMana = ttk.Combobox(master, width = 6, textvariable = keyPressTrainMana) 
	  
	keyPressTrainMana['values'] =  fKeys
	  
	keyPressTrainMana.grid(row = 7, column = 3) 
	keyPressTrainMana.current()


	tk.Label(master, 
		text="Auto SSA when Life <").grid(row = 6, column = 6, sticky=W)
	
	lifeToPullSSA = tk.Entry(master, width = 4)	
	lifeToPullSSA.grid(row = 6, column=7, sticky=W)
	
	tk.Label(master, 
		text="% use").grid(row = 6, column = 8, sticky=W)	
	keyToPullSSA = StringVar()
	keyToPullSSA = ttk.Combobox(master, width = 6, textvariable = keyToPullSSA) 
	  
	keyToPullSSA['values'] =  fKeys
	  
	keyToPullSSA.grid(row = 6, column = 9) 
	keyToPullSSA.current()
			
	itemsFromScreen = {
		"keyPressCure90": keyChoosenCure90,
		"keyPressCure70": keyChoosenCure70,
		"keyPressCure50": keyChoosenCure50,
		"manaPercent": manaPercent,
		"manaPercentForTrain": manaPercentForTrain, 
		"keyPressCureMana": keyPressCureMana,
		"keyPressTrainMana": keyPressTrainMana,
		"eatFood": eatFood,
		"keyPressFood": keyPressFood,
		"totalLife": totalLife,
		"totalMana": totalMana,
		"autoRun": autoRun,
		"spellHur": keyPressRun,
		"autoSpell": boxAutoSpell,
		"keyAutoSpell": keyAutoSpell,
		"timeAutoSpell": timeAutoSpell,
		"autoUtamo": autoUtamo,
		"keyUtamoVita": keyUtamoVita,
		"autoUtito": autoUtitoTempo,
		"keyUtito": keyUtitoTempo,
		"antiIdle": autoAntiIdle,
		"lifeToPullSSA": lifeToPullSSA,
		"keyToPullSSA": keyToPullSSA
	}

	concur.setMaster(itemsFromScreen)

	tk.Button(master, 
			  text='Config Screen',
			  activebackground='green',
			  command=lambda: configScreen()).grid(row=0, 
										column=4, 
										sticky=W, 
										pady=4)
	tk.Button(master, 
			  text='Check Config Screen',
			  bg='red',
			  command = lambda: checkIfLifeAndManaBarAreBeSeeing(master, controller, itemsFromScreen)).grid(row=0, 
										column=3, 
										sticky=E, 
										pady=4,
										padx=4)

	tk.Button(master, 
			  text='Stop', command = lambda: stopBot(concur, master)).grid(row=8, 
														   column=2, 
														   sticky=tk.W, 
														   pady=4)

	tk.Button(master, 
			  text='Start', command = lambda: startBot(concur, master)).grid(row=8, 
														   column=1, 
														   sticky=tk.W, 
														   pady=4)


if __name__ == '__main__':
	firstTime = True
	master = tk.Tk()
	master.geometry("750x300")
	master.resizable(False, False)
	master.title('TibiaBot - Stopped')

	concur = Concur(master)
	controller = Controller(master, concur)
	createSreen(concur, controller)
	concur.start()
	concur.pause()



	tk.mainloop()
	