class Character():
	def __init__(self, bot):
		self.bot = bot
		self.value_total_mana = None
		self.value_total_life = None
		self.key_to_press_when_life_90 = None
		self.key_to_press_when_life_70 = None
		self.key_to_press_when_life_50 = None
		self.mana_percent_to_cure = None
		self.mana_percent_to_train = None
		self.key_to_press_healing_mana = None
		self.key_to_press_training_mana = None
		self.life_to_pull_ssa = None
		self.key_to_press_pulling_ssa = None
		self.value_to_pull_ring = None
		self.key_to_pull_ring = None
		self.bar_to_pull_ring = None
		self.ring_type = None
		self.key_eat_food = None
		self.key_spell_hur = None
		self.key_auto_utamo = None
		self.key_auto_utito = None
		self.key_sio = None


	def set_all_attributes_about_character(self):
		bot = self.bot
		self.set_character_life_attributes(bot)
		self.set_character_mana_attributes(bot)
		self.set_character_support_attributes(bot)

	def set_character_life_attributes(self, bot):
		self.value_total_life = bot.screen["totalLife"].get()
		self.key_to_press_when_life_90 = bot.screen["keyPressCure90"].get().lower()
		self.key_to_press_when_life_70 = bot.screen["keyPressCure70"].get().lower()
		self.key_to_press_when_life_50 = bot.screen["keyPressCure50"].get().lower()

	def set_character_mana_attributes(self, bot):
		self.value_total_mana = bot.screen["totalMana"].get()
		self.mana_percent_to_cure = bot.screen["manaPercent"].get()
		self.mana_percent_to_train = bot.screen["mana_percent_to_train"].get()
		self.key_to_press_healing_mana = bot.screen["keyPressCureMana"].get().lower()
		self.key_to_press_training_mana = bot.screen["key_to_press_training_mana"].get().lower()

	def set_character_support_attributes(self, bot):
		self.life_to_pull_ssa = bot.screen["life_to_pull_ssa"].get()
		self.key_to_press_pulling_ssa = bot.screen["key_to_press_pulling_ssa"].get().lower()
		self.bar_to_pull_ring = bot.screen["barToPullRing"].get()
		self.value_to_pull_ring = bot.screen["valueToPullRing"].get()
		self.key_to_pull_ring = bot.screen["keyToPullRing"].get().lower()
		self.ring_type = bot.screen["ringType"].get()
		self.key_eat_food = bot.screen["keyPressFood"].get().lower()
		self.key_spell_hur = bot.screen["spellHur"].get().lower()
		self.key_auto_utamo = bot.screen["keyUtamoVita"].get().lower()
		self.key_auto_utito = bot.screen["keyUtito"].get().lower()
		self.key_sio = bot.screen["keyForSio"].get().lower()

	