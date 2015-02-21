'''
Created on Feb 21, 2015

@author: OWNERPC
'''
from faker import Faker
from town import Town
from util import issue_mod

class Candidate():
    
    def __init__(self, party):
        fake = Faker()
        self.name = fake.name()
        self.town = Town.rand_town()
        self.party = party
        
        self.issues = issue_mod(party, 0.9)
        