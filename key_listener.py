from pynput.keyboard import Key, Listener
from threading import Thread
import sys

class KeyListener(Thread):
	def __init__ (self, screen_manager, bot_manager):
		Thread.__init__(self)
		self.screen_manager = screen_manager
		self.bot_manager = bot_manager
		self.bot_is_running = False
		self.running = True
		self.keyboard = Listener()

	def on_press(self, key):
		return 

	def on_release(self, key):
		if key == Key.delete:
			self.screen_manager.quit()
			return False
		elif key == Key.insert and self.bot_is_running:
			children_widgets = self.screen_manager.winfo_children()
			for child_widget in children_widgets:
				if child_widget.winfo_class() == 'Button':
					if (str(child_widget) == ".!button5"):
						child_widget.configure(bg="red")
					elif (str(child_widget) == ".!button4"):
						child_widget.configure(bg="green")
			self.bot_is_running = False
			self.bot_manager.pause()
			self.screen_manager.title('TibiaBot - Stopped')
			return True
		elif key == Key.insert and self.bot_is_running == False:
			children_widgets = self.screen_manager.winfo_children()
			for child_widget in children_widgets:
				if child_widget.winfo_class() == 'Button':
					if (str(child_widget) == ".!button5"):
						child_widget.configure(bg="green")
					elif (str(child_widget) == ".!button4"):
						child_widget.configure(bg="red")
			self.bot_manager.resume()
			self.bot_is_running = True
			self.screen_manager.title('TibiaBot - Running')
			return True

	def run(self):
		if (self.running):
			with Listener(on_press=self.on_press, on_release=self.on_release) as keyListener:
				keyListener.join()

	def stop(self):
		self.running = False

	def resume(self):
		self.running = True