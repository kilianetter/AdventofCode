import numpy as np

day = "03"

input = f"D:/Code/{day}/input.txt"
input1 = f"D:/Code/{day}/input1.txt"
test_first = f"D:/Code/{day}/test_first.txt"
test_second = f"D:/Code/{day}/test_second.txt"

infile = test_second
data = []

with open(infile, "r") as file:
    for line in file:
        # changed to unpack string to list
        data.append([*line.strip()])

def find_symbols(data):
    data = set([val for line in data for val in line])
    symbols = set()
    for elem in data:
        if not elem.isdigit() and elem != ".":
            symbols.add(elem)
    print(f'symbols: {symbols}')
    return symbols


def check_neighbors(data, loc:tuple):
    directions = {"N": (-1,0),
                  "NE": (-1,1),
                  "E": (1,0),
                  "SE": (1,1),
                  "S": (0,1),
                  "SW": (1,-1),
                  "W": (0,-1),
                  "NW": (-1,-1)}
    num_loc = []
    for key,vect in directions.items():
        check_loc = tuple(a + b for a,b in zip(loc, vect))
        if check_loc[1] < 0 or check_loc[1] > len(data[1])-1:
            print(f'looking {key} at {check_loc} -invalid x')
            continue
        if check_loc[0] < 0 or check_loc[0] > len(data[0])-1:
            print(f'looking {key} at {check_loc} - invalid y')
            continue
        if data[check_loc[0]][check_loc[1]].isdigit():
            print(f'looking {key} at {check_loc} - is a digit')
            # print(f'{check_loc} is a digit')
            num_loc.append(check_loc)
        else:
            print(f'looking {key} at {check_loc} - is not a digit')
            continue
    return num_loc
    
    
    

def get_number(data, loc:tuple):
    # go left
    num_loc = list(loc)
    number = []
    while num_loc[1] >= 0:
        # print("left", num_loc)
        if data[num_loc[0]][num_loc[1]-1].isdigit():
            num_loc[1] -= 1
        else:
            break
    # go right
    while num_loc[1] <=  len(data[0])-1:
        # print("right", num_loc)
        # if data[num_loc[0]][num_loc[1]] != ".":
        if data[num_loc[0]][num_loc[1]].isdigit():
            digit = data[num_loc[0]][num_loc[1]]
            # print(digit)
            number.append(digit)
            num_loc[1] += 1
        else:
            # number = ["0","0"]
            break        
    return int(''.join(number))




def solve_first(data):
    result = []
    symbols = find_symbols(data)
    sym_coords = []
    data = np.array(data)
    print(data)
    for symbol in symbols:
        sym_index = np.where(data == symbol)
        sym_coord = list(zip(sym_index[0], sym_index[1]))
        print(f'looking for symbol {symbol} - found {len(sym_coord)} at {sym_coord}')
        sym_coords.append(sym_coord)

    sym_coords = [item for sublist in sym_coords for item in sublist]
    print(f'symbols found at: {sym_coords}')

    for s_coord in sym_coords:
        print(s_coord)
        neighbor_coords = check_neighbors(data, s_coord)
        print(f'neighbors to check for {s_coord}: {neighbor_coords}')
        nums = []
        for n_coord in neighbor_coords:
            nums.append(get_number(data, n_coord))
        print(f'number found: {list(set(nums))}\n')   
        result.append(list(set(nums)))
    result = [item for sublist in result for item in sublist]
    print(result)
    return sum(result)



def solve_second(data):
    pass


if __name__ == "__main__":
    first = solve_first(data)
    print(f'the solution for the first puzzle is: \t {first}')
    
    
    second = solve_second(data)
    print(f'the solution for the second puzzle is: \t {second}')