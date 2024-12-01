import numpy as np

day = "02"

input = f"D:/Code/{day}/input.txt"
test_first = f"D:/Code/{day}/test_first.txt"
test_second = f"D:/Code/{day}/test_second.txt"

infile = input
data = []

with open(infile, "r") as file:
    for line in file:
        data.append(line.strip())


def check_hand(hand):
    '''
    checks one hand 
    returns maximum number of each colored cube in hand
    '''
    #colors = ["red","green","blue"]
    # print(f'hand to check: {hand}')
    max_colors_in_hand = {"red":0, "green":0, "blue":0}
    draws = hand
    for draw in draws:
        num, col = draw.split(" ")
        if max_colors_in_hand[col] < int(num):
            max_colors_in_hand[col] = int(num)
    # print(f'max cubes in hand are {max_colors_in_hand}')
    return max_colors_in_hand



def solve_first(data):
    cubes = {"red":12, "green":13,"blue":14}
    games = []
    invalid_games = []
    for line in data:
        # Split game #
        game = line.split(": ")[0].split(" ")[1].strip()
        # split cubes per hand
        hands = line.split(":")[1].split(";")
        hands = [hand.strip().replace(", ", ",").split(",") for hand in hands]
        # check each hand
        for hand in hands:
            max_cubes_in_hand = check_hand(hand)
            result = {key: max_cubes_in_hand.get(key, 0) - cubes.get(key, 0) for key in set(max_cubes_in_hand) | set(cubes)}
            if all(value <= 0 for value in result.values()):
                games.append(int(game))
            else:
                invalid_games.append(int(game))
                continue
        ### better: only check invalid games and delete them them from range(1-len)
        valid_games = set(games)-set(invalid_games)
    return sum(valid_games)
    

def solve_second(data):
    cubes = {"red":12, "green":13,"blue":14}
    games = []
    power = 0
    for line in data:
        # Split game #
        game = line.split(": ")[0].split(" ")[1].strip()
        # split cubes per hand
        hands = line.split(":")[1].split(";")
        hands = [hand.strip().replace(", ", ",").split(",") for hand in hands]

        # check each hand
        handpower = []
        for hand in hands:
            max_cubes_in_hand = check_hand(hand)
            handpower.append(list(max_cubes_in_hand.values()))
        
        handpower = np.array(handpower).max(axis=0)
        power += handpower[0] * handpower[1] * handpower[2]
    
    return power


if __name__ == "__main__":
    first = solve_first(data)
    print(f'the solution for the first puzzle is: \t {first}')
    
    
    second = solve_second(data)
    print(f'the solution for the second puzzle is: \t {second}')