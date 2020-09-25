class Character():
	def __init__(self, bot_manager):
		self.bot_manager = bot_manager
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


	def set_all_attributes_about_character(self):
		bot_manager = self.bot_manager
		self.set_character_life_attributes(bot_manager)
		self.set_character_mana_attributes(bot_manager)
		self.set_character_support_attributes(bot_manager)

	def set_character_life_attributes(self, bot_manager):
		self.value_total_life = bot_manager.screen["totalLife"].get()
		self.key_to_press_when_life_90 = bot_manager.screen["keyPressCure90"].get().lower()
		self.key_to_press_when_life_70 = bot_manager.screen["keyPressCure70"].get().lower()
		self.key_to_press_when_life_50 = bot_manager.screen["keyPressCure50"].get().lower()

	def set_character_mana_attributes(self, bot_manager):
		self.value_total_mana = bot_manager.screen["totalMana"].get()
		self.mana_percent_to_cure = bot_manager.screen["manaPercent"].get()
		self.mana_percent_to_train = bot_manager.screen["mana_percent_to_train"].get()
		self.key_to_press_healing_mana = bot_manager.screen["keyPressCureMana"].get().lower()
		self.key_to_press_training_mana = bot_manager.screen["key_to_press_training_mana"].get().lower()

	def set_character_support_attributes(self, bot_manager):
		self.life_to_pull_ssa = bot_manager.screen["life_to_pull_ssa"].get()
		self.key_to_press_pulling_ssa = bot_manager.screen["key_to_press_pulling_ssa"].get().lower()
		self.bar_to_pull_ring = bot_manager.screen["barToPullRing"].get()
		self.value_to_pull_ring = bot_manager.screen["valueToPullRing"].get()
		self.key_to_pull_ring = bot_manager.screen["keyToPullRing"].get().lower()
		self.ring_type = bot_manager.screen["ringType"].get()

	