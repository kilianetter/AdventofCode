import os
import math
filename = "input.txt"
filepath = os.path.join(os.path.dirname(__file__), filename)

# https://adventofcode.com/2022/day/2

score = []

# Rock Paper Scissors
me = ['X','Y','Z']
opp =  ['A','B','C']

win = ['AY','BZ','CX']
draw = ['AX','BY', 'CZ']


with open(filepath, 'r') as file:  
    for line in file.readlines():
        round = line.strip().replace(" ", "")
        if round in win:
            s = me.index(round[1]) + 1 + 6
            score.append(s)
        elif round in draw:
            s = me.index(round[1]) + 1 + 3
            score.append(s)
        else:
            s = me.index(round[1]) + 1 + 0
            score.append(s)
        # print(f'{round} - {s}')




print("Part one")
print(sum(score))

# lose, draw, win
me = ['X','Y','Z']
# Rock Paper Scissors
opp =  ['A','B','C']

score = []

with open(filepath, 'r') as file:  
    for line in file.readlines():
        round = line.strip().replace(" ", "")
        if round[1] == 'X':
            print('lose!')
            print(f'opp threw {round[0]} -  you need {opp[opp.index(round[0])-1]}')
            needed = opp[opp.index(round[0])-1]
            s = opp.index(opp[opp.index(needed)]) + 1 + 0
        elif round[1] == 'Y':
            print('draw!')
            print(f'opp threw {round[0]} -  you need {opp[opp.index(round[0])]}')
            needed = opp[opp.index(round[0])]
            s = opp.index(opp[opp.index(needed)]) + 1 + 3
            
        elif round[1] == 'Z':
            print('win!')
            try:
                print(f'opp threw {round[0]} -  you need {opp[opp.index(round[0])+1]}')
                needed = opp[opp.index(round[0])+1]
            except IndexError:
                print(f'opp threw {round[0]} -  you need {opp[0]}')
                needed = opp[0]

            s = opp.index(opp[opp.index(needed)]) + 1 + 6
        print(s)
        score.append(s)
        #print(f'{round} - {s}')

print("Part two")
print(sum(score))

