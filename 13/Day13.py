import os
import math
import json


filename = "input.txt"
example = "example.txt"
filepath = os.path.join(os.path.dirname(__file__), filename)
expath = os.path.join(os.path.dirname(__file__), example)





# https://adventofcode.com/2022/day/13

left = [1,1,3,1,1]
right = [1,1,5,1,1]

def isOrdered(left:list, right:list):
    maxlen = max(len(left),len(right))
    minlen = min(len(left),len(right))
    for i in range(maxlen):
        print(i, minlen, maxlen)
        if len(left)<len(right) and i > minlen-1:
            return True
        if len(left)>len(right) and i > minlen-1:
            return False
        
        if type(left[i]) != type(right[i]):
            if type(left[i]) != "list":
                left = list(left)
            if type(right[i]) != "list":
                right = list(right)


        elif left[i] > right[i]:
            return False
        elif left[i] < right[i]:
            continue
        else:
            continue
    return True

print(isOrdered(left, right))



        





# run
if __name__ == "__main__":
    with open(filepath, 'r') as file:  
        data = file.read()
        lines = data.split("\n")
    
    print(data)
    print(lines)

    pair = []
    pairs = []
    for n in lines:
        if n != "":
            pair.append(json.loads(n))
        else:
            pairs.append(pair)
            pair = []
    
    print(pairs[0])
    
    
    
    i = 1
    indexOrdered = []
    for pair in pairs:
        left, right = pair
        isOrdered(left, right)
        indexOrdered.append(i)
        i+=1


    p1 = sum(indexOrdered)
    p2 = 0
    # get answer
    print("Part one")
    print(p1)

    print("Part two")
    print(p2)

