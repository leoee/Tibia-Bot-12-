from tkinter import *
from tkinter import ttk
import tkinter as tk
import threading
import pyscreenshot as ImageGrab
from PIL import Image
import pyautogui
import time
from firebase import firebase
from datetime import datetime
import sys
import os
import json

class Concur(threading.Thread):
	def __init__(self):
		super(Concur, self).__init__()
		self.iterations = 0
		self.master = None
		self.daemon = True  # Allow main to exit even if still running.
		self.paused = True  # Start out paused.
		self.state = threading.Condition()

	def setMaster(self, master):
		self.master = master

	def run(self):
		self.resume()
		while True:
			with self.state:
				if self.paused:
					self.state.wait()  # Block execution until notified.
			controller(self)
			time.sleep(.1)
			self.iterations += 1

	def resume(self):
		with self.state:
			self.paused = False
			self.state.notify()  # Unblock self if waiting.

	def pause(self):
		with self.state:
			self.paused = True  # Block self.


def changeGeneratorToList(vector_life, vector_mana):
	for i in range(0, 10):
		vector_life[i] = list(vector_life[i])
		vector_mana[i] = list(vector_mana[i])

def configHeal(master, currentLife, currentMana):
	valueTotalMana = concur.master["totalMana"].get()
	valueTotalLife = concur.master["totalLife"].get()
	keyLife90 = concur.master["keyPressCure90"].get().lower()
	keyLife70 = concur.master["keyPressCure70"].get().lower()
	keyLife50 = concur.master["keyPressCure50"].get().lower()
	manaPercentForHeal = concur.master["manaPercent"].get()
	keyPressMana = concur.master["keyPressCureMana"].get().lower()
	
	if (valueTotalLife.isdigit() == False or valueTotalMana.isdigit() == False):
		return

	currentLifePercent = (float(currentLife/int(valueTotalLife)) * 100)
	currentManaPercent = (float(currentMana/int(valueTotalMana)) * 100)
		
	if (currentLifePercent <= 50 and keyLife50 != " "):
		pyautogui.press(keyLife50)
	elif (currentLifePercent <= 70 and keyLife70 != " "):
		pyautogui.press(keyLife70)
	elif (currentLifePercent <= 90 and keyLife90 != " "):
		pyautogui.press(keyLife90)
	
	if (manaPercentForHeal.isdigit() == False):
		return

	if (currentManaPercent <= int(manaPercentForHeal) and keyPressMana != " "):
		pyautogui.press(keyPressMana)

def confirmIsTarget(image):
	esq = pyautogui.locate('C:/Users/Leo/Desktop/heal_bot/images/esq.png', image, grayscale=True, confidence=.75)
	dir = pyautogui.locate('C:/Users/Leo/Desktop/heal_bot/images/dir.png', image, grayscale=True, confidence=.75)
	cima = pyautogui.locate('C:/Users/Leo/Desktop/heal_bot/images/cima.png', image, grayscale=True, confidence=.75)
	baixo = pyautogui.locate('C:/Users/Leo/Desktop/heal_bot/images/baixo.png', image, grayscale=True, confidence=.75)
	
	if (esq != None and dir != None and cima != None and baixo != None):
		return True

	return False


