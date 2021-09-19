# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 20:35:52 2021

@author: CSM
"""


speech = "I'am so amazed  by the   sheer excellence of this boy-I am so so so grateful for this"
word = "am"

def countRepetition(speech,word):
    new_speech = ''
    for w in speech:
        if w.isalnum():
            new_speech += w
        else:
            new_speech += ' '
    print(new_speech)
    return len([w for w in new_speech.split() if w == word])

print(countRepetition(speech,word))




PhoneAFeatures = ['a','b','c']
PhoneBFeatures = ['b','c','d']

def findComplement(PhoneAFeatures,PhoneBFeatures):
    return [f for f in PhoneBFeatures if f not in PhoneAFeatures]

print(findComplement(PhoneAFeatures,PhoneBFeatures))















