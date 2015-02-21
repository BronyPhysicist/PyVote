'''
Created on Feb 21, 2015

@author: OWNERPC
'''

from random import uniform

def issue_mod(issues, prob):
    for n in range(0,len(issues)):
            if uniform(0,1) < 0.8:
                if issues[n] is 0:
                    issues[n] += 1
                elif issues[n] is 2:
                    issues[n] -= 1
                else:
                    if uniform(0,1) < 0.5:
                        issues[n] -= 1
                    else:
                        issues[n] += 1