import os
import math
import numpy as np
filename = "input.txt"
example = "example.txt"
filepath = os.path.join(os.path.dirname(__file__), filename)


# https://adventofcode.com/2022/day/10



instructions = []
with open(filepath, 'r') as file:  
        # instructions = file.read()
        for line in file.readlines():
            instructions.append(line.strip())


print(instructions)
print(len(instructions))




def getInstruction(index:int):
    return instructions[i]

def checkCycle(cycle:int):
    foo=cycle-20
    if cycle == 20 :
        return True
    if cycle > 20 and (cycle-20)%40 == 0:
        return True
    else:
        return False


### initial state
cyc = 0
reg = 1
sig = 0
regList = []
sigList = []
i = -1 # why?
on = True

while on == True:
    try :
        cmd = getInstruction(i)
        instr, val = cmd.split(" ")
    except ValueError:
        cmd = getInstruction(i)
        instr = cmd.split(" ")
    except:
        print(f'instructions have ended')
        on = False
        break
    cyc +=1
    i += 1
    if instr == "noop":
        pass
    if checkCycle(cyc):
        sig = cyc * reg
        print(f' #{cyc} - {reg},{val} - sig: {sig}' )
        sigList.append(sig)
    regList.append(reg)

    if instr == "addx":
        cyc += 1
        if checkCycle(cyc):
            sig = cyc * reg
            print(f' #{cyc} - {reg},{val} - sig: {sig}' )
            sigList.append(sig)
        reg += int(val)
        regList.append(reg)
    
    print (f'cycle #{cyc}')

print(regList)

lines = 6
pixels = 40

crt = [[] for _ in range(lines)]
y=0
for line in crt:
    print(f'===== Line {y} =====')
    for px in range(pixels):
        i = (40*y)+px      
        print(px, i, [n for n in range(regList[i]-1,regList[i]+2)])
        if px in range(regList[i]-1,regList[i]+2):
            char = "#"
        else:
            char = " "
        line.append(char)
        print(f'draw pixel {px} for cycle {i} - {char}')
        print("".join(line))
    crt[y] = line
    y+=1



p1 = sum(sigList[0:6])
p2 = 0

# get answer

print("Part one")
print(p1)


for line in crt:
    print("".join(line))

print("Part two")
print(p2)

