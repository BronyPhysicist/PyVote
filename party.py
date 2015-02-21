import random

'''
Issues
Parties: Liberal, Conservative, Libertarian, Green, Socialist, Christian, Centrist, Taxpayers, Techno, Random
Abbrevs: LBL, CON, LBT, GRN, SOC, CHR, CEN, TAX, TEC, RDM

Version 1: 0 - For; 1 - Indifferent; 2 - Against
Version 2: 0 -Strongly For; 1 - For; 2 - Indifferent; 3 - Against; 4 - Strongly Against
	RULE: For every 5% given, each party gets 1 extra issue to feel strongly about
		Centrists do not feel strongly about any issues

				LBL 	CON 	LBT 	GRN 	SOC 	CHR 	CEN 	TAX 	TEC 	RDM
Gay Marriage	0		3		1		1		1		4		1		2		2		4
Gun Control		1		4		4		1		1		3		2		3		2		1
Finance Reg		1		4		4		1		0		3		2		4		1		1
End Foreign War	0		3		1		0		1		1		1		1		1		1
Environment		1		4		2		0		1		2		1		3		1		3
Medicaid		1		3		2		1		0		3		3		4		2		3
Min Wage Inc	1		3		2		1		1		3		3		4		1		4
Immg. Reform	0		3		2		1		1		3		2		3		2		2
Public HC		0		4		3		1		0		3		3		4		1		2
Legal Drugs		1		3		0		1		1		4		2		2		0		1

AVG				0.6		3.6		2.1		0.8		0.7		2.9		2		3.0		1.3		2.2
Strong Issues	4		4		3		2		3		2		0		3		1		1
'''

N_ISSUES = 10

#     [1,2,2,1,0,0,0,1,2,1]

LBL = [0,1,1,0,1,1,1,0,0,1]
CON = [3,4,4,3,4,3,3,3,4,3]
LBT = [1,4,4,1,1,2,2,2,3,0]
GRN = [1,1,1,0,0,1,1,1,1,1]
SOC = [1,1,0,1,1,0,1,1,0,1]
CHR = [4,3,3,1,2,3,3,3,3,4]
CEN = [1,2,2,1,1,3,3,2,3,2]
TAX = [2,3,4,1,3,4,4,3,4,2]
TEC = [2,2,1,1,1,2,1,2,1,0]
RDM = [4,1,1,1,3,3,4,2,2,1]

N_PARTIES = 10

parties = [LBL,CON,LBT,GRN,SOC,CHR,CEN,TAX,TEC,RDM]

def select_party():
	return parties[random.choice([0]*20 + [1]*17 + [2]*13 + [3]*9 + [4]*10 + [5]*10 + [6]*10 + [7]*6 + [8]*5)]