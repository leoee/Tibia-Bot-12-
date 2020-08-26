from pynput.keyboard import Key, Listener
from threading import Thread
import sys

class KeyListener(Thread):
	def __init__ (self, master, concur):
		Thread.__init__(self)
		self.master = master
		self.concur = concur
		self.botIsRunning = False
		self.running = True
		self.keyboard = Listener()

	def on_press(self, key):
		return 

	def on_release(self, key):
		if key == Key.delete:
			self.master.quit()
			return False
		elif key == Key.insert and self.botIsRunning:
			children_widgets = self.master.winfo_children()
			for child_widget in children_widgets:
				if child_widget.winfo_class() == 'Button':
					if (str(child_widget) == ".!button5"):
						child_widget.configure(bg="red")
					elif (str(child_widget) == ".!button4"):
						child_widget.configure(bg="green")
			self.botIsRunning = False
			self.concur.pause()
			self.master.title('TibiaBot - Stopped')
			return True
		elif key == Key.insert and self.botIsRunning == False:
			children_widgets = self.master.winfo_children()
			for child_widget in children_widgets:
				if child_widget.winfo_class() == 'Button':
					if (str(child_widget) == ".!button5"):
						child_widget.configure(bg="green")
					elif (str(child_widget) == ".!button4"):
						child_widget.configure(bg="red")
			self.concur.resume()
			self.botIsRunning = True
			self.master.title('TibiaBot - Running')
			return True

	def run(self):
		if (self.running):
			with Listener(on_press=self.on_press, on_release=self.on_release) as keyListener:
				keyListener.join()

	def stop(self):
		self.running = False

	def resume(self):
		self.running = True