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
    xmax = len(grid[0])
    ymax = len(grid)
    visible = True
    if y == 0:
        print(f'checking tree at {pos} with height {grid[y][x]} - is border')
        return visible
    for ycheck in range(y,0-1,-1):
        if (x, ycheck) == pos:
            continue
        tree = grid[ycheck][x]
        print(f'checking tree at {pos} with height {grid[y][x]} against tree at {(x, ycheck)} with height {tree} - dir: N')
        if tree >= grid[y][x]:
            visible = False
            print(f'vN failed at {(x, ycheck)}')
            break
    return visible

def viewS(pos:tuple, grid:list):
    x,y = pos
    xmax = len(grid[0])
    ymax = len(grid)
    visible = True
    if y == ymax:
        print(f'checking tree at {pos} with height {grid[y][x]} - is border')
        return visible
    for ycheck in range(y,ymax,1):
        if (x, ycheck) == pos:
            continue
        tree = grid[ycheck][x]
        print(f'checking tree at {pos} with height {grid[y][x]} against tree at {(x, ycheck)} with height {tree} - dir: S')
        if tree >= grid[y][x]:
            visible = False
            print(f'vS failed at {(x, ycheck)}')
            break
    return visible

def viewE(pos:tuple, grid:list):
    x,y = pos
    xmax = len(grid[0])
    ymax = len(grid)
    visible = True
    if x == xmax:
        print(f'checking tree at {pos} with height {grid[y][x]} - is border')
        return visible
    for xcheck in range(x,xmax,1):
        if (xcheck, y) == pos:
            continue
        tree = grid[y][xcheck]
        print(f'checking tree at {pos} with height {grid[y][x]} against tree at {(xcheck, y)} with height {tree} - dir: E')
        if tree >= grid[y][x]:
            visible = False
            print(f'vE failed at {(xcheck,y)}')
            break
    return visible

def viewW(pos:tuple, grid:list):
    x,y = pos
    xmax = len(grid[0])
    ymax = len(grid)
    visible = True

    for xcheck in range(x,-1,-1):
        if (xcheck, y) == pos:
            continue
        tree = grid[y][xcheck]
        print(f'checking tree at {pos} with height {grid[y][x]} against tree at {(xcheck, y)} with height {tree} - dir: W')
        if tree >= grid[y][x]:
            visible = False
            print(f'vW failed at {(xcheck,y)}')
            break
    return visible



def view(pos:tuple, grid:list, direction:str="N"):
    x,y = pos
    xmax = len(grid[0])
    ymax = len(grid)
    visible = True
    dist = 1
    if direction == "N":
        direct = (-1,0)
    if direction == "S":
        direct = (1,0)
    if direction == "E":
        direct = (0,1)
    if direction == "W":
        direct = (-1,0)

    if x == 0 or x == xmax or y == 0 or y == ymax:
        print(f'tree at {pos} with height {grid[y][x]} is on border')
        visible = True 

    
    coords = [(nx,ny) for nx,ny in zip(pos,direct)]
    print(coords)

    for obstx,obsty in coords:
        if (obstx,obsty) == pos:
            print(f'tree at {pos} with height {grid[y][x]} is self')
            continue
        obstacle = grid[obsty][obstx]
        print(f'checking tree at {pos} with height {grid[y][x]} against tree at {(obstx, obsty)} with height {obstacle} - dir: {direction}')
        dist += 1
        if obstacle >= grid[y][x]:
            visible = False
            print(f'vW failed at {(obstx,obsty)}')
            break

    return {"direction" : direction,  "distance": dist, "free" : visible}











mat = []

for line in grid:
    l = list(line)
    height = [int(n) for n in l]
    mat.append(height)

grid = mat
for row in grid:
    print(row)


print(view((2,1),grid,direction="N"))
print(view((2,1),grid,direction="S"))
print(view((2,1),grid,direction="E"))
print(view((2,1),grid,direction="W"))





print('\n\n')


# with open(filepath, 'r') as file:  
#         lines = file.read().split("\n")[:-1]
#         grid = []       
#         for line in lines:
#             linestr = list(line)
#             height = [int(n) for n in linestr]
#             grid.append(height)

score = 0
viewscore = []

y=0
for row in grid:
    x=0
    for col in row:
        pos = (x,y)
        vN = view(pos,grid,direction="N")
        vS = view(pos,grid,direction="S")
        vE = view(pos,grid,direction="E")
        vW = view(pos,grid,direction="W")
        treescore = vN["distance"] * vS["distance"] * vE["distance"] * vW["distance"]
        viewscore.append(treescore)
        if vN["free"] or vS["free"] or vE["free"] or vW["free"]:
            score+=1
        
    y+=1


print(score)
print(max(viewscore))





#####
print(len(grid[0]), len(grid))
y=0
# position as (x,y)
result = 0
score =[]
inv = []
for row in grid:
    x=0
    for col in row:
        pos = (x,y) 
        print(f'current position: {pos}')
        vN = viewN(pos, grid)
        if vN:
            result += 1
            print(f'{pos} - {grid[y][x]} is visible from N')
            x += 1
            continue
        # print(f'for tree with height {grid[y][x]} at {pos} tree visibility is {vN} to the North')
        vS = viewS(pos, grid)
        if vS:
            result += 1
            print(f'{pos} - {grid[y][x]} is visible from S')
            x += 1
            continue
        # print(f'for tree with height {grid[y][x]} at {pos} tree visibility is {vS} to the South')
        vE = viewE(pos, grid)
        if vE:
            result += 1
            print(f'{pos} - {grid[y][x]} is visible from E')
            x += 1
            continue
        # print(f'for tree with height {grid[y][x]} at {pos} tree visibility is {vE} to the East')
        vW = viewW(pos, grid)
        if vW:
            result += 1
            print(f'{pos} - {grid[y][x]} is visible from W')
            x += 1
            continue
        # print(f'for tree with height {grid[y][x]} at {pos} tree visibility is {vW} to the West')
        # print(vN, vS, vE, vW)
        # print(f'{pos} - {grid[y][x]} is not visible')
        inv.append(pos)
        x += 1
        
    y += 1

print(result)
print(inv)

# vN = viewN((1,3), grid)
# vS = viewS((1,3), grid)
# vE = viewE((1,3), grid)
# vW = viewW((1,3), grid)
# print(grid[3][1], vN, vS, vE, vW)



p1 = result
p2 = 0

# get answer

print("Part one")
print(p1)

print("Part two")
print(p2)

