import os
import math
filename = "input.txt"
example = "example.txt"
filepath = os.path.join(os.path.dirname(__file__), filename)


# https://adventofcode.com/2022/day/6


treegrid = """30373
25512
65332
33549
35390"""


### Hints:
# could use a set for this problem for a more elegant solution
# see https://www.youtube.com/watch?v=LvwsB-JpJmQ

grid = list(treegrid.split("\n"))
print(grid)




def viewN(pos:tuple, grid:list):
    x,y = pos
    xmax = len(grid[0])-1
    ymax = len(grid)-1
    visible = True
    if y == 0:
        return visible
    for ycheck in range(y,0,-1):
        tree = grid[ycheck][x]
        print(f'checking tree at {pos} with height {grid[y][x]} against tree at {(x, ycheck)} with height {tree} - dir: N')
        if tree > grid[y][x]:
            visible = False
            print(f'vN failed at {(x, ycheck)}')
            break
    return visible

def viewS(pos:tuple, grid:list):
    x,y = pos
    xmax = len(grid[0])-1
    ymax = len(grid)-1
    visible = True
    if y == ymax:
        return visible
    for ycheck in range(y,ymax,1):
        if (x, ycheck) == pos:
            continue
        tree = grid[ycheck][x]
        print(f'checking tree at {pos} with height {grid[y][x]} against tree at {(x, ycheck)} with height {tree} - dir: S')
        if tree > grid[y][x]:
            visible = False
            print(f'vS failed at {(x, ycheck)}')
            break
    return visible

def viewEW(pos:tuple, grid:list):
    x,y = pos
    if grid[y][x] > min(grid[y]):
        return True
    else:
        return False




mat = []

for line in grid:
    l = list(line)
    height = [int(n) for n in l]
    mat.append(height)

grid = mat
for row in grid:
    print(row)

print('\n\n')

result = 0

y=0
# position as (x,y)

for row in grid:
    x=0
    for col in row:
        pos = (x,y) 
        print(f'current position: {pos}')
        vN = viewN(pos, grid)
        print(f'for tree with height {grid[y][x]} at {pos} tree visibility is {vN} to the North')
        vS = viewS(pos, grid)
        print(f'for tree with height {grid[y][x]} at {pos} tree visibility is {vS} to the South')
        vEW = viewEW(pos, grid)
        print('\n')
        x += 1
        if vN or vS or vEW:
            result += 1
    y += 1


print(result)

vN = viewN((2,3), grid)
vS = viewS((2,3), grid)
vEW = viewEW(pos, grid)
print(grid[3][2], vN, vS, vEW)


with open(filepath, 'r') as file:  
        data = file.read()




p1 = 0
p2 = 0

# get answer

print("Part one")
print(p1)

print("Part two")
print(p2)

