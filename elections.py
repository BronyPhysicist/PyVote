'''
Created on Feb 21, 2015

@author: OWNERPC
'''
from candidate import Candidate
import citizen as czn
from faker import Faker
from util import issue_mod
from town import Town
import copy
import party
import sys
import uuid

def find_winner(results, population):
    required = population/2
    for result in results:
        if result[2] > required:
            return result
    if len(results) is 1:
        #print('Winner by default.')
        return results[0]
    return None

def runoff(ballot_box, results, town):
    if len(results) is 0:
        sys.exit('You done goofed.')
    least = len(town.pop)
    loser = -1
    for result in results:
        if result[2] < least:
            least = result[2]
            loser = result
    #print("Identified "+loser[0].name+'/'+loser[0].party+" as the biggest loser with only "+str(loser[2])+" votes.")
    
    for vote in ballot_box:
        for choice in vote:
            if choice.name is loser[0].name:
                vote.remove(choice)
    return ballot_box, loser

def count_votes(ballot_box, results):
    for n in range(0, len(results)):
        results[n] = (results[n][0], results[n][1], 0)
    for vote in ballot_box:
        if len(vote) < 1:
            continue
        for n,result in enumerate(results):
            if vote[0] is result[0]:
                results[n] = (result[0], result[1], result[2] + 1)
        
    for result in results:
        if result[2] is 0:
            results.remove(result)
    return results
    
def candidate_to_id(candidate, candidates):
    for can in candidates:
        if can[0] is candidate:
            return can[1]
    return None

def id_to_candidate(index, candidates):
    for can in candidates:
        if can[1] is index:
            return can[0]
    return None

def election(town):
    analysis = []
    
    citizens = czn.read_citizens_csv("./data/voters.txt")
    for citizen in citizens:
        if citizen.town is town:
            town.add_person(citizen)
    analysis.append(town)
    #print(town.name+" polls open for "+str(len(town.pop))+" people...")
    results = []; losers = []
    ballot_box = []
    for n,prt in enumerate(party.names):
        candidate = Candidate(Faker().name(), town, prt, issue_mod(party.parties[n], 0.9))
        results.append( (candidate, uuid.uuid4(), 0) )
        #print(candidate.name+" from the "+candidate.party+" is running.")
    
    #Voting
    for citizen in town.pop:
        can_no_id = []
        for can in results:
            can_no_id.append(can[0])
        ballot_box.append(citizen.vote(can_no_id))
    #print("...and polls are closed.\n")
    
    results = count_votes(ballot_box, results)
    #print("Preliminary Results")
    high = 0
    winning = None
    for n,res in enumerate(results):
        can = res[0]
        if res[2] > high:
            high = res[2]
            winning = res
        #print(can.name+"/"+can.party+': '+str(res[2])+' votes.')
    #print('')
    analysis.append(copy.deepcopy(results))
    analysis.append(winning)
    n = 0
    while find_winner(results, len(town.pop)) is None:
        n += 1
        ballot_box, loser = runoff(ballot_box, results, town)
        losers.append(loser)
        results = count_votes(ballot_box, results)
    analysis.append(n)
    for loser in losers:
        analysis.append(loser)
    winner = find_winner(results, len(town.pop))
    #print("\n"+town.name+" Election Results\n===========================================================")
    #print("Winner is "+winner[0].name+'/'+winner[0].party+" with "+str(winner[2])+" votes.")
    #print("This election had "+str(n)+" runoffs.\n")
    #print("Surviving Candidates are: ")
    analysis.append(results)
    analysis.append(winner)
    
    return analysis
        
file_for_later = open('./data/results.txt', 'w')
party_victories = [0]*party.N_PARTIES
for i in range(0, 10):
    print('Carrying through eleciton #'+str(i+1)+'...\n')
    for town in list(Town):
        town.empty()
        analysis = election(town)
        n = 0
        file_for_later.write('Election for '+analysis[n].name+' and for '+str(len(analysis[n].pop))+' people.\n')
        n += 1
        file_for_later.write('These are the initial results: \n')
        for res in analysis[n]:
            pct = int(len(town.pop)/100)
            tabs = 10-int(len(str(res[0])+': ')/4)
            file_for_later.write(str(res[0])+': '+'\t'*tabs+'#'*int(res[2]/pct)+' '+str('%.2f'%(100*float(res[2])/len(town.pop)))+'\n')
        n += 1
        file_for_later.write('Projected Winner: '+str(analysis[n][0])+' with '+str(analysis[n][2])+' votes.\n')
        n += 1
        runoffs = analysis[n]
        file_for_later.write('Election had '+str(runoffs)+' runoffs.\n')
        n += 1
        for i in range(n, n+runoffs):
            file_for_later.write('\t\tLosing candidate: '+str(analysis[i][0])+' with '+str(analysis[i][2])+' votes.\n')
        n += runoffs
        file_for_later.write('Winners of the election are:\n')
        for res in analysis[n]:
            pct = int(len(town.pop)/100)
            tabs = 10-int(len(str(res[0])+': ')/4)
            file_for_later.write(str(res[0])+': '+'\t'*tabs+'#'*int(res[2]/pct)+' '+str(res[2])+' votes ('+str('%.2f'%(100*float(res[2])/len(town.pop)))+'%) votes.\n')
        n += 1
        party_victories[party.names.index(analysis[n][0].party)] += 1
        file_for_later.write('\n\n')
file_for_later.write('Grand Totals: \n')
for n in range(0, len(party_victories)):
    file_for_later.write(party.names[n]+' has '+str(party_victories[n])+' wins.\n')
file_for_later.close()