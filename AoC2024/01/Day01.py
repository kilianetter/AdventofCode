
import os
import re



input = "D:/01 Code/adventofcode/AoC2024/01/input.txt"
test_first = "D:/01 Code/adventofcode/AoC2024/01/test_first.txt"
test_second = "D:/01 Code/adventofcode/AoC2024/01/test_second.txt"

infile = input

data = []
a = []
b = []

with open(infile, "r") as file:
    for line in file:
        data.append(line.strip())
    for pair in data:
        a.append(pair.split("   ")[0])
        b.append(pair.split("   ")[1])
    data = [a,b]
        



def solve_first(data):
    a,b = data
    dist = 0
    if len(a) == len(b):
        for i in range(len(a)):
            mina = a.index(min(a)) 
            minb = b.index(min(b))

            dist += abs(int(a.pop(mina)) - int(b.pop(minb)))

            print(dist)

    return dist

 

def solve_second(data):
    a,b = data
    similarity = 0
    for location in a:
        try:
            occurences = [index for index, element in enumerate(b) if element == location]    
        except ValueError:
            occurences = [] 
        similarity += int(location)*len(occurences)
    return similarity


if __name__ == "__main__":
    print(data)
    # first = solve_first(data)
    # print(f'the solution for the first puzzle is: \t {first}')
    second = solve_second(data)
    print(f'the solution for the second puzzle is: \t {second}')