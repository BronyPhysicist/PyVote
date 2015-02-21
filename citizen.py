from faker import Faker
from town import Town
import util
import party
import math

class Citizen(object):
	
	
	def __init__(self):
		fake = Faker()
		self.name = fake.name()
		self.town = Town.rand_town()
		self.issues = util.issue_mod(party.select_party())
		
	def calc_allegiance(self):
		sums = [0]*10
		for i,party in enumerate(party.parties):
			for n,issue in enumerate(party):
				sums[i] += float((issue - self.issues[n])*(issue - self.issues[n]))
			sums[i] /= party.N_ISSUES
			sums[i] = math.sqrt(sums[i])
		lowest = 2
		best_match = -1
		for n in range(0,len(sums)):
			if sums[n] < lowest:
				lowest = sums[n]
				best_match = n
		return party.parties[best_match]
	
	def calc_candidate(self, candidate):
		issue_sum = 0
		for i,issue in enumerate(candidate.issues):
			issue_sum += float((issue - self.issues[i])*(issue-self.issues[i]))
		issue_sum /= party.N_ISSUES
		return math.sqrt(sum)
	
	def csv_string(self):
		csv = self.name+","+self.town+','
		for issue in self.issues:
			csv += str(issue)+','
		if csv[-1] is ',':
			csv = csv[:-1]
		if csv[-1] is not '\n':
			csv += '\n'
		return csv