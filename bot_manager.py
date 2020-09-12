from key_listener import KeyListener
import threading
import time
from controller import Controller


class BotManager(threading.Thread):
	def __init__(self, screen_manager):
		super(BotManager, self).__init__()
		self.iterations = 0
		self.screen_manager = screen_manager
		self.daemon = True
		self.paused = True
		self.state = threading.Condition()
		self.keyListener = KeyListener(self.screen_manager, self)
		self.keyListener.start()
		self.controller = Controller(self, self.screen_manager, self.keyListener)

	def set_screen_manager(self, screen_manager):
		self.screen_manager = screen_manager

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