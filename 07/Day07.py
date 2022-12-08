import os
import math
filename = "input.txt"
example = "example.txt"
filepath = os.path.join(os.path.dirname(__file__), filename)


# https://adventofcode.com/2022/day/6


instructions = """
$ cd /
$ ls
    dir a
    14848514 b.txt
    8504156 c.dat
    dir d
    $ cd a
    $ ls
        dir e
        29116 f
        2557 g
        62596 h.lst
        $ cd e
            $ ls
            584 i
            $ cd ..
        $ cd ..
    $ cd d
        $ ls
        4060174 j
        8033020 d.log
        5626152 d.ext
        7214296 k
"""

cmds = [line for line in instructions.split("\n")]
print(cmds)

root = []
dirlist = []
dirProp = {
    "name":"",
    "size":"",
    "content": []
    }

def dirdict(cmds:list, index:int):
    return 0
    



def createDirList(cmds:list, dirlist):
    for i in range(len(cmds)):
        if cmds[i].startswith("$ cd") and cmds[i] != "$ cd ..":
            
            directory = dirProp
            directory["name"] = cmds[i].split(" ")[2]
            
        if cmds[i] != "$ cd .."
            print(directory)


    return 0

createDirList(cmds,dirlist)

### Hints:
# could use a set for this problem for a more elegant solution
# see https://www.youtube.com/watch?v=LvwsB-JpJmQ











with open(filepath, 'r') as file:  
        data = file.read()



p1 = 0
p2 = 0

# get answer

print("Part one")
print(p1)

print("Part two")
print(p2)

