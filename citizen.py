from faker import Faker
from town import Town
from util import issue_mod
import party
import math

class Citizen(object):
	
	def __init__(self, name, town, issues):
		self.name = name; self.town = town; self.issues = issues
		
	def set_issues(self):
		self.issues = issue_mod(party.select_party(self.town), 0.8)
		
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
		csv = self.name+","+str(self.town)+','
		for issue in self.issues:
			csv += str(issue)+','
		csv += str(self.political_avg())
		if csv[-1] is ',':
			csv = csv[:-1]
		if csv[-1] is not '\n':
			csv += '\n'
		return csv
	
	def political_avg(self):
		sm = 0
		for issue in self.issues:
			sm += issue
		return sm/party.N_ISSUES
	
def read_citizens_csv(fname):
	citizens = []
	f = open(fname)
	txt = f.read().split('\n')
	for line in txt:
		if line is '':
			continue
		tks = line.split(',')
		citizens.append(Citizen(tks[0], Town[tks[1]], [int(tks[2]),int(tks[3]),int(tks[4]),int(tks[5]),int(tks[6]),
                                                 int(tks[7]),int(tks[8]),int(tks[9]),int(tks[10]),int(tks[11])]))
	return citizens

def create_citizens():
	print("Population Settings\n================================")
	print("Political Avg: "+str(party.populace_avg()))
	for n in range(0, len(party.parties)):
		print(party.names[n]+' Average: '+str(party.political_avg(n)))
	f = open('./data/voters.txt','w')
	for i in range(0,5000):
		if(i % 100 is 0):
			print("Creating citizen "+str(i)+"...")
		town = Town.rand_town()	
		citizen = Citizen(Faker().name(), town, issue_mod(party.select_party(town), 0.8));
		f.write(citizen.csv_string())
	f.close()