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
    "size":""
    }



def createDirList(cmds:list, dirlist):
    for i in range(len(cmds)):
        if cmds[i] == "$ ls":
            for j in range(i+1,i+3,1):
                print(cmds[j])

    return 0

createDirList(cmds,dirlist)

### Hints:
# could use a set for this problem for a more elegant solution
# see https://www.youtube.com/watch?v=LvwsB-JpJmQ











with open(filepath, 'r') as file:  
        data = file.read()




SOP = findSOP(data)
SOM = findSOM(data)

# get answer

print("Part one")
print(SOP)

print("Part two")
print(SOM)

