import random
import math

'''
Issues
Parties: Liberal, Conservative, Libertarian, Green, Socialist, Christian, Centrist, Taxpayers, Techno, Random
Abbrevs: LBL, CON, LBT, GRN, SOC, CHR, CEN, TAX, TEC, RDM

				LBL 	CON 	LBT 	GRN 	SOC 	CHR 	CEN 	TAX 	TEC 	RDM
Gay Marriage	0		2		0		0		0		2		0		1		1		1
Gun Control		0		2		2		0		0		1		1		2		1		2
Finance Reg		0		2		2		0		0		1		1		2		0		0
Overseas War	0		2		0		0		0		0		0		0		0		1
Environment		0		2		1		0		1		1		0		2		0		2
Medicaid		0		2		1		1		0		2		2		2		1		0
Min Wage Inc	0		2		1		0		0		2		2		2		0		1
Immg. Reform	0		2		1		0		1		0		1		2		1		0
Public HC		0		2		2		0		0		2		2		2		0		0
Legal Drugs		0		2		0		0		1		2		1		1		0		1

AVG				0		2		1		0.1		0.3		1.3		1		1.6		0.4		0.8
'''

N_ISSUES = 10

#     [1,2,2,1,0,0,0,1,2,1]

LBL = [0,0,0,0,0,0,0,0,0,0]
CON = [2,2,2,2,2,2,2,2,2,2]
LBT = [0,2,2,0,1,1,1,1,2,0]
GRN = [0,0,0,0,0,1,0,0,0,0]
SOC = [0,0,0,0,1,0,0,1,0,1]
CHR = [2,1,1,0,1,2,2,0,2,2]
CEN = [0,1,1,0,0,2,2,1,2,1]
TAX = [1,2,2,0,2,2,2,2,2,1]
TEC = [1,1,0,0,0,1,0,1,0,0]
RDM = [1,2,0,1,2,0,1,0,0,1]

N_PARTIES = 10

parties = [LBL,CON,LBT,GRN,SOC,CHR,CEN,TAX,TEC,RDM]

def select_party():
	return parties[random.choice([0]*20 + [1]*17 + [2]*13 + [3]*9 + [4]*10 + [5]*10 + [6]*10 + [7]*6 + [8]*5)]

def calc_allegiance(citizen):
	sums = [0]*10
	for i,party in enumerate(parties):
		for n,issue in enumerate(party):
			sums[i] += float((issue - citizen.issues[n])*(issue - citizen.issues[n]))
		sums[i] /= 10
		sums[i] = math.sqrt(sums[i])
	lowest = 2
	best_match = -1
	for n in range(0,len(sums)):
		if sums[n] < lowest:
			lowest = sums[n]
			best_match = n
	return parties[best_match]