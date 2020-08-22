import threading
import time
from controller import Controller

class Concur(threading.Thread):
	def __init__(self, master):
		super(Concur, self).__init__()
		self.iterations = 0
		self.master = master
		self.daemon = True
		self.paused = True
		self.state = threading.Condition()
		self.controller = Controller(self, self.master)

	def setMaster(self, master):
		self.master = master

	def run(self):
		self.resume()
		while True:
			with self.state:
				if self.paused:
					self.state.wait()
			self.controller.core()
			time.sleep(.1)
			self.iterations += 1

	def resume(self):
		with self.state:
			self.paused = False
			self.state.notify()

	def pause(self):
		with self.state:
			self.paused = True