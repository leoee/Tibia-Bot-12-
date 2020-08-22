class Character():
	def __init__(self, concur):
		self.concur = concur
		self.valueTotalMana = None
		self.valueTotalLife = None
		self.keyLife90 = None
		self.keyLife70 = None
		self.keyLife50 = None
		self.manaPercentForHeal = None
		self.manaPercentForTrain = None
		self.keyPressMana = None
		self.keyPressTrainMana = None
		self.lifeToPullSSA = None
		self.keyToPullSSA = None

	def setAllAttributes(self):
		concur = self.concur
		self.valueTotalMana = concur.master["totalMana"].get()
		self.valueTotalLife = concur.master["totalLife"].get()
		self.keyLife90 = concur.master["keyPressCure90"].get().lower()
		self.keyLife70 = concur.master["keyPressCure70"].get().lower()
		self.keyLife50 = concur.master["keyPressCure50"].get().lower()
		self.manaPercentForHeal = concur.master["manaPercent"].get()
		self.manaPercentForTrain = concur.master["manaPercentForTrain"].get()
		self.keyPressMana = concur.master["keyPressCureMana"].get().lower()
		self.keyPressTrainMana = concur.master["keyPressTrainMana"].get().lower()
		self.lifeToPullSSA = concur.master["lifeToPullSSA"].get()
		self.keyToPullSSA = concur.master["keyToPullSSA"].get().lower()
	