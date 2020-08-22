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
from pynput.mouse import Listener as MouseListener
from pynput import mouse

path = os.getcwd()

class Controller():
	master = None
	concur = None

	def __init__(self, concur, master):
		self.master = master
		self.concur = concur

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
		valueTotalMana = concur.master["totalMana"].get()
		valueTotalLife = concur.master["totalLife"].get()
		keyLife90 = concur.master["keyPressCure90"].get().lower()
		keyLife70 = concur.master["keyPressCure70"].get().lower()
		keyLife50 = concur.master["keyPressCure50"].get().lower()
		manaPercentForHeal = concur.master["manaPercent"].get()
		manaPercentForTrain = concur.master["manaPercentForTrain"].get()
		keyPressMana = concur.master["keyPressCureMana"].get().lower()
		keyPressTrainMana = concur.master["keyPressTrainMana"].get().lower()
		lifeToPullSSA = concur.master["lifeToPullSSA"].get()
		keyToPullSSA = concur.master["keyToPullSSA"].get().lower()
		
		if (valueTotalLife.isdigit() == False or valueTotalMana.isdigit() == False):
			return

		if (currentLife > int(valueTotalLife)):
			valueTotalLife = currentLife
			concur.master["totalLife"].delete(0, END)
			concur.master["totalLife"].insert(0, str(currentLife))

		if (currentMana > int(valueTotalMana)):
			valueTotalMana = currentMana
			concur.master["totalMana"].delete(0, END)
			concur.master["totalMana"].insert(0, str(currentMana))

		currentLifePercent = (float(currentLife/int(valueTotalLife)) * 100)
		currentManaPercent = (float(currentMana/int(valueTotalMana)) * 100)

		if (currentLifePercent < int(lifeToPullSSA) and len(mustEquipSSA) == 0):
			pyautogui.press(keyToPullSSA)

		if (currentLifePercent <= 50 and keyLife50 != " "):
			pyautogui.press(keyLife50)
		elif (currentLifePercent <= 70 and keyLife70 != " "):
			pyautogui.press(keyLife70)
		elif (currentLifePercent <= 90 and keyLife90 != " "):
			pyautogui.press(keyLife90)
		
		if (manaPercentForHeal.isdigit() == False and manaPercentForTrain.isdigit() == False):
			return

		if (manaPercentForHeal.isdigit() and currentManaPercent <= int(manaPercentForHeal) and keyPressMana != " "):
			pyautogui.press(keyPressMana)

		if (manaPercentForTrain.isdigit() and currentManaPercent > int(manaPercentForTrain) and keyPressTrainMana != " "):
			pyautogui.press(keyPressTrainMana)

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
			vector_life[x] =  pyautogui.locateAll(path + '/images/' + str(x) + '.png', imgLife, grayscale=True, confidence=.90)
			vector_mana[x] =  pyautogui.locateAll(path + '/images/' + str(x) + '.png', imgMana, grayscale=True, confidence=.90)

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
			time.sleep(0.2)
			im=pyautogui.screenshot()
			life = im
			mana = im
			food = im
			isTarget = im
			listPoints = self.returnListPointsBar()
			life = life.crop((int(listPoints[0]), int(listPoints[1]), int(listPoints[2]), int(listPoints[3])))
			mana = mana.crop((int(listPoints[4]), int(listPoints[5]), int(listPoints[6]), int(listPoints[7])))
			food = food.crop((int(listPoints[8]), int(listPoints[9]), int(listPoints[10]), int(listPoints[11])))
			#isTarget = isTarget.crop((int(listPoints[12]), int(listPoints[13]), int(listPoints[14]), int(listPoints[15])))
			
			screenBot = pyautogui.locateAll('images/bot.png', im, grayscale=True, confidence=.70)
			lstScreen = list(screenBot)

			vector_life = {}
			vector_mana = {}
			
			hasHungry = pyautogui.locateAll(path + '/images/food.png', food, grayscale=True, confidence=.75)
			lstHasHungry = list(hasHungry)
			hasSpeed = pyautogui.locateAll(path + '/images/speed.png', food, grayscale=True, confidence=.75)
			lstHasSpeed = list(hasSpeed)
			hasUtamo = pyautogui.locateAll(path + '/images/utamo.png', food, grayscale=True, confidence=.75)
			listHasUtamo = list(hasUtamo)
			hasUtito = pyautogui.locateAll(path + '/images/utamo.png', food, grayscale=True, confidence=.75)
			listHasUtito = list(hasUtito)
			hasSSA = pyautogui.locateAll(path + '/images/ssa.png', im, grayscale=True, confidence=.90)
			listHasSSA = list(hasSSA)
			
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
					
			lifeValue = self.convertNumbersToString(validIndexLife, vector_life, lifeValue)
			manaValue = self.convertNumbersToString(validIndexMana, vector_mana, manaValue)

			self.master.title('Tibia Bot - Running - Life: ' + str(lifeValue) + ' // Mana: ' + str(manaValue))
			self.configHeal(concur.master, listHasSSA, int(lifeValue), int(manaValue))

			if (len(lstScreen) != 0):
				continue

			if (len(lstHasHungry) != 0 and mustEatFood):
				pyautogui.press(keyPressEatFood)

			if (len(lstHasSpeed) == 0 and mustUseHur and spellHur != " "):
				pyautogui.press(spellHur)

			if (len(listHasUtamo) == 0 and keyAutoUtamo != "" and mustUseUtamo or (190 * 5) <= (FLAG_TIME_AUTO_UTAMO)):
				pyautogui.press(keyAutoUtamo)
				FLAG_TIME_AUTO_UTAMO = 0

			elif (len(listHasUtito) == 0 and mustUseUtito and keyAutoUtito != " "):
				pyautogui.press(keyAutoUtito)

			elif (mustUseAutoSpell and keyAutoSpell != " " and timeAutoSpell * 5 <= FLAG_TIME_AUTO_SPELL):
				pyautogui.press(keyAutoSpell)
				FLAG_TIME_AUTO_SPELL = 0

			elif (isAntiIdleOn and (60 * 5) < FLAG_TIME_ANTI_IDLE):
				self.activeAntiIdle()
				FLAG_TIME_ANTI_IDLE = 0