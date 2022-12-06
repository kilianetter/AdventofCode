import os
import math
filename = "input.txt"
example = "example.txt"
filepath = os.path.join(os.path.dirname(__file__), filename)


# https://adventofcode.com/2022/day/6


sig = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"



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




with open(filepath, 'r') as file:  
        data = file.read()

print(data)


SOP = findSOP(data)

SOM = findSOM(data)

# get answer


# set single to True
print("Part one")
print(SOP)

# set single to False
print("Part two")
print(SOM)

