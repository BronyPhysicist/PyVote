from random import randint
from enum import Enum

N_TOWNS = 10

class Town(Enum):
	Abington = 0
	Boxford = 1
	Carlisle = 2
	Danvers = 3
	Essex = 4
	Foxboro = 5
	Groton = 6
	Haverhill = 7
	Ipswich = 8
	Jonesboro = 9
	
	def __init__(self, number):
		self.pop = []
	
	@classmethod	
	def rand_town(cls):
		i = randint(0,N_TOWNS-1)
		for town in list(Town):
			if town.value is i:
				return town
	
	def add_person(self, citizen):
		self.pop.append(citizen)
	
	def __str__(self):
		return self.name
		
		