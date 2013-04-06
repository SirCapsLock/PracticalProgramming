'''
Created on Mar 28, 2013

@author: Kiks
'''

from string import ascii_lowercase as lowerAlphabet
from string import ascii_uppercase as upperAlphabet

lowercaseLetters = list(lowerAlphabet)
uppercaseLetters = list(upperAlphabet)


letterList = [(i,j) for i in lowercaseLetters for j in uppercaseLetters]

letterList = []
for i in lowercaseLetters:
    for j in uppercaseLetters:
        letterList.append((i,j))

