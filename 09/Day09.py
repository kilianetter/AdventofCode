import os
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani



np.set_printoptions(linewidth=300)

filename = "input.txt"
example = "example.txt"
filepath = os.path.join(os.path.dirname(__file__), filename)
expath = os.path.join(os.path.dirname(__file__), example)
outpath = os.path.join(os.path.dirname(__file__), "movie.mp4")




# https://adventofcode.com/2022/day/6


### Hints:
# could use a set for this problem for a more elegant solution
# see https://www.youtube.com/watch?v=LvwsB-JpJmQ



def calcTailDistance(head:tuple, tail:tuple):
    x1,y1 = head
    x2,y2 = tail
    ab = (x1-x2)**2 + (y1-y2)**2
    dist = math.sqrt(ab)
    return dist

def calcTailDirection(head:tuple, tail:tuple):
    x1,y1 = head
    x2,y2 = tail
    dx = (x1-x2)
    dy = (y1-y2)
    print(f'tail must move in direction: {dx},{dy}')
    if dx > 1:
        dx = 1
    elif dx < -1:
        dx = -1
    if dy > 1:
        dy = 1
    elif dy < -1:
        dy = -1
    TH = (dx, dy)
    return TH


def getDirectionVector(d:str):
    vectors = [(0,1),(0,-1),(1,0),(-1,0)] # UDRL - switched North/South or Up/Down to flip board
    if d == "U":
        dirvect = vectors[0]
    if d == "D":
        dirvect = vectors[1]
    if d == "R":
        dirvect = vectors[2]
    if d == "L":
        dirvect = vectors[3]
    try:
        dirvect
    except NameError:
        print("travel vector undefined")
    return dirvect



def moveTail(head:tuple, tail:tuple):
    taildist = calcTailDistance(head,tail)
    taildir = calcTailDirection(head,tail)
    print(f'moving tail in dir {taildir}')
    posTail = tuple([h+t for h,t in zip(tail, taildir)])
    result.append(posTail)
    print(f'new position of Tail: {posTail}')
    return posTail


def moveSegment(n, elemList):
    head = elemList[n-1]
    tail = elemList[n]
    taildist = calcTailDistance(head,tail)
    taildir = calcTailDirection(head,tail)
    if taildist > math.sqrt(2):
        print(f'moving element {n} in dir {taildir}')
        posElem = tuple([h+t for h,t in zip(tail, taildir)])
        print(f'moved element to {posElem}')
    else:
        posElem = tail
        print(f'Element adjacent to previous Element')
    print(f'new position of element {n}: {posElem}')
    if n == len(elemList)-1:
        result.append(posElem)
    return posElem



def printBoard(head:tuple, tail:tuple):
    board = np.zeros([500,500])
    board[head[1], head[0]] = "1"
    board[tail[1], tail[0]] = "2"
    print(np.flipud(board))


def printBoard2(segments:list, show:bool=False):
    board = np.zeros([300,300])
    board[:] = np.nan
    n = 0
    for seg in segments:
        x,y = seg
        board[y][x] = n
        n+=1
    mat = np.flipud(board)
    if show == True:
        print(mat)
    return mat


# def moveRope(head:tuple, tail:tuple, cmd:str):
#     traveldir = cmd.split(" ")[0]
#     traveldist = int(cmd.split(" ")[1])
#     steps = int(cmd.split(" ")[1])
#     dirvect = getDirectionVector(traveldir)
#     print(traveldir, traveldist, dirvect)
#     travelvect = dirvect # tuple([traveldist*elem for elem in dirvect])
#     posHead = head
#     posTail = tail
#     result.append(posTail)
#     ahead = 0
#     for step in range(traveldist):
#         print(f'old position of head: {posHead}')
#         posHead = tuple([h+t for h,t in zip(posHead, travelvect)])
#         print(f'new position of head: {posHead}')
#         printBoard(posHead, posTail)
#         if calcTailDistance(posHead, posTail) > math.sqrt(2):
#             posTail = moveTail(posHead, posTail)
#             print(f'moved Tail to {posTail}')
#         else:
#             print(f'Tail adjacent to Head')
#         printBoard(posHead, posTail)
#         print(f'end of step')
#         print(f'\n')
#     return [posHead, posTail]

def moveRope(segmentList:list, cmd:str):
    traveldir = cmd.split(" ")[0]
    traveldist = int(cmd.split(" ")[1])
    steps = int(cmd.split(" ")[1])
    travelvect = getDirectionVector(traveldir) # for single step: tuple([traveldist*elem for elem in dirvect])
    
    for step in range(traveldist): 
        n = 0
        for segment in segmentList:
            if n == 0:
                ### move head (segment 0)
                print(f'old position of head: {segment}')
                segmentPos = tuple([h+t for h,t in zip(segment, travelvect)])
                print(f'new position of head: {segment}')
                
            else:
                ### move segments 1-9 
                segmentPos = moveSegment(n, segmentList)
            
            segmentList[n] = segmentPos
            n += 1

        print(f'end of step')
        print(f'\n')
        matrixList.append(printBoard2(segmentList, show=False))
    print(segmentList)
    printBoard2(segmentList)
    return segmentList



with open(filepath, 'r') as file:  
        instructions = file.readlines()   


# initial state
ahead = 0
head = (0,0)
tail = (0,0)
ropelength = 10
segmentList = [(0,0) for n in range(ropelength)]
print(segmentList)




result = []
matrixList = []
for cmd in instructions:
    segmentList = moveRope(segmentList, cmd)
    


print(type(matrixList))
ims = []

fig, ax = plt.subplots()
for mat in matrixList:
    im = ax.matshow(mat, animated=True)
    ims.append([im])


anim = ani.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)
anim.save(outpath)

# plt.show()

print(len(set(result)))


p1 = len(set(result))
p2 = len(set(result))

# get answer

print("Part one")
print(p1)

print("Part two")
print(p2)

