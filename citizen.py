from faker import Faker
from random import *
from towns import Town
import party

class Citizen(object):
	
	
	def __init__(self):
		fake = Faker()
		self.name = fake.name()
		self.town = Town.rand_town()
		self.issues = party.select_party()
		for n in range(0,len(self.issues)):
			if uniform(0,1) < 0.8:
				if self.issues[n] is 0:
					self.issues[n] += 1
				elif self.issues[n] is 2:
					self.issues[n] -= 1
				else:
					if uniform(0,1) < 0.5:
						self.issues[n] -= 1
					else:
						self.issues[n] += 1