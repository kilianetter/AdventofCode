
import os
import re



input = "AoC2024/03/input.txt"
test = "AoC2024/03/test_first.txt"
test_second = "AoC2024/03/test_second.txt"

infile = input

data = []
a = []
b = []

with open(infile, "r") as file:
    for line in file:
        data.append(line.strip())
    data = data[0]

   
def solve_first(data):
    result = 0
    expr = re.findall("mul[(]\d+,\d+[)]", data)
    for occ in expr:
        print(occ)
        nums = re.findall("\d+", occ)
        print(nums)
        result += int(nums[0])  * int(nums[1])
    return result


def solve_second(data):
    result = 0
    data = re.sub("don't\(\).*?do\(\)","", data)
    print(data)
    expr = re.findall("mul\(\d+,\d+\)", data)
    for occ in expr:
        print(occ)
        nums = re.findall("\d+", occ)
        print(nums)
        result += int(nums[0])  * int(nums[1])
    return result


if __name__ == "__main__":
    print(data)
    first = solve_first(data)
    print(f'the solution for the first puzzle is: \t {first}')
    second = solve_second(data)
    print(f'the solution for the second puzzle is: \t {second}')