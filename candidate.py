'''
Created on Feb 21, 2015

@author: OWNERPC
'''

class Candidate():
    
    def __init__(self, name, town, party, issues):
        self.name = name; self.town = town; self.party = party; self.issues = issues

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.name == other.name and self.party is other.party
        else:
            return False