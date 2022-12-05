import os
import math
filename = "input.txt"
example = "example.txt"
filepath = os.path.join(os.path.dirname(__file__), filename)


# https://adventofcode.com/2022/day/5

foo = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 
"""

x = 0
y = 0

x_size = 3
y_size = 3

crates = []
lines = 0
boxboxbox =[]
cmdlist = []

with open(filepath, 'r') as file:  
    for line in file.readlines():
        lines += 1
        cratesPerLine = (len(line)+1)//4
        if line == "" or cratesPerLine == 0:
            break
        # make empty crates 
        while len(boxboxbox) < cratesPerLine:
            boxboxbox.append([])
        # fill crates, when should be filled
        for i in range(len(boxboxbox)):
            ch = line[1+4*i]
            if ch != ' ' and 'A'<=ch<='Z':
                boxboxbox[i].append(ch)


boxboxbox = [list(reversed(elem)) for elem in boxboxbox]


with open(filepath, 'r') as file:  
    for line in file.readlines()[lines:]:
        ints = [int(i) for i in line.strip().split() if i.isdigit()]

        tup = (ints[0],ints[1],ints[2]) # (amount, stack, target)
        cmdlist.append(tup)


def printShelf(shelf:list):
    i=0
    for col in shelf:
        i += 1
        print(f'{i} - {col}')
    print("\n")


def execute(shelf:list, cmd:tuple, single:bool=True):
    amount, stack, target = cmd
    crates = shelf[stack-1][-amount:]
    del shelf[stack-1][-amount:]
    if single == True:
        crates = list(reversed(crates))
    shelf[target-1] = shelf[target-1] + crates
    return shelf



n=0
print(f'#-/- - initial state')
printShelf(boxboxbox)  
for cmd in cmdlist:
    amount, stack, target = cmd
    print(f'#{n} - taking top {amount} from stack {stack} to {target} --- {cmd}')
    boxboxbox = execute(boxboxbox, cmd, single=False)
    print(f'new shelf:')
    printShelf(boxboxbox)  
    n += 1  



# get answer
p1 = "".join([col[-1] for col in boxboxbox])

p2 = "".join([col[-1] for col in boxboxbox])

# set single to True
print("Part one")
print(p1)

# set single to False
print("Part two")
print(p2)

