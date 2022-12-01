import os
import math
filename = "input.txt"
filepath = os.path.join(os.path.dirname(__file__), filename)

elves = []
cal = 0

with open(filepath, 'r') as file:  
    for line in file.readlines():
        if line.strip() == "":
            elves.append(cal)
            cal = 0
        else:
            cal = cal + int(line)

    # data = file.read()

print(elves)


print("Part one")
print(max(elves))

print("Part two")
elves_s = sorted(elves, reverse=True)
print(sum(elves_s[0:3]))

