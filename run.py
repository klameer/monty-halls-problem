import random
import numpy as np

def run_no_change_doors():
    doors = {'a', 'b', 'c'}
    right_door = set(random.sample(doors, 1))
    guessed_door = set(random.sample(doors, 1))
    if right_door == guessed_door:
        return 1
    else:
        return 0

def run_change_doors():
    doors = {'a', 'b', 'c'}
    right_door = set(random.sample(doors, 1))
    guessed_door = set(random.sample(doors, 1))

    # The opened door is not the guessed door or the right door
    opened_door = set(random.sample(doors - right_door - guessed_door,1))

    # You're changing your guess based on the open door
    changed_door = doors - opened_door - guessed_door    

    if right_door == changed_door:
        return 1
    else:
        return 0

num_simulations = 100
num_turns_per_simulation = 100

no_change_doors_simulations = []
for i in range(num_simulations):
    total = 0
    for j in range(num_turns_per_simulation):
        total += run_no_change_doors()
    no_change_doors_simulations.append(total)
print("Average wins if you didn't change doors is %d%%." % np.mean(no_change_doors_simulations) )

change_doors_simulations = []
for i in range(num_simulations):
    total = 0
    for j in range(num_turns_per_simulation):
        total += run_change_doors()
    change_doors_simulations.append(total)
print("Average wins if you changed doors is %d%%." % np.mean(change_doors_simulations))
