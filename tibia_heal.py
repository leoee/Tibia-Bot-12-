import json
import logging
import random
import os
import pyautogui
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

def check_config_screen():
	im=pyautogui.screenshot()
	im = im.crop((int(P1[0]), int(P1[1]), int(P2[0]), int(P2[1])))
	im.show()
	create_popup_message('Please, confirm if the following points are valids\n P1' + str(P1) + ', P2' + str(P2))

def on_move(x, y):
	global firstTime
	if (firstTime == False):
		return False

def on_click(x, y, button, pressed):
	global shouldListener
	if pressed:
		if (button == mouse.Button.right and shouldListener):
			shouldListener = False
			check_config_screen()
			return False
		else:
			global configIndex, P1, P2
			if (configIndex == 0):
				P1 = [x, y]
				configIndex = 1
			elif (configIndex == 1):
				P2 = [x, y]
				configIndex = 0

with MouseListener(on_move=on_move, on_click=on_click) as mouseListener:
	mouseListener.join()

def create_popup_message(msg):
	popup = tk.Tk()
	popup.wm_title("Warning")
	label = ttk.Label(popup, text=msg, font=("Verdana", 8))
	label.pack(side="top", fill="x", pady=10)
	B2 = ttk.Button(popup, text="Ok", command = popup.destroy)
	B2.pack()
	popup.mainloop()

def stop_bot(concur, master):
	concur.keyListener.botIsRunning = False
	children_widgets = master.winfo_children()
	for child_widget in children_widgets:
		if child_widget.winfo_class() == 'Button':
			if (str(child_widget) == ".!button5"):
				child_widget.configure(bg="red")
			elif (str(child_widget) == ".!button4"):
				child_widget.configure(bg="green")
	master.title('TibiaBot - Stopped')
	concur.pause()

def loadConfig(a, b):
	print(a.get())
	print(b.get())
	
def start_bot(concur, master):
	concur.keyListener.botIsRunning = True
	children_widgets = master.winfo_children()
	for child_widget in children_widgets:
		if child_widget.winfo_class() == 'Button':
			if (str(child_widget) == ".!button5"):
				child_widget.configure(bg="green")
			elif (str(child_widget) == ".!button4"):
				child_widget.configure(bg="red")
	valueTotalMana = concur.master["totalMana"].get()
	valueTotalLife = concur.master["totalLife"].get()
	
	if (valueTotalLife.isdigit() == False or valueTotalMana.isdigit() == False):
		create_popup_message('Configure Total Life and Total Mana')
	else:
		concur.resume()
		master.title('TibiaBot - Running')

def validate_bars_of_screen(master, controller, itemsFromScreen):
	children_widgets = master.winfo_children()
	valueLife = itemsFromScreen["totalLife"].get()
	valueMana = itemsFromScreen["totalMana"].get()
	im=pyautogui.screenshot()
	life = im
	mana = im
	list = controller.get_list_of_points_bar()
	life = life.crop((int(list[0]), int(list[1]), int(list[2]), int(list[3])))
	mana = mana.crop((int(list[4]), int(list[5]), int(list[6]), int(list[7])))
	vector_life = {}
	vector_mana = {}
		
	controller.identify_numbers_on_image(life, mana, vector_life, vector_mana)
			
	validIndexLife = 0
	validIndexMana = 0
	lifeValue = ""
	manaValue = ""
	
	controller.change_generator_to_list(vector_life, vector_mana)
	
	for i in range(0, 10):
		validIndexLife += (sum(x is not None for x in vector_life[i]))
		validIndexMana += (sum(x is not None for x in vector_mana[i]))

	lifeValue = controller.convert_numbers_to_string(validIndexLife, vector_life, lifeValue)
	manaValue = controller.convert_numbers_to_string(validIndexMana, vector_mana, manaValue)

	if (valueLife == "" or valueMana == ""):
		create_popup_message('Set total life and total mana')
	if (validIndexLife != len(valueLife)):
		create_popup_message('Length total life does not match with your length from life bar.\n'+
					'If your total life is right, please change your Life Bar points into config_screen.\n'+
					'Your life is ' + str(valueLife) + ' but the bot identify ' + str(lifeValue))
		return
	elif (validIndexMana != len(valueMana)):
		create_popup_message('Length total mana does not match with your length from mana bar.\n'+
					'If your total mana is right, please change your Life Mana points into config_screen.\n'+
					'Your mana is ' + str(valueMana) + ' but the bot identify ' + str(manaValue))
		return
	else:
		for child_widget in children_widgets:
			if child_widget.winfo_class() == 'Button':
				if (str(child_widget) == ".!button3"):
					child_widget.configure(bg="green")
	master.title('Tibia Bot - Life: ' + str(lifeValue) + ' // Mana: ' + str(manaValue))


