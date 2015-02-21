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
        cit_str = citizen.name+","+citizen.town+','
        for issue in citizen.issues:
            cit_str += str(issue)+','
        cit_str = cit_str[:-1]+'\n'
        f.write(cit_str)
    f.close()
    
create_citizens()