import time
import random
import os
import pyautogui
import numpy
from model.character import Character

path = os.getcwd()
parent = os.path.dirname(path)

class Orchestrator():
	screen = None
	bot_manager = None
	pixel_configuration = None
	bar_configuration = None

	def __init__(self, bot_manager, screen, keyListener, pixel_configuration, bar_configuration):
		self.screen = screen
		self.bot_manager = bot_manager
		self.character = Character(bot_manager)
		self.keyListener = keyListener
		self.pixel_configuration = pixel_configuration
		self.bar_configuration = bar_configuration
		self.x1 = 0
		self.x2 = 0
		self.y1 = 0
		self.y2 = 0
		self.already_checked = False
		self.autoSio = None
		self.np_im = None

	def config_heal(self, screen, mustEquipSSA, must_equip_energy, must_equip_might, currentLife, currentMana):
		self.character.set_all_attributes_about_character()
		character = self.character

		currentLifePercent = currentLife
		currentManaPercent = currentMana

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
		locations = self.bar_configuration.get_bar_locations()
		party_list_location = locations['party_list']
		# self.autoSio = pyautogui.screenshot()
		self.autoSio = pyautogui.screenshot(region=(party_list_location['left'], party_list_location['top'], party_list_location['width'], party_list_location['height']))
		hasLifeBarSio = pyautogui.locateAll(parent + '\src\images\sio.png', self.autoSio, grayscale=False, confidence=.95)
		listLifeBarSio = list(hasLifeBarSio)
		life_status_bar_sio = None
		print(len(listLifeBarSio))

		if len(listLifeBarSio) > 1:
			if listLifeBarSio[0][1] <= listLifeBarSio[1][1]:
				life_status_bar_sio = listLifeBarSio[0]
			else:
				life_status_bar_sio = listLifeBarSio[1]
		elif len(listLifeBarSio) == 1:
			life_status_bar_sio = listLifeBarSio[0]

		if (life_status_bar_sio != None and self.already_checked == False):
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

			# Take screenshot
			im = pyautogui.screenshot()
			equipment = im

			# Cut screenshot according coordinates on the screen
			locations = self.bar_configuration.get_bar_locations()
			life_location = locations['life']
			mana_location = locations['mana']
			statuses_location = locations['statuses']
			equipment_location = locations['status_fight']
			party_list_location = locations['party_list']

			life = pyautogui.screenshot(region=(life_location['left'], life_location['top'], life_location['width'], life_location['height']))
			total_red_pixels = self.pixel_configuration.count_pix_color(numpy.array(life))

			mana = pyautogui.screenshot(region=(mana_location['left'], mana_location['top'], mana_location['width'], mana_location['height']))
			total_blue_pixels = self.pixel_configuration.count_pix_color(numpy.array(mana))

			equipment = pyautogui.screenshot(region=(equipment_location['left'], equipment_location['top'], equipment_location['width'], equipment_location['height']))

			# Check if screen of the bot is active. This means user is configuring.
			screenBot = pyautogui.locateAll(parent + '\src\images\\bot.png', im, grayscale=True, confidence=.70)
			lstScreen = list(screenBot)

			# Check if has SSA on the equipment.
			hasSSA = pyautogui.locateAll(parent + '\src\images\ssa.png', equipment, grayscale=True, confidence=.65)
			listHasSSA = list(hasSSA)

			# Check if has energy or might ring on the equipment.
			has_energy_ring = pyautogui.locateAll(parent + '\src\images\energy_ring.png', equipment, grayscale=True, confidence=.65)
			list_has_energy_ring = list(has_energy_ring)
			has_might_ring = pyautogui.locateAll(parent + '\src\images\might_ring.png', equipment, grayscale=True, confidence=.65)
			list_has_might_ring = list(has_might_ring)

			lifeValue = self.bar_configuration.get_status_bar_in_percent(total_red_pixels)
			manaValue = self.bar_configuration.get_status_bar_in_percent(total_blue_pixels)

			if (len(lstScreen) != 0):
				self.screen.title('Tibia Bot - Paused - Life: ' + str(lifeValue) + '% // Mana: ' + str(manaValue) + '%')
				self.keyListener.stop()
				continue

			if (self.keyListener.running == False):
				self.keyListener.resume()

			self.screen.title('Tibia Bot - Running - Life: <=' + str(lifeValue) + '% // Mana: <=' + str(manaValue) + '%')

			self.config_heal(bot_manager.screen, listHasSSA, list_has_energy_ring, list_has_might_ring, int(lifeValue), int(manaValue))

			# Need refactor to increase performance. Need to use crop
			tools = pyautogui.screenshot(region=(statuses_location['left'], statuses_location['top'], statuses_location['width'], statuses_location['height']))

			hasHungry = pyautogui.locateAll(parent + '\src\images\\food.png', tools, grayscale=True, confidence=.70)
			lstHasHungry = list(hasHungry)
			hasSpeed = pyautogui.locateAll(parent + '\src\images\speed.png', tools, grayscale=True, confidence=.70)
			lstHasSpeed = list(hasSpeed)
			hasUtamo = pyautogui.locateAll(parent + '\src\images\\utamo.png', tools, grayscale=True, confidence=.70)
			listHasUtamo = list(hasUtamo)
			hasUtito = pyautogui.locateAll(parent + '\src\images\\utito.jpeg', tools, grayscale=True, confidence=.70)
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
				self.autoSio.show()
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