def config_screen():
	global shouldListener
	if (shouldListener):
		return
	shouldListener = True
	mouseListener.run()

def create_screen(concur, controller):
	fKeys = ('F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 
			'F9', 'F10', 'F11', 'F12', '1', '2', '3', '4'
				, '5', '6', '7', '8', '9', '0', ' ')
			
	tk.Label(master, 
			 text="Total Life").grid(row = 0)
	tk.Label(master, 
			 text="Total Mana").grid(row = 1)
	tk.Label(master, 
			 text="Time(s)").grid(row=5, column = 8)
	tk.Label(master, 
			 text="Life sio(%)").grid(row=8, column = 7)
	tk.Label(master, 
			 text="Auto Ring when").grid(row=7, column = 6)


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
	keyToPullSSA = ttk.Combobox(master, width = 3, textvariable = keyToPullSSA) 
	  
	keyToPullSSA['values'] =  fKeys
	  
	keyToPullSSA.grid(row = 6, column = 9) 
	keyToPullSSA.current()

	bar_to_pull_ring = StringVar()
	bar_to_pull_ring = ttk.Combobox(master, width = 6, textvariable = bar_to_pull_ring) 
	  
	bar_to_pull_ring['values'] =  ('MANA', 'LIFE')
	  
	bar_to_pull_ring.grid(row = 7, column = 7) 
	bar_to_pull_ring.current()

	value_to_pull_ring = tk.Entry(master, width = 4)	
	value_to_pull_ring.grid(row = 7, column=8)

	tk.Label(master, 
		text="% use").grid(row = 7, column = 9)

	key_auto_ring = StringVar()
	key_auto_ring = ttk.Combobox(master, width = 3, textvariable = key_auto_ring)

	key_auto_ring['values'] = fKeys
	  
	key_auto_ring.grid(row = 7, column = 10, sticky=W) 
	key_auto_ring.current()

	tk.Label(master, 
		text="Ring").grid(row = 7, column = 11, sticky=W)

	ring_type = StringVar()
	ring_type = ttk.Combobox(master, width = 5, textvariable = ring_type)

	ring_type['values'] = ('Might', 'Energy')
	  
	ring_type.grid(row = 7, column = 12, sticky=W) 
	ring_type.current()

	text_life_sio = StringVar()
	life_to_sio = ttk.Combobox(master, width = 4, textvariable = text_life_sio)

	life_to_sio['values'] = ('90%', '70%', '50%', ' ')
	  
	life_to_sio.grid(row = 8, column = 8, sticky=E) 
	life_to_sio.current()	

	tk.Label(master, 
		text="use").grid(row = 8, column = 9)

	text_life_sio = StringVar()
	key_sio = ttk.Combobox(master, width = 3, textvariable = text_life_sio)

	key_sio['values'] = fKeys
	  
	key_sio.grid(row = 8, column = 10, sticky=W) 
	key_sio.current()	
			
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
		"keyToPullSSA": keyToPullSSA,
		"lifeToUseSio": life_to_sio,
		"keyForSio": key_sio,
		"barToPullRing": bar_to_pull_ring,
		"valueToPullRing": value_to_pull_ring,
		"keyToPullRing": key_auto_ring,
		"ringType": ring_type	
	}

	concur.setMaster(itemsFromScreen)

	tk.Button(master, 
			  text='Check Party List',
			  activebackground='green',
			  command=lambda: controller.check_sio_bar()).grid(row=8, 
										column=6, 
										sticky=W, 
										pady=4)

	tk.Button(master, 
			  text='Config Screen',
			  activebackground='green',
			  command=lambda: config_screen()).grid(row=0, 
										column=4, 
										sticky=W, 
										pady=4)
	tk.Button(master, 
			  text='Check Config Screen',
			  bg='red',
			  command = lambda: validate_bars_of_screen(master, controller, itemsFromScreen)).grid(row=0, 
										column=3, 
										sticky=E, 
										pady=4,
										padx=4)

	tk.Button(master, 
			  text='Stop', command = lambda: stop_bot(concur, master)).grid(row=8, 
														   column=2, 
														   sticky=tk.W, 
														   pady=4)

	tk.Button(master, 
			  text='Start', command = lambda: start_bot(concur, master)).grid(row=8, 
														   column=1, 
														   sticky=tk.W, 
														   pady=4)

if __name__ == '__main__':
	firstTime = True
	master = tk.Tk()
	master.geometry("800x300")
	master.resizable(False, False)
	master.title('TibiaBot - Stopped')

	concur = Concur(master)

	#controller = Controller(master, concur, keyListener)
	create_screen(concur, concur.controller)
	concur.start()
	concur.pause()

	tk.mainloop()
	pyautogui.press('delete')
	