import os
import math
filename = "input.txt"
filepath = os.path.join(os.path.dirname(__file__), filename)

input = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw"
]

import string
abc = list(string.ascii_lowercase)
ABC = list(string.ascii_uppercase)




def splitItems(str:str):
    half = int(len(str)/2)
    return [str[0:half], str[half:len(str)]]


abcABC = abc + ABC
prio = 0
p = 0
groups = []


# for line in input:
#     items = splitItems(line)
#     for char in items[0]:
#         if char in items[1]:
#             p = abcABC.index(char)+1
#             print(p)
#     prio += p

with open(filepath, 'r') as file:  
    for line in file.readlines():
        items = splitItems(line)
        for char in items[0]:
            if char in items[1]:
                p = abcABC.index(char)+1
        prio += p


print("Part one")
print(prio)

print(groups)


def splitGroups(lst:list, size:int ):
    for i in range(0, len(lst), size):
        yield lst[i:i + size]


badges = []
grpprio = 0

with open(filepath, 'r') as file:  
    rucksackList = file.readlines()
    groupList = list(splitGroups(rucksackList, 3))
    for group in groupList:
        for char in group[0]:
            if char in group[1] and char in group[2]:
                badges.append(char)
                break
        grpprio += abcABC.index(char)+1

print(badges)

print("Part two")
print(grpprio)

