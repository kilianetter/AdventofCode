
import os
import re
import numpy as np




input = "AoC2024/02/input.txt"
test_first = "AoC2024/02/test_first.txt"
test_second = "AoC2024/02/test_second.txt"

infile = input

data = []
a = []
b = []

with open(infile, "r") as file:
    for line in file:
        data.append(list(map(int, line.strip().split()))) 

### Helper
def is_sorted(lst):
    if np.all(np.diff(lst) >= 1) and np.all(np.diff(lst) <=3):
        return True
    else:
        return False
    


def solve_first(data):
    safe = 0
    for line in data:
        # ascending
        if is_sorted(line):
            safe +=1
        # descending
        elif is_sorted(line[::-1]):
            safe +=1
    return safe

 

def solve_second(data):
    safe = 0
    for line in data:
        for i in range(len(line)):
            modified_list = line[:i] + line[i + 1:]  # Remove the i-th element
            if is_sorted(modified_list) or is_sorted(modified_list[::-1]):
                safe +=1
                break
    return safe


if __name__ == "__main__":
    #print(data)
    first = solve_first(data)
    print(f'the solution for the first puzzle is: \t {first}')
    second = solve_second(data)
    print(f'the solution for the second puzzle is: \t {second}')