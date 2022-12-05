import os
import math
filename = "input.txt"
filepath = os.path.join(os.path.dirname(__file__), filename)

def contained(str:str):
    elves = str.split(",")
    first = elves[0].split("-")
    second = elves[1].split("-")
    contained = False
    if int(first[0]) >= int(second[0]) and int(first[1]) <= int(second[1]):
        contained = True
        print(f'{first} - {second} - first in second')
    elif int(second[0]) >= int(first[0]) and int(second[1]) <= int(first[1]):
        contained = True
        print(f'{first} - {second} - second in first')
    return contained

def overlap(str:str):
    elves = str.split(",")
    first = elves[0].split("-")
    second = elves[1].split("-")
    overlap = False
    if (int(first[0]) >= int(second[0]) and int(first[0]) <= int(second[1])) or (int(first[1]) >= int(second[0]) and int(first[1]) <= int(second[1])):
        overlap = True
        print(f'{first} - {second} - first over second')
    elif (int(second[0]) >= int(first[0]) and int(second[0]) <= int(first[1])) or (int(second[1]) >= int(first[0]) and int(second[1]) <= int(first[1])):
        overlap = True
        print(f'{first} - {second} - second over first')
    return overlap


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

