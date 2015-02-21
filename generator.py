'''
Created on Feb 21, 2015

@author: OWNERPC
'''
from citizen import Citizen
import party

def create_citizens():
    print("Population Settings\n================================")
    print("Political Avg: "+str(party.populace_avg()))
    for n in range(0, len(party.parties)):
        print(party.names[n]+' Average: '+str(party.political_avg(n)))
    f = open('voters.txt','w')
    for i in range(0,5000):
        if(i % 100 is 0):
            print("Creating citizen "+str(i)+"...")
        citizen = Citizen()
        f.write(citizen.csv_string())
    f.close()
    
create_citizens()