# -*- coding: utf-8 -*-

import random

from .config import GUNS, GUN


# Define the data structure of gun

class GunType(object):
	'''The data structure of a gun
	'''
	def __init__(self, name='m4'):
		self.name  = name
		self.delta = GUNS.get(name).get('delta')
		self.cd    = GUNS.get(name).get('cd')
	
	# random delta and cd
	def init(self):
		self.delta += random.randint(-3, 3)
		self.cd    += random.uniform(0.005, 0.01)

	def __str__(self):
		return '<GunType: {}>'.format(self.name)

	__repr__ = __str__