def controller(concur):
	time.sleep(1)
	while (True):
		if (concur.paused == True):
			break
		time.sleep(0.2)
		im=pyautogui.screenshot()
		life = im
		mana = im
		food = im
		isTarget = im
		life = life.crop((1200, 135, 1350, 155))
		mana = mana.crop((1200, 152, 1350, 174))
		food = food.crop((1190, 310, 1310, 330))
		isTarget = isTarget.crop((1170, 405, 1300, 482))
		
		screenBot = pyautogui.locate('C:/Users/Leo/Desktop/heal_bot/images/bot.png', im, grayscale=True, confidence=.75)
		
		if (screenBot != None):
			print('Skipping')
			continue
		
		vector_life = {}
		vector_mana = {}
		
		hasHungry = pyautogui.locate('C:/Users/Leo/Desktop/heal_bot/images/food.png', food, grayscale=True, confidence=.75)
		hasSpeed = pyautogui.locate('C:/Users/Leo/Desktop/heal_bot/images/speed.png', food, grayscale=True, confidence=.75)
		
		vector_life[0] =  pyautogui.locateAll('C:/Users/Leo/Desktop/heal_bot/images/0.png', life, grayscale=True, confidence=.95)
		vector_life[1] =  pyautogui.locateAll('C:/Users/Leo/Desktop/heal_bot/images/1.png', life, grayscale=True, confidence=.95)
		vector_life[2] =  pyautogui.locateAll('C:/Users/Leo/Desktop/heal_bot/images/2.png', life, grayscale=True, confidence=.95)
		vector_life[3] =  pyautogui.locateAll('C:/Users/Leo/Desktop/heal_bot/images/3.png', life, grayscale=True, confidence=.95)
		vector_life[4] =  pyautogui.locateAll('C:/Users/Leo/Desktop/heal_bot/images/4.png', life, grayscale=True, confidence=.95)
		vector_life[5] =  pyautogui.locateAll('C:/Users/Leo/Desktop/heal_bot/images/5.png', life, grayscale=True, confidence=.95)
		vector_life[6] =  pyautogui.locateAll('C:/Users/Leo/Desktop/heal_bot/images/6.png', life, grayscale=True, confidence=.95)
		vector_life[7] =  pyautogui.locateAll('C:/Users/Leo/Desktop/heal_bot/images/7.png', life, grayscale=True, confidence=.95)
		vector_life[8] =  pyautogui.locateAll('C:/Users/Leo/Desktop/heal_bot/images/8.png', life, grayscale=True, confidence=.95)
		vector_life[9] =  pyautogui.locateAll('C:/Users/Leo/Desktop/heal_bot/images/9.png', life, grayscale=True, confidence=.95)
		
		vector_mana[0] =  pyautogui.locateAll('C:/Users/Leo/Desktop/heal_bot/images/0.png', mana, grayscale=True, confidence=.95)
		vector_mana[1] =  pyautogui.locateAll('C:/Users/Leo/Desktop/heal_bot/images/1.png', mana, grayscale=True, confidence=.95)
		vector_mana[2] =  pyautogui.locateAll('C:/Users/Leo/Desktop/heal_bot/images/2.png', mana, grayscale=True, confidence=.95)
		vector_mana[3] =  pyautogui.locateAll('C:/Users/Leo/Desktop/heal_bot/images/3.png', mana, grayscale=True, confidence=.95)
		vector_mana[4] =  pyautogui.locateAll('C:/Users/Leo/Desktop/heal_bot/images/4.png', mana, grayscale=True, confidence=.95)
		vector_mana[5] =  pyautogui.locateAll('C:/Users/Leo/Desktop/heal_bot/images/5.png', mana, grayscale=True, confidence=.95)
		vector_mana[6] =  pyautogui.locateAll('C:/Users/Leo/Desktop/heal_bot/images/6.png', mana, grayscale=True, confidence=.95)
		vector_mana[7] =  pyautogui.locateAll('C:/Users/Leo/Desktop/heal_bot/images/7.png', mana, grayscale=True, confidence=.95)
		vector_mana[8] =  pyautogui.locateAll('C:/Users/Leo/Desktop/heal_bot/images/8.png', mana, grayscale=True, confidence=.95)
		vector_mana[9] =  pyautogui.locateAll('C:/Users/Leo/Desktop/heal_bot/images/9.png', mana, grayscale=True, confidence=.95)
		
		validIndexLife = 0
		validIndexMana = 0
		lifeValue = ""
		manaValue = ""
				
		changeGeneratorToList(vector_life, vector_mana)
		
		for i in range(0, 10):
			validIndexLife += (sum(x is not None for x in vector_life[i]))
			validIndexMana += (sum(x is not None for x in vector_mana[i]))
			
		if (validIndexLife == validIndexMana and validIndexMana == 0):
			continue;
		
		mustEatFood = concur.master["eatFood"].get()
		keyPressEatFood = concur.master["keyPressFood"].get().lower()
		mustUseHur = concur.master["autoRun"].get()
		spellHur = concur.master["spellHur"].get().lower()
		mustAtk = concur.master["autoSpellInTarget"].get()
		spellAtk = concur.master["keyAutoAtk"].get().lower()
				

		while(validIndexLife):
			max = 2000
			indexRemoved = 0
			insideIndexRemove = 0
			for value in vector_life:
				if (vector_life[value] != None):
					for valueIntoItem in vector_life[value]:
						if (max > valueIntoItem[0]):
							indexRemoved = value
							insideIndexRemove = valueIntoItem
							max = valueIntoItem[0]
			if (insideIndexRemove != 0):
				vector_life[indexRemoved].remove(insideIndexRemove)
			lifeValue += str(indexRemoved)
			validIndexLife -= 1
				
		while(validIndexMana):
			max = 2000
			indexRemoved = 0
			insideIndexRemove = 0
			for value in vector_mana:
				if (vector_mana[value] != None):
					for valueIntoItem in vector_mana[value]:
						if (max > valueIntoItem[0]):
							indexRemoved = value
							insideIndexRemove = valueIntoItem
							max = valueIntoItem[0]
			if (insideIndexRemove != 0):
				vector_mana[indexRemoved].remove(insideIndexRemove)
			manaValue += str(indexRemoved)
			validIndexMana -= 1
		
		#print(lifeValue + ' ---- ' + manaValue)
		#print(e1)
			
		if (hasHungry != None and mustEatFood):
			pyautogui.press(keyPressEatFood)
		if (hasSpeed == None and mustUseHur and spellHur != " "):
			pyautogui.press(spellHur)
		if (mustAtk and spellAtk != " " and confirmIsTarget(isTarget)):
			pyautogui.press(spellAtk)
			
		configHeal(master, int(lifeValue), int(manaValue))

