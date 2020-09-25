import time
import json
import logging
import random
import os
import pyautogui
import pyscreenshot as ImageGrab
import sys
import tkinter as tk
from tkinter import *
import numpy
from pynput.mouse import Listener as MouseListener
from pynput import mouse
from model.character import Character

path = os.getcwd()
#a = os.path.dirname(os.path.abspath(__file__))
parent = os.path.dirname(path)

class Actuator():
	screen = None
	bot_manager = None

	def __init__(self, bot_manager, screen, keyListener):
		self.screen = screen
		self.bot_manager = bot_manager
		self.character = Character(bot_manager)
		self.keyListener = keyListener
		self.x1 = 0
		self.x2 = 0
		self.y1 = 0
		self.y2 = 0
		self.already_checked = False
		self.autoSio = None
		self.np_im = None

	def get_list_of_points_bar(self):
		file = open(parent + "\src\conf\config_screen.txt", "r")
		contents = file.read()
		list = []
		indexPrevious = 0
		indexNext = 0
		for i in range (20):
			value = ""
			indexPrevious = contents.index('"', indexNext + 1)
			indexNext = contents.index('"', indexPrevious + 1)
			for x in range(indexPrevious + 1, indexNext):
				value += contents[x]
			list.append(value)
		return list

	def change_generator_to_list(self, vector_life, vector_mana):
		for i in range(0, 10):
			vector_life[i] = list(vector_life[i])
			vector_mana[i] = list(vector_mana[i])

	def config_heal(self, screen, mustEquipSSA, must_equip_energy, must_equip_might, currentLife, currentMana):
		bot_manager = self.bot_manager
		self.character.set_all_attributes_about_character()
		character = self.character
		
		if (character.value_total_life.isdigit() == False or character.value_total_mana.isdigit() == False):
			return

		currentLifePercent = (float(currentLife/int(character.value_total_life)) * 100)
		currentManaPercent = (float(currentMana/int(character.value_total_mana)) * 100)

		if (character.key_to_press_when_life_90 != " " and currentLifePercent <= 90 and currentLifePercent > 70):
			pyautogui.press(character.key_to_press_when_life_90)
		elif (character.key_to_press_when_life_70 != " " and currentLifePercent <= 70 and currentLifePercent > 50):
			pyautogui.press(character.key_to_press_when_life_70)
		elif (character.key_to_press_when_life_50 != " " and currentLifePercent <= 50):
			pyautogui.press(character.key_to_press_when_life_50)

		if (character.mana_percent_to_cure.isdigit() and currentManaPercent <= int(character.mana_percent_to_cure) and character.key_to_press_healing_mana != " "):
			pyautogui.press(character.key_to_press_healing_mana)

		if (character.life_to_pull_ssa.isdigit() and currentLifePercent < int(character.life_to_pull_ssa) and len(mustEquipSSA) == 0):
			pyautogui.press(character.key_to_press_pulling_ssa)

		if (character.value_to_pull_ring.isdigit() and character.key_to_pull_ring != ' ' and character.ring_type != ' '):
			if (character.bar_to_pull_ring == 'MANA' and int(character.value_to_pull_ring) >= currentManaPercent):
				if (character.ring_type == 'Might' and len(must_equip_might) == 0):
					pyautogui.press(character.key_to_pull_ring)
				elif (character.ring_type == 'Energy' and len(must_equip_energy) == 0):
					pyautogui.press(character.key_to_pull_ring)
			if (character.bar_to_pull_ring == 'LIFE' and int(character.value_to_pull_ring) >= currentLifePercent):
				if (character.ring_type == 'Might' and len(must_equip_might) == 0):
					pyautogui.press(character.key_to_pull_ring)
				elif (character.ring_type == 'Energy' and len(must_equip_energy) == 0):
					pyautogui.press(character.key_to_pull_ring)
			elif (character.bar_to_pull_ring == 'LIFE'):
				if (character.ring_type == 'Energy' and len(must_equip_energy) != 0):
					pyautogui.press(character.key_to_pull_ring)		

		if (character.mana_percent_to_train.isdigit() and currentManaPercent > int(character.mana_percent_to_train) and character.key_to_press_training_mana != " "):
			pyautogui.press(character.key_to_press_training_mana)

		if (currentLife > int(character.value_total_life)):
			value_total_life = currentLife
			bot_manager.screen["totalLife"].delete(0, END)
			bot_manager.screen["totalLife"].insert(0, str(currentLife))

		if (currentMana > int(character.value_total_mana)):
			value_total_mana = currentMana
			bot_manager.screen["totalMana"].delete(0, END)
			bot_manager.screen["totalMana"].insert(0, str(currentMana))

	def confirm_is_targeted(self, image):
		left = pyautogui.locateAll(parent + '\src\images\left.png', image, grayscale=True, confidence=.85)
		right = pyautogui.locateAll(parent + '\src\images\right.png', image, grayscale=True, confidence=.85)
		top = pyautogui.locateAll(parent + '\src\images\top.png', image, grayscale=True, confidence=.85)
		bottom = pyautogui.locateAll(parent + '\src\images\bottom.png', image, grayscale=True, confidence=.85)
			
		if (left != None and right != None and top != None and bottom != None):
			return True

		return False

	def identify_numbers_on_image(self, imgLife, imgMana, vector_life, vector_mana):
		for x in range(0, 10):
			vector_life[x] =  pyautogui.locateAll(parent + '\src\images\\' + str(x) + '.png', imgLife, grayscale=True, confidence=.95)
			vector_mana[x] =  pyautogui.locateAll(parent + '\src\images\\' + str(x) + '.png', imgMana, grayscale=True, confidence=.95)

	def convert_numbers_to_string(self, validIndex, vector, currentValue):
		while(validIndex):
			max = 2000
			indexRemoved = 0
			insideIndexRemove = 0
			for value in vector:
				if (vector[value] != None):
					for valueIntoItem in vector[value]:
						if (max > valueIntoItem[0]):
							indexRemoved = value
							insideIndexRemove = valueIntoItem
							max = valueIntoItem[0]
			if (insideIndexRemove != 0):
				vector[indexRemoved].remove(insideIndexRemove)
			currentValue += str(indexRemoved)
			validIndex -= 1
		return currentValue

	def use_spell(self, spell):
		pyautogui.write(spell)
		pyautogui.press('enter')
		pyautogui.write(spell)
		pyautogui.press('enter')
		pyautogui.write(spell)
		pyautogui.press('enter')

	def active_anti_idle(self):
		direction = random.randint(0, 4)
		if (direction == 1):
			pyautogui.hotkey('ctrl', 'up')
		elif (direction == 2):
			pyautogui.hotkey('ctrl', 'right')
		elif(direction == 3):
			pyautogui.hotkey('ctrl', 'down')
		else:
			pyautogui.hotkey('ctrl', 'left')

	def check_sio_bar(self):
		#self.already_checked = False
		listPoints = self.get_list_of_points_bar()
		self.autoSio = pyautogui.screenshot()
		self.autoSio = self.autoSio.crop((int(listPoints[16]), int(listPoints[17]), int(listPoints[18]), int(listPoints[19])))
		#self.autoSio = self.autoSio.crop((int(listPoints[12]), int(listPoints[13]), int(listPoints[14]), int(listPoints[15])))
		hasLifeBarSio = pyautogui.locateAll(parent + '\src\images\sio.png', self.autoSio, grayscale=True, confidence=.95)
		listLifeBarSio = list(hasLifeBarSio)

		if (len(listLifeBarSio) != 0 and self.already_checked == False):
			self.already_checked = True
			x1 = listLifeBarSio[0][0] + 8
			y1 = listLifeBarSio[0][1]
			x2 = listLifeBarSio[0][2] + x1 + 1
			y2 = listLifeBarSio[0][3] + y1

			self.x1 = x1
			self.x2 = x2
			self.y1 = y1
			self.y2 = y2

			children_widgets = self.screen.winfo_children()
			for child_widget in children_widgets:
				if child_widget.winfo_class() == 'Button':
					if (str(child_widget) == ".!button"):
						child_widget.configure(bg="green")

	def core(self):
		bot_manager = self.bot_manager
		FLAG_TIME_ANTI_IDLE = 0
		FLAG_TIME_AUTO_SPELL = 0
		FLAG_TIME_AUTO_UTAMO = 0
		time.sleep(1)

		while (True):
			FLAG_TIME_AUTO_SPELL += 1
			FLAG_TIME_ANTI_IDLE += 1
			FLAG_TIME_AUTO_UTAMO += 1

			if (bot_manager.paused == True):
				break

			im = pyautogui.screenshot()
			life = im
			mana = im
			equipment = im
			listPoints = self.get_list_of_points_bar()
			life = life.crop((int(listPoints[0]), int(listPoints[1]), int(listPoints[2]), int(listPoints[3])))
			mana = mana.crop((int(listPoints[4]), int(listPoints[5]), int(listPoints[6]), int(listPoints[7])))
			equipment = equipment.crop((int(listPoints[12]), int(listPoints[13]), int(listPoints[14]), int(listPoints[15])))

			screenBot = pyautogui.locateAll(parent + '\src\images\\bot.png', im, grayscale=True, confidence=.70)
			lstScreen = list(screenBot)
			hasSSA = pyautogui.locateAll(parent + '\src\images\ssa.png', equipment, grayscale=True, confidence=.90)
			listHasSSA = list(hasSSA)
			has_energy_ring = pyautogui.locateAll(parent + '\src\images\energy_ring.png', equipment, grayscale=True, confidence=.90)
			list_has_energy_ring = list(has_energy_ring)
			has_might_ring = pyautogui.locateAll(parent + '\src\images\might_ring.png', equipment, grayscale=True, confidence=.90)
			list_has_might_ring = list(has_might_ring)

			if (len(lstScreen) != 0):
				self.keyListener.stop()
				continue

			if (self.keyListener.running == False):
				self.keyListener.resume()

			vector_life = {}
			vector_mana = {}

			self.identify_numbers_on_image(life, mana, vector_life, vector_mana)

			validIndexLife = 0
			validIndexMana = 0
			lifeValue = ""
			manaValue = ""
					
			self.change_generator_to_list(vector_life, vector_mana)
			
			for i in range(0, 10):
				validIndexLife += (sum(x is not None for x in vector_life[i]))
				validIndexMana += (sum(x is not None for x in vector_mana[i]))
				
			if (validIndexLife == validIndexMana and validIndexMana == 0):
				continue;

			lifeValue = self.convert_numbers_to_string(validIndexLife, vector_life, lifeValue)
			manaValue = self.convert_numbers_to_string(validIndexMana, vector_mana, manaValue)

			self.screen.title('Tibia Bot - Running - Life: ' + str(lifeValue) + ' // Mana: ' + str(manaValue))
			self.config_heal(bot_manager.screen, listHasSSA, list_has_energy_ring, list_has_might_ring, int(lifeValue), int(manaValue))

			food = im
			food = food.crop((int(listPoints[8]), int(listPoints[9]), int(listPoints[10]), int(listPoints[11])))

			hasHungry = pyautogui.locateAll(parent + '\src\images\\food.png', food, grayscale=True, confidence=.75)
			lstHasHungry = list(hasHungry)
			hasSpeed = pyautogui.locateAll(parent + '\src\images\speed.png', food, grayscale=True, confidence=.75)
			lstHasSpeed = list(hasSpeed)
			hasUtamo = pyautogui.locateAll(parent + '\src\images\\utamo.png', food, grayscale=True, confidence=.75)
			listHasUtamo = list(hasUtamo)
			hasUtito = pyautogui.locateAll(parent + '\src\images\\utito.jpeg', food, grayscale=True, confidence=.75)
			listHasUtito = list(hasUtito)

			mustEatFood = bot_manager.screen["eatFood"].get()
			keyPressEatFood = bot_manager.screen["keyPressFood"].get().lower()
			mustUseAutoSpell = bot_manager.screen["autoSpell"].get()
			keyAutoSpell = bot_manager.screen["keyAutoSpell"].get().lower()
			timeAutoSpell = bot_manager.screen["timeAutoSpell"].get()
			mustUseHur = bot_manager.screen["autoRun"].get()
			spellHur = bot_manager.screen["spellHur"].get().lower()
			mustUseUtamo = bot_manager.screen["autoUtamo"].get()
			keyAutoUtamo = bot_manager.screen["keyUtamoVita"].get().lower()
			mustUseUtito= bot_manager.screen["autoUtito"].get()
			keyAutoUtito = bot_manager.screen["keyUtito"].get().lower()
			isAntiIdleOn= bot_manager.screen["antiIdle"].get()
			life_to_use_sio = bot_manager.screen["lifeToUseSio"].get()
			key_sio = bot_manager.screen["keyForSio"].get().lower()

			if (self.already_checked):
				self.check_sio_bar()

				self.autoSio = self.autoSio.crop((int(self.x1), int(self.y1), int(self.x2), int(self.y2)))
				self.np_im = numpy.array(self.autoSio)
				blue, green, red = self.np_im[..., 0], self.np_im[..., 1], self.np_im[..., 2]

				total = int(self.x2- self.x1 + self.y2 - self.y1)
				cont_life = 0
				cont_blue = 0
				cont_green = 0
				cont_red = 0

				for pixel in blue:
					for i in range(len(pixel)):
						if (pixel[i] <= 70 and pixel[i] != 0):
							cont_blue += 1
				for pixel in red:
					for i in range(len(pixel)):
						if (pixel[i] <= 70 and pixel[i] != 0):
							cont_red += 1
				for pixel in green:
					for i in range(len(pixel)):
						if (pixel[i] <= 70 and pixel[i] != 0):
							cont_green += 1

				cont_life = int((cont_blue + cont_green + cont_red)/3)

				if (key_sio != ' ' and life_to_use_sio != ' '):
					if (life_to_use_sio == '90%' and cont_life >= 10):
						pyautogui.press(key_sio)
						cont_life = 0
					elif (life_to_use_sio == '70%' and cont_life >= 60):
						pyautogui.press(key_sio)
						cont_life = 0
					elif (life_to_use_sio == '50%' and cont_life >= 80):
						pyautogui.press(key_sio)
						cont_life = 0						

			if (len(lstHasHungry) != 0 and mustEatFood):
				pyautogui.press(keyPressEatFood)

			if (len(lstHasSpeed) == 0 and mustUseHur and spellHur != " "):
				pyautogui.press(spellHur)

			if (len(listHasUtamo) == 0 and keyAutoUtamo != "" and mustUseUtamo or (190 * 5) <= (FLAG_TIME_AUTO_UTAMO)):
				pyautogui.press(keyAutoUtamo)
				FLAG_TIME_AUTO_UTAMO = 0

			elif (len(listHasUtito) == 0 and mustUseUtito and keyAutoUtito != " "):
				pyautogui.press(keyAutoUtito)

			#elif (mustUseAutoSpell and keyAutoSpell != " " and timeAutoSpell * 5 <= FLAG_TIME_AUTO_SPELL):
			#	pyautogui.press(keyAutoSpell)
			#	FLAG_TIME_AUTO_SPELL = 0

			elif (isAntiIdleOn and (60 * 5) < FLAG_TIME_ANTI_IDLE):
				self.active_anti_idle()
				FLAG_TIME_ANTI_IDLE = 0
