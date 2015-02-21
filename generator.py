'''
Created on Feb 21, 2015

@author: OWNERPC
'''
from citizen import *
import matplotlib.pyplot as plt
from town import Town
 
def analysis(fname):
    citizens = read_citizens_csv(fname)
    avgs = []
    for citizen in citizens:
        avgs.append(citizen.political_avg())
        citizen.town.add_person(citizen)

    # the histogram of the data
    n, bins, patches = plt.hist(avgs, 40, facecolor='green')
    
    plt.xlabel('Politics')
    plt.ylabel('Voters')
    plt.axis([0, 4, 0, 600])
    
    for town in Town:
        avg = 0
        for citizen in town.pop:
            avg += citizen.political_avg()
        print("The average political measurement for "+town.name+" is "+str(avg/len(town.pop)))

    plt.show()
    
create_citizens()
analysis("./data/voters.txt")