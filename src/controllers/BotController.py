import threading
from .KeyListener import KeyListener
from .Orchestrator import Orchestrator


class BotController(threading.Thread):
	def __init__(self, screen, pixel_configuration, bar_configuration):
		super(BotController, self).__init__()

		self.iterations = 0
		self.screen = screen
		self.daemon = True
		self.paused = True
		self.state = threading.Condition()
		self.keyListener = KeyListener(self.screen, self)
		self.keyListener.start()
		self.controller = Orchestrator(self, self.screen, self.keyListener, pixel_configuration, bar_configuration)

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