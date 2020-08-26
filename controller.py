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

class Controller():
	master = None
	concur = None

	def __init__(self, concur, master, keyListener):
		self.master = master
		self.concur = concur
		self.character = Character(concur)
		self.keyListener = keyListener
		self.x1 = 0
		self.x2 = 0
		self.y1 = 0
		self.y2 = 0
		self.already_checked = False
		self.autoSio = None
		self.np_im = None

	def returnListPointsBar(self):
		file = open("config_screen.txt", "r")
		contents = file.read()
		list = []
		indexPrevious = 0
		indexNext = 0
		for i in range (16):
			value = ""
			indexPrevious = contents.index('"', indexNext + 1)
			indexNext = contents.index('"', indexPrevious + 1)
			for x in range(indexPrevious + 1, indexNext):
				value += contents[x]
			list.append(value)
		return list

	def changeGeneratorToList(self, vector_life, vector_mana):
		for i in range(0, 10):
			vector_life[i] = list(vector_life[i])
			vector_mana[i] = list(vector_mana[i])

	def configHeal(self, master, mustEquipSSA, currentLife, currentMana):
		concur = self.concur
		self.character.setAllAttributesRegardingHeal()
		character = self.character
		
		if (character.valueTotalLife.isdigit() == False or character.valueTotalMana.isdigit() == False):
			return

		currentLifePercent = (float(currentLife/int(character.valueTotalLife)) * 100)
		currentManaPercent = (float(currentMana/int(character.valueTotalMana)) * 100)

		if (character.lifeToPullSSA.isdigit() and currentLifePercent < int(character.lifeToPullSSA) and len(mustEquipSSA) == 0):
			pyautogui.press(character.keyToPullSSA)

		if (character.keyLife90 != " " and currentLifePercent <= 90 and currentLifePercent > 70):
			pyautogui.press(character.keyLife90)
		elif (character.keyLife70 != " " and currentLifePercent <= 70 and currentLifePercent > 50):
			pyautogui.press(character.keyLife70)
		elif (character.keyLife50 != " " and currentLifePercent <= 50):
			pyautogui.press(character.keyLife50)

		if (character.manaPercentForHeal.isdigit() and currentManaPercent <= int(character.manaPercentForHeal) and character.keyPressMana != " "):
			pyautogui.press(character.keyPressMana)

		if (character.manaPercentForTrain.isdigit() and currentManaPercent > int(character.manaPercentForTrain) and character.keyPressTrainMana != " "):
			pyautogui.press(character.keyPressTrainMana)

		if (currentLife > int(character.valueTotalLife)):
			valueTotalLife = currentLife
			concur.master["totalLife"].delete(0, END)
			concur.master["totalLife"].insert(0, str(currentLife))

		if (currentMana > int(character.valueTotalMana)):
			valueTotalMana = currentMana
			concur.master["totalMana"].delete(0, END)
			concur.master["totalMana"].insert(0, str(currentMana))

	def confirmIsTarget(self, image):
		left = pyautogui.locateAll(path + '/images/left.png', image, grayscale=True, confidence=.85)
		right = pyautogui.locateAll(path + '/images/right.png', image, grayscale=True, confidence=.85)
		top = pyautogui.locateAll(path + '/images/top.png', image, grayscale=True, confidence=.85)
		bottom = pyautogui.locateAll(path + '/images/bottom.png', image, grayscale=True, confidence=.85)
			
		if (left != None and right != None and top != None and bottom != None):
			return True

		return False

	def identifyNumbers(self, imgLife, imgMana, vector_life, vector_mana):
		for x in range(0, 10):
			vector_life[x] =  pyautogui.locateAll(path + '/images/' + str(x) + '.png', imgLife, grayscale=True, confidence=.95)
			vector_mana[x] =  pyautogui.locateAll(path + '/images/' + str(x) + '.png', imgMana, grayscale=True, confidence=.95)

	def convertNumbersToString(self, validIndex, vector, currentValue):
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


	def useSpell(self, spell):
		pyautogui.write(spell)
		pyautogui.press('enter')
		pyautogui.write(spell)
		pyautogui.press('enter')
		pyautogui.write(spell)
		pyautogui.press('enter')


	def activeAntiIdle(self):
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
		listPoints = self.returnListPointsBar()
		self.autoSio = pyautogui.screenshot()
		self.autoSio = self.autoSio.crop((int(listPoints[12]), int(listPoints[13]), int(listPoints[14]), int(listPoints[15])))
		hasLifeBarSio = pyautogui.locateAll(path + '/images/sio.png', self.autoSio, grayscale=True, confidence=.95)
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

			children_widgets = self.master.winfo_children()
			for child_widget in children_widgets:
				if child_widget.winfo_class() == 'Button':
					if (str(child_widget) == ".!button"):
						child_widget.configure(bg="green")

	def core(self):
		concur = self.concur
		FLAG_TIME_ANTI_IDLE = 0
		FLAG_TIME_AUTO_SPELL = 0
		FLAG_TIME_AUTO_UTAMO = 0
		time.sleep(1)
		while (True):
			FLAG_TIME_AUTO_SPELL += 1
			FLAG_TIME_ANTI_IDLE += 1
			FLAG_TIME_AUTO_UTAMO += 1
			if (concur.paused == True):
				break

			im=pyautogui.screenshot()
			life = im
			mana = im
			listPoints = self.returnListPointsBar()
			life = life.crop((int(listPoints[0]), int(listPoints[1]), int(listPoints[2]), int(listPoints[3])))
			mana = mana.crop((int(listPoints[4]), int(listPoints[5]), int(listPoints[6]), int(listPoints[7])))

			screenBot = pyautogui.locateAll('images/bot.png', im, grayscale=True, confidence=.70)
			lstScreen = list(screenBot)
			hasSSA = pyautogui.locateAll(path + '/images/ssa.png', im, grayscale=True, confidence=.90)
			listHasSSA = list(hasSSA)

			if (len(lstScreen) != 0):
				self.keyListener.stop()
				continue

			if (self.keyListener.running == False):
				self.keyListener.resume()
			vector_life = {}
			vector_mana = {}

			self.identifyNumbers(life, mana, vector_life, vector_mana)
			validIndexLife = 0
			validIndexMana = 0
			lifeValue = ""
			manaValue = ""
					
			self.changeGeneratorToList(vector_life, vector_mana)
			
			for i in range(0, 10):
				validIndexLife += (sum(x is not None for x in vector_life[i]))
				validIndexMana += (sum(x is not None for x in vector_mana[i]))
				
			if (validIndexLife == validIndexMana and validIndexMana == 0):
				continue;

			lifeValue = self.convertNumbersToString(validIndexLife, vector_life, lifeValue)
			manaValue = self.convertNumbersToString(validIndexMana, vector_mana, manaValue)

			self.master.title('Tibia Bot - Running - Life: ' + str(lifeValue) + ' // Mana: ' + str(manaValue))
			self.configHeal(concur.master, listHasSSA, int(lifeValue), int(manaValue))

			food = im
			food = food.crop((int(listPoints[8]), int(listPoints[9]), int(listPoints[10]), int(listPoints[11])))

			hasHungry = pyautogui.locateAll(path + '/images/food.png', food, grayscale=True, confidence=.75)
			lstHasHungry = list(hasHungry)
			hasSpeed = pyautogui.locateAll(path + '/images/speed.png', food, grayscale=True, confidence=.75)
			lstHasSpeed = list(hasSpeed)
			hasUtamo = pyautogui.locateAll(path + '/images/utamo.png', food, grayscale=True, confidence=.75)
			listHasUtamo = list(hasUtamo)
			hasUtito = pyautogui.locateAll(path + '/images/utito.jpeg', food, grayscale=True, confidence=.75)
			listHasUtito = list(hasUtito)

			mustEatFood = concur.master["eatFood"].get()
			keyPressEatFood = concur.master["keyPressFood"].get().lower()
			mustUseAutoSpell = concur.master["autoSpell"].get()
			keyAutoSpell = concur.master["keyAutoSpell"].get().lower()
			timeAutoSpell = concur.master["timeAutoSpell"].get()
			mustUseHur = concur.master["autoRun"].get()
			spellHur = concur.master["spellHur"].get().lower()
			mustUseUtamo = concur.master["autoUtamo"].get()
			keyAutoUtamo = concur.master["keyUtamoVita"].get().lower()
			mustUseUtito= concur.master["autoUtito"].get()
			keyAutoUtito = concur.master["keyUtito"].get().lower()
			isAntiIdleOn= concur.master["antiIdle"].get()
			life_to_use_sio = concur.master["lifeToUseSio"].get()
			key_sio = concur.master["keyForSio"].get().lower()


			self.check_sio_bar()
			if (self.already_checked):
				x_gap = int(listPoints[12])
				y_gap = int(listPoints[13])
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
				self.activeAntiIdle()
				FLAG_TIME_ANTI_IDLE = 0
