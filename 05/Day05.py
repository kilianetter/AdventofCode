
day = "05"

input = f"./{day}/input.txt"
test_first = f"./{day}/test_first.txt"
test_second = f"./{day}/test_second.txt"

infile = test_first
data = []



with open(infile, "r") as file:
    data = file.read()

def parse_almanac(almanac):
    maps = almanac.split('\n')
    return maps



def solve_first(data):
    almanac = data
    maps = parse_almanac(almanac)
    seed = maps.pop(0)
    i = 0
    for elem in maps:
        if elem == '':
            maps.pop(i)
        i += 1

            
    print(seed)
    print(maps)

    result = None
    return result
    




def solve_second(data):
    pass





if __name__ == "__main__":
    first = solve_first(data)
    print(f'the solution for the first puzzle is: \t {first}\n')
    
    
    second = solve_second(data)
    print(f'the solution for the second puzzle is: \t {second}\n')