import os
import math
filename = "input.txt"
example = "example.txt"
filepath = os.path.join(os.path.dirname(__file__), filename)


# https://adventofcode.com/2022/day/6

### Hints:
# could use a set for this problem for a more elegant solution
# see https://www.youtube.com/watch?v=LvwsB-JpJmQ


# examples
sig = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

# signal processing
def findSOP(signal:str):
    for i in range(4, len(signal)):
        SOP = list(signal[i-4:i])
        for char in SOP:
            if SOP.count(char)>1:
                duplicate = True
                break
            else:
                duplicate = False
        if duplicate == False:
            break
    return i

def findSOM(signal:str):
    for i in range(14, len(signal)):
        SOP = list(signal[i-14:i])
        for char in SOP:
            if SOP.count(char)>1:
                duplicate = True
                break
            else:
                duplicate = False
        if duplicate == False:
            break
    return i

# get data
with open(filepath, 'r') as file:  
        data = file.read()


# get answers
SOP = findSOP(data)
SOM = findSOM(data)

print("Part one")
print(SOP)

print("Part two")
print(SOM)