def stopBot(concur, master):
	master.title('TibiaBot - Stopped')
	concur.pause()

def loadConfig(a, b):
	print(a.get())
	print(b.get())
	

def startBot(concur, master):
	master.title('TibiaBot - Running')
	concur.resume()
	
if __name__ == '__main__':
	master = tk.Tk()
	master.geometry("510x150")
	master.resizable(False, False)
	master.title('TibiaBot - Stopped')
		
	fKeys = ('F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 
				'F9', 'F10', 'F11', 'F12', 'HOME', 'INSERT', 'DEL', 'NONE')
			
	tk.Label(master, 
			 text="Total Life").grid(row = 0)
	tk.Label(master, 
			 text="Total Mana").grid(row = 1)
	tk.Label(master, 
			 text="Spell").grid(row = 0, column = 4)

	totalLife = tk.Entry(master, width=7)
	totalMana = tk.Entry(master, width=7)
	#autoHur = tk.Entry(master, width=18)
	
	totalLife.grid(row=0, column=1)
	totalMana.grid(row=1, column=1)
	#autoHur.grid(row=0, column=4, padx=5)

	keyPressHur = StringVar()
	keyPressRun = ttk.Combobox(master, width = 6, textvariable = keyPressHur) 
	  
	# Adding combobox drop down list 
	keyPressRun['values'] = fKeys
	  
	keyPressRun.grid(row = 0, column = 4) 
	keyPressRun.current()	

	eatFood = IntVar()
	Checkbutton(master, text="Eat Food", variable=eatFood).grid(row=1, column = 3, sticky=W)
	
	autoRun = IntVar()
	Checkbutton(master, text="Auto Run", variable=autoRun).grid(row=0, column = 3, sticky=W)
	
	autoTarget = IntVar()
	Checkbutton(master, text="Auto Target", variable=autoTarget).grid(row=0, column = 5, sticky=W)
	
	changeGold = IntVar()
	Checkbutton(master, text="Change Gold", variable=changeGold).grid(row=1, column = 5, sticky=W)
	
	keyAtk = StringVar()
	keyAutoAtk = ttk.Combobox(master, width = 4, textvariable = keyAtk) 
	  
	# Adding combobox drop down list 
	keyAutoAtk['values'] = fKeys 
	  
	keyAutoAtk.grid(row = 0, column = 5, sticky=W, padx = 95) 
	keyAutoAtk.current() 

	keyPressFood = StringVar()
	keyChoosen = ttk.Combobox(master, width = 4, textvariable = keyPressFood) 
	  
	# Adding combobox drop down list 
	keyChoosen['values'] = fKeys 
	  
	keyChoosen.grid(row = 1, column = 4, sticky=W) 
	keyChoosen.current(11) 	
					 
	tk.Label(master, 
			text="Life 90%").grid(row = 3)
			
	keyPressCure90 = StringVar()
	keyChoosenCure90 = ttk.Combobox(master, width = 6, textvariable = keyPressCure90) 
	  
	# Adding combobox drop down list 
	keyChoosenCure90['values'] = fKeys
	  
	keyChoosenCure90.grid(row = 3, column = 1, sticky=W) 
	keyChoosenCure90.current()
	
	tk.Label(master, 
			text="Life 70%").grid(row = 3, column = 3)
			
	keyPressCure70 = StringVar()
	keyChoosenCure70 = ttk.Combobox(master, width = 6, textvariable = keyPressCure70) 
	  
	# Adding combobox drop down list 
	keyChoosenCure70['values'] = fKeys
	  
	keyChoosenCure70.grid(row = 3, column = 4, sticky=W) 
	keyChoosenCure70.current()

	tk.Label(master, 
			text="Life 50%").grid(row = 3, column = 5, sticky=W)
			
	keyPressCure50 = StringVar()
	keyChoosenCure50 = ttk.Combobox(master, width = 6, textvariable = keyPressCure50) 
	  
	# Adding combobox drop down list 
	keyChoosenCure50['values'] =  fKeys
	  
	keyChoosenCure50.grid(row = 3, column = 5, sticky=W, padx = 60) 
	keyChoosenCure50.current()
	
	tk.Label(master, 
		text="When Mana <=").grid(row = 4, column = 0)
	
	manaPercent = tk.Entry(master, width=6)	
	manaPercent.grid(row=4, column=1)
	
	tk.Label(master, 
		text="% use").grid(row = 4, column = 2)	
	keyPressCureMana = StringVar()
	keyPressCureMana = ttk.Combobox(master, width = 6, textvariable = keyPressCureMana) 
	  
	# Adding combobox drop down list 
	keyPressCureMana['values'] =  fKeys
	  
	keyPressCureMana.grid(row = 4, column = 3) 
	keyPressCureMana.current()
			
	itemsFromScreen = {
		"keyPressCure90": keyChoosenCure90,
		"keyPressCure70": keyChoosenCure70,
		"keyPressCure50": keyChoosenCure50,
		"manaPercent": manaPercent,
		"keyPressCureMana": keyPressCureMana,
		"eatFood": eatFood,
		"keyPressFood": keyPressFood,
		"totalLife": totalLife,
		"totalMana": totalMana,
		"autoRun": autoRun,
		"spellHur": keyPressRun,
		"autoSpellInTarget": autoTarget,
		"keyAutoAtk": keyAutoAtk,
		"changeGold": changeGold
	}
	
	concur = Concur()
	concur.setMaster(itemsFromScreen)
	concur.start()
	concur.pause()

	tk.Button(master, 
			  text='Save Config', 
			  command=master.quit).grid(row=4, 
										column=5, 
										sticky=W, 
										pady=4)
	tk.Button(master, 
			  text='Load Config', 
			  command = lambda: loadConfig(eatFood, keyChoosen)).grid(row=4, 
										column=4, 
										sticky=E, 
										pady=4,
										padx=4)

	tk.Button(master, 
			  text='Stop', command = lambda: stopBot(concur, master)).grid(row=5, 
														   column=4, 
														   sticky=tk.W, 
														   pady=4)

	tk.Button(master, 
			  text='Start', command = lambda: startBot(concur, master)).grid(row=5, 
														   column=3, 
														   sticky=tk.W, 
														   pady=4)

	tk.mainloop()
	