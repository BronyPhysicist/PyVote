'''
Created on Feb 21, 2015

@author: OWNERPC
'''
from citizen import Citizen

def create_citizens():
    f = open('voters.txt','w')
    for i in range(0,5000):
        if(i % 100 is 0):
            print("Creating citizen "+str(i)+"...")
        citizen = Citizen()
        f.write(citizen.csv_string())
    f.close()
    
#create_citizens()