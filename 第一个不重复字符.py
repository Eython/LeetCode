# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 20:28:42 2021

@author: CSM
"""


s = 'hackthegame'


def getUniqueCharacter(s):
    
    exclusion = set()
    candidate = []
    
    for i in s:
        if i not in exclusion:
            if i in candidate:
                exclusion.add(i)
                candidate.remove(i)
            else:
                candidate.append(i)
        
        print(exclusion)
        print(candidate)
        
    if candidate:
        return s.find(candidate[0]) + 1
    else:
        return -1
    
print(getUniqueCharacter(s))















