'''
Created on Apr 4, 2013

@author: Kiks
'''
 
animals = ["lion","whale","dolphin","shrimp","amoeba"]

animalPrey =  {} 



animalPrey["lion"] = ["gorillas","hyenas","dolphins"]
animalPrey["whale"] = ["plankton","shrimp","corpses"]

print( animalPrey["lion"] )

bottomOfFoodChain = "hamsters"

for animal in animals:
    print("Looking for: " + animal)
    if animal not in animalPrey.keys():
        animalPrey[animal] = []
    animalPrey[animal].append(bottomOfFoodChain)

print(animalPrey)





