# -*- coding: utf-8 -*-

import sys
import time
from threading import Thread
from concurrent.futures import ThreadPoolExecutor

from pynput import mouse, keyboard

from .log import logger
from .config import GUN
from .models import GunType


class PUBG(object):
	def __init__(self):
		self.on = False
		self.shooting = False
		self.gun = GunType(GUN)
		self.mouse = mouse.Controller()
		self.keyborad = keyboard.Controller()
		self.banner()

	def banner(self):
		logger.info('Status: OFF')
		logger.info('Press F5 to start/stop the listening.')
		logger.info('Now you are using {}'.format(self.gun.name))

	def start(self):
		with ThreadPoolExecutor(max_workers=5) as executor:
			executor.submit(self.mouse_listener)
			executor.submit(self.keyboard_listener)
			executor.submit(self.moving)

	# Monitoring the mouse
	def on_move(self, x, y):
		# logger.debug('Pointer moved to {0}'.format((x, y)))
		pass

	def on_click(self, x, y, button, pressed):
		logger.debug('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
		if self.on and button == mouse.Button.left:
			self.shooting = pressed


	def on_scroll(self, x, y, dx, dy):
		logger.debug('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up', (x, y)))
		
	# Monitoring the keyboard
	def on_press(self, key):
		try:
			logger.debug('alphanumeric key {0} pressed'.format(key.char))
		except KeyboardInterrupt:
			sys.exit(0)
		except AttributeError:
			logger.debug('special key {0} pressed'.format(key))

		if key == keyboard.Key.f5:
			self.on = not self.on
			if self.on:
				logger.info('Status: ON')
			else:
				logger.info('Status: OFF')

	def on_release(self, key):
		logger.debug('{0} released'.format(key))

	# listening
	def mouse_listener(self):
		with mouse.Listener(on_move=self.on_move, 
							on_click=self.on_click, 
							on_scroll=self.on_scroll) as listener:
			listener.join()

	def keyboard_listener(self):
		with keyboard.Listener(on_press=self.on_press, 
							   on_release=self.on_release) as listener:
			listener.join()


	# Mouse Cheating track
	def moving(self):
		while True:
			if self.on and self.shooting:
				self.mouse.move(0 ,self.gun.delta)
				print('move move move move')
				time.sleep(self.gun.cd)
				self.gun.init()
			
			
