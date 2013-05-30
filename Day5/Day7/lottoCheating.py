'''
Created on May 9, 2013

@author: Kiks
'''

#Has the same sequence ever come up in lotto history?
#Which number has the highest frequency of appearances

import re
import random

lottoFile = open('lotto.txt','r')

sequences = []

#number => numberOfApperances
numberFrequency = {}

print("LottoCheater v 1.0 - Kiks")

print("Collecting sequences..."),

for i, line in enumerate(lottoFile.readlines()):
    if i % 2 != 0:
        #print(line)
        pattern = re.compile(r"(?<!x)[0-9]+") #negative lookbehind assertion
        sequence = [int(num) for num in re.findall(pattern, line)]
        if (len(set(sequence)) != 6):
            print("\n**Faulty line found**")
            print("Line " + str(i+1) + ": " + line)
            break
        #REMEMBER: append() so that list stays intact
        sequences.append(sequence) 
        #print("Numbers found: ", sequence)
else:
    print("DONE")


print("Analyzing sequences...")
numberOfSequences = len(sequences)

#convert list of lists into set of tuples #note immutability
sequenceSet = set( [(a,b,c,d,e,f) for a,b,c,d,e,f in sequences ])
numberOfUniqueSequences = len(sequenceSet)

print("DONE")

print("")
print("-----------------Analysis-----------------")
print("Sequences are unique? " + str(numberOfSequences == numberOfUniqueSequences))

print("")

for sequence in sequences:
    for num in sequence:
        if num not in numberFrequency.keys():
            #initialize key for number
            numberFrequency[num] = 0
        numberFrequency[num] += 1

numberFrequency = sorted( numberFrequency.items(), key= lambda keyCmp: keyCmp[1], reverse=True )

print("**Always use this number: " + str(numberFrequency[0][0]))
print("")
print("**Lucky lotto numbers!**")

def getLuckySequence():
    luckySequence = []
    for i in range(6):
        luckySequence.append(random.randint(1,56))
    if luckySequence in sequences:
        return None
    else:
        return luckySequence

luckySequence = None
while luckySequence is None:
    luckySequence = getLuckySequence()
print(sorted(luckySequence))

print("")

print("Full distribution: ")
for numTuple in numberFrequency:
    print( str(numTuple[0]) + " : " + str(numTuple[1]) )