import os
import math
import numpy as np
filename = "input.txt"
filepath = os.path.join(os.path.dirname(__file__), filename)


# https://adventofcode.com/2022/day/5

foo = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 
 """

bar = []
for line in foo:
    bar.append(list(line))

print (foo)
print (bar)
crates = np.empty([3,3], dtype=str)




cont = 0
over = 0

with open(filepath, 'r') as file:  
    for line in file.readlines():
        c = contained(line.strip())
        o = overlap(line.strip())
        cont += c
        over += o


print("Part one")
print(cont)


print("Part two")
print(over)

