

import os
import re

input = "D:/Code/01/input.txt"
test_first = "D:/Code/01/test_first.txt"
test_second = "D:/Code/01/test_second.txt"

infile = input

data = []

with open(infile, "r") as file:
    for line in file:
        data.append(line.strip())


def solve_first(data):
    vals = []
    for line in data:
        chars = list(line)
        nums = []
        for char in chars:
            try:
                int(char) ### can check this with char.isdigit()
                nums.append(char)
            except:
                continue
        val = int(nums[0] + nums[-1])
        vals.append(val)
    return sum(vals)

 

def solve_second(data):
    p1 = 0
    p2 = 0
    for line in data:
        p1_digits = []
        p2_digits = []
        for i, char in enumerate(line):
            if char.isdigit():
                # p1_digits.append(char)
                p2_digits.append(char)
            for d,val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
                if line[i:].startswith(val):
                    p2_digits.append(str(d+1))
        # p1 += int(p1_digits[0]+p1_digits[-1])
        p2 += int(p2_digits[0]+p2_digits[-1])

    return p2


if __name__ == "__main__":
    first = solve_first(data)
    print(f'the solution for the first puzzle is: \t {first}')
    second = solve_second(data)
    print(f'the solution for the second puzzle is: \t {second}')