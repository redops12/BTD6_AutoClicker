import time
import threading
import time
from pynput.mouse import Button, Controller as MC
from pynput.keyboard import Listener, KeyCode, Key, Controller as KC


button = Button.left
start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='e')
dart = (538, 625, 'q')
ben = (725, 150, 'u')
wizard = (963, 442, 'a')

class ClickMouse(threading.Thread):
	def __init__(self, button):
		super(ClickMouse, self).__init__()
		self.button = button
		self.running = False
		self.program_running = True

	def start_clicking(self):
		self.running = True

	def stop_clicking(self):
		self.running = False

	def exit(self):
		self.stop_clicking()
		self.program_running = False

	def upg(self, x, y, key, path):
		mc.position = (x,y)
		time.sleep(0.1)	
		mc.click(button.left)
		time.sleep(0.1)	
		arr = ['i','o','p']
		kc.press(arr[path])
		kc.release(arr[path])
		time.sleep(0.1)	
		mc.click(button.left)

	def place(self, x, y, key):
		mc.position = (x,y)
		kc.press(key)
		kc.release(key)
		time.sleep(0.1)
		mc.click(button.left)

	def run(self):
		while self.program_running:
			time.sleep(0.1)
			while self.running:
				#--------Dark forest Easy
				self.place(*dart)
				self.upg(*dart, 1)
				self.upg(*dart, 1)
				self.upg(*dart, 1)
				self.upg(*dart, 2)
				self.upg(*dart, 2)
				kc.press(Key.space)
				kc.release(Key.space)
				time.sleep(0.3)
				kc.press(Key.space)
				kc.release(Key.space)
				time.sleep(62)
				self.place(*wizard)
				time.sleep(12)
				self.upg(*wizard,1)
				time.sleep(20)
				self.place(*ben)				
				time.sleep(24)
				self.upg(*wizard,1)
				time.sleep(16)
				self.upg(*wizard,2)
				time.sleep(14)
				self.upg(*wizard,2)
				time.sleep(38)
				self.upg(*wizard,1)
				time.sleep(200)
				mc.position = (1134, 897)
				mc.click(button.left)
				time.sleep(1)
				mc.position = (947, 764)
				mc.click(button.left)
				time.sleep(1)
				mc.position = (1563, 37)
				mc.click(button.left)
				time.sleep(1)
				mc.position = (1102, 908)
				mc.click(button.left)
				time.sleep(1)
				mc.position = (1175, 778)
				mc.click(button.left)
				time.sleep(1)

mc = MC()
kc = KC()
click_thread = ClickMouse(button)
click_thread.start()

def on_press(key):
	if key == start_stop_key:
		click_thread.start_clicking()
	elif key == exit_key:
		click_thread.exit()
		listener.stop()

with Listener(on_press=on_press) as listener:
	listener.join()
