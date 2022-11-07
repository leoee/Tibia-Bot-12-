import tkinter as tk
from tkinter import *

class ScreenConfiguration():
	def create_screen(self, screen, bot_manager, controller):
		fKeys = ('F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 
				'F9', 'F10', 'F11', 'F12', '1', '2', '3', '4'
					, '5', '6', '7', '8', '9', '0', ' ')
				
		tk.Label(screen, 
				text="Current Life").grid(row = 0)
		tk.Label(screen, 
				text="Current Mana").grid(row = 1)
		tk.Label(screen, 
				text="Time(s)").grid(row=5, column = 8)
		tk.Label(screen, 
				text="Life sio(%)").grid(row=8, column = 7)
		tk.Label(screen, 
				text="Auto Ring when").grid(row=7, column = 6)


		totalLife = tk.Entry(screen, width=7)
		totalMana = tk.Entry(screen, width=7)
		timeAutoSpell = tk.Entry(screen, width=7)
		
		totalLife.grid(row=0, column=1)
		totalLife.configure(state="disabled")
		totalMana.grid(row=1, column=1)
		totalMana.configure(state="disabled")
		timeAutoSpell.grid(row=5, column = 9)

		autoUtamo = IntVar()
		Checkbutton(screen, text="Auto Utamo Vita", variable=autoUtamo, state='disable').grid(row=0, column = 6, sticky=W)

		autoUtitoTempo = IntVar()
		Checkbutton(screen, text="Auto Utito Tempo", variable=autoUtitoTempo).grid(row=1, column = 6, sticky=W)

		autoAntiIdle = IntVar()
		Checkbutton(screen, text="Anti Idle", variable=autoAntiIdle).grid(row=2, column = 6, sticky=W)

		eatFood = IntVar()
		Checkbutton(screen, text="Eat Food", variable=eatFood).grid(row=3, column = 6, sticky=W)
		
		autoRun = IntVar()
		Checkbutton(screen, text="Auto Run", variable=autoRun).grid(row=4, column = 6, sticky=W)

		autoSpell = IntVar()
		Checkbutton(screen, text="Auto Spell", variable=autoSpell, state='disable').grid(row=5, column = 6, sticky=W)

		textUtamoVita = StringVar()
		keyUtamoVita = ttk.Combobox(screen, width = 6, textvariable = textUtamoVita)

		keyUtamoVita['values'] = fKeys
			
		keyUtamoVita.grid(row = 0, column = 7, sticky=W) 
		keyUtamoVita.current()	

		textUtitoTempo = StringVar()
		keyUtitoTempo = ttk.Combobox(screen, width = 6, textvariable = textUtitoTempo)

		keyUtitoTempo['values'] = fKeys
			
		keyUtitoTempo.grid(row = 1, column = 7, sticky=W) 
		keyUtitoTempo.current()

		textHur = StringVar()
		keyPressRun = ttk.Combobox(screen, width = 6, textvariable = textHur)

		keyPressRun['values'] = fKeys
			
		keyPressRun.grid(row = 4, column = 7, sticky=W) 
		keyPressRun.current()	
		
		boxAutoSpell = StringVar()
		keyAutoSpell = ttk.Combobox(screen, width = 6, textvariable = boxAutoSpell)
		
		keyAutoSpell['values'] = fKeys 
			
		keyAutoSpell.grid(row = 5, column = 7, sticky=W) 
		keyAutoSpell.current() 

		keyPressFood = StringVar()
		keyChoosen = ttk.Combobox(screen, width = 6, textvariable = keyPressFood)
		
		keyChoosen['values'] = fKeys
			
		keyChoosen.grid(row = 3, column = 7, sticky=W) 
		keyChoosen.current()

		tk.Label(screen, 
				text="Life 90%").grid(row = 3)
				
		keyPressCure90 = StringVar()
		keyChoosenCure90 = ttk.Combobox(screen, width = 6, textvariable = keyPressCure90)
		
		keyChoosenCure90['values'] = fKeys
			
		keyChoosenCure90.grid(row = 3, column = 1, sticky=W) 
		keyChoosenCure90.current()
		
		tk.Label(screen, 
				text="Life 70%").grid(row = 4, column = 0)
				
		keyPressCure70 = StringVar()
		keyChoosenCure70 = ttk.Combobox(screen, width = 6, textvariable = keyPressCure70) 

		keyChoosenCure70['values'] = fKeys
			
		keyChoosenCure70.grid(row = 4, column = 1, sticky=W) 
		keyChoosenCure70.current()

		tk.Label(screen, 
				text="Life 50%").grid(row = 5, column = 0)
				
		keyPressCure50 = StringVar()
		keyChoosenCure50 = ttk.Combobox(screen, width = 6, textvariable = keyPressCure50) 

		keyChoosenCure50['values'] =  fKeys
			
		keyChoosenCure50.grid(row = 5, column = 1, sticky=W) 
		keyChoosenCure50.current()
		
		tk.Label(screen, 
			text="When Mana <").grid(row = 6, column = 0, sticky=W)
		
		manaPercent = tk.Entry(screen, width=6)	
		manaPercent.grid(row=6, column=1, sticky=W)
		
		tk.Label(screen, 
			text="% use").grid(row = 6, column = 2, sticky=W)	
		keyPressCureMana = StringVar()
		keyPressCureMana = ttk.Combobox(screen, width = 6, textvariable = keyPressCureMana) 
			
		keyPressCureMana['values'] =  fKeys
			
		keyPressCureMana.grid(row = 6, column = 3) 
		keyPressCureMana.current()

		tk.Label(screen, 
			text="When Mana >").grid(row = 7, column = 0, sticky=W)
		
		mana_percent_to_train = tk.Entry(screen, width=6)	
		mana_percent_to_train.grid(row=7, column=1, sticky=W)
		
		tk.Label(screen, 
			text="% use").grid(row = 7, column = 2, sticky=E)	
		key_to_press_training_mana = StringVar()
		key_to_press_training_mana = ttk.Combobox(screen, width = 6, textvariable = key_to_press_training_mana) 
			
		key_to_press_training_mana['values'] =  fKeys
			
		key_to_press_training_mana.grid(row = 7, column = 3) 
		key_to_press_training_mana.current()


		tk.Label(screen, 
			text="Auto SSA when Life <").grid(row = 6, column = 6, sticky=W)
		
		life_to_pull_ssa = tk.Entry(screen, width = 4)	
		life_to_pull_ssa.grid(row = 6, column=7, sticky=W)
		
		tk.Label(screen, 
			text="% use").grid(row = 6, column = 8, sticky=W)

		key_to_press_pulling_ssa = StringVar()
		key_to_press_pulling_ssa = ttk.Combobox(screen, width = 3, textvariable = key_to_press_pulling_ssa) 
			
		key_to_press_pulling_ssa['values'] =  fKeys
			
		key_to_press_pulling_ssa.grid(row = 6, column = 9) 
		key_to_press_pulling_ssa.current()

		bar_to_pull_ring = StringVar()
		bar_to_pull_ring = ttk.Combobox(screen, width = 6, textvariable = bar_to_pull_ring) 
			
		bar_to_pull_ring['values'] =  ('MANA', 'LIFE')
			
		bar_to_pull_ring.grid(row = 7, column = 7) 
		bar_to_pull_ring.current()

		value_to_pull_ring = tk.Entry(screen, width = 4)	
		value_to_pull_ring.grid(row = 7, column=8)

		tk.Label(screen, 
			text="% use").grid(row = 7, column = 9)

		key_auto_ring = StringVar()
		key_auto_ring = ttk.Combobox(screen, width = 3, textvariable = key_auto_ring)

		key_auto_ring['values'] = fKeys
			
		key_auto_ring.grid(row = 7, column = 10, sticky=W) 
		key_auto_ring.current()

		tk.Label(screen, 
			text="Ring").grid(row = 7, column = 11, sticky=W)

		ring_type = StringVar()
		ring_type = ttk.Combobox(screen, width = 5, textvariable = ring_type)

		ring_type['values'] = ('Might', 'Energy')
			
		ring_type.grid(row = 7, column = 12, sticky=W) 
		ring_type.current()

		text_life_sio = StringVar()
		life_to_sio = ttk.Combobox(screen, width = 4, textvariable = text_life_sio)

		life_to_sio['values'] = ('90%', '70%', '50%', ' ')
			
		life_to_sio.grid(row = 8, column = 8, sticky=E) 
		life_to_sio.current()	

		tk.Label(screen, 
			text="use").grid(row = 8, column = 9)

		text_life_sio = StringVar()
		key_sio = ttk.Combobox(screen, width = 3, textvariable = text_life_sio)

		key_sio['values'] = fKeys
			
		key_sio.grid(row = 8, column = 10, sticky=W) 
		key_sio.current()	
				
		itemsFromScreen = {
			"keyPressCure90": keyChoosenCure90,
			"keyPressCure70": keyChoosenCure70,
			"keyPressCure50": keyChoosenCure50,
			"manaPercent": manaPercent,
			"mana_percent_to_train": mana_percent_to_train, 
			"keyPressCureMana": keyPressCureMana,
			"key_to_press_training_mana": key_to_press_training_mana,
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
			"life_to_pull_ssa": life_to_pull_ssa,
			"key_to_press_pulling_ssa": key_to_press_pulling_ssa,
			"lifeToUseSio": life_to_sio,
			"keyForSio": key_sio,
			"barToPullRing": bar_to_pull_ring,
			"valueToPullRing": value_to_pull_ring,
			"keyToPullRing": key_auto_ring,
			"ringType": ring_type	
		}

		bot_manager.set_screen(itemsFromScreen)

		tk.Button(screen, 
					text='Check Party List',
					state='disabled',
					activebackground='green',
					command=lambda: controller.check_sio_bar()).grid(row=8, 
											column=6, 
											sticky=W, 
											pady=4)
		tk.Button(screen, 
					text='Check Config Screen',
					state='disabled',
					command = lambda: check_config_screen()).grid(row=0, 
											column=3, 
											sticky=E, 
											pady=4,
											padx=4)

		tk.Button(screen, 
					text='How to configure',
					command = lambda: open_how_to_configure()).grid(row=1, 
											column=3, 
											sticky=E, 
											pady=4,
											padx=4)

		tk.Button(screen, 
					text='Config Screen',
					activebackground='green',
					command=lambda: config_screen()).grid(row=0, 
											column=4, 
											sticky=W, 
											pady=4)

		tk.Button(screen, 
					text='Configure 90%',
					command = lambda: configure_status_90()).grid(row=0, 
											column=9, 
											sticky=E, 
											pady=4,
											padx=4)

		tk.Button(screen, 
					text='Configure 70%',
					command = lambda: configure_status_70()).grid(row=1, 
											column=9, 
											sticky=E, 
											pady=4,
											padx=4)

		tk.Button(screen, 
					text='Configure 50%',
					command = lambda: configure_status_50()).grid(row=2, 
											column=9, 
											sticky=E, 
											pady=4,
											padx=4)

		tk.Button(screen, 
					text='Stop', command = lambda: stop_bot(bot_manager, screen)).grid(row=8, 
																column=2, 
																sticky=tk.W, 
																pady=4)

		tk.Button(screen, 
					text='Start', command = lambda: start_bot(bot_manager, screen)).grid(row=8, 
																column=1, 
																sticky=tk.W, 
																pady=4)