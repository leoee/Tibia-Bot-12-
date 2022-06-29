import threading
import time
from .key_listener import KeyListener
from .actuator import Actuator


class BotManager(threading.Thread):
	def __init__(self, screen):
		super(BotManager, self).__init__()

		self.iterations = 0
		self.screen = screen
		self.daemon = True
		self.paused = True
		self.state = threading.Condition()
		self.keyListener = KeyListener(self.screen, self)
		self.keyListener.start()
		self.controller = Actuator(self, self.screen, self.keyListener)

	def set_screen(self, screen):
		self.screen = screen

	def run(self):
		self.resume()
		while True:
			with self.state:
				if self.paused:
					self.state.wait()
			self.controller.core()
			self.iterations += 1

	def resume(self):
		with self.state:
			self.paused = False
			self.state.notify()

	def pause(self):
		with self.state:
			self.paused = True