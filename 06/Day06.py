import math

day = "06"

input = f"./{day}/input.txt"
test_first = f"./{day}/test_first.txt"
test_second = f"./{day}/test_second.txt"

infile = test_first
data = []

with open(infile, "r") as file:
    for line in file:
        data.append(line.strip())

with open(infile, "r") as file:
    data = file.read()

test = {
"time": [7, 15, 30],
"dist": [9, 40, 200]
}


data = {
"time": [59, 79, 65, 75],
"dist": [597, 1234, 1032, 1328]
}

data_2 = {
"time": [59796575],
"dist": [597123410321328]
}


def solve_first(data):
    records = zip(data["time"],data["dist"])
    result = 0
    for  record_time, record_dist in records:
        # record_time = data["time"][0]
        # record_dist = data["dist"][0]
        speed = 0
        count = 0
        for press_time in  range(0,record_time):
            # press_time = 1
            travel_time = record_time - press_time

            speed = press_time 
            dist = travel_time * speed
            if dist <= record_dist:
                continue

            count += 1
            print(f'button press time: {press_time} ms')
            print(f'distance traveled: {dist} mm')
        print(f'there are {count} ways to beat the record\n')

        if result != 0:
            result *= count
        else:
            result += count
    return result
    




def solve_second(data):
    time = 597123410321328 / 59796575
    print(math.floor(time))

    
    pass





if __name__ == "__main__":
    first = solve_first(test)
    print(f'the solution for the first puzzle is: \t {first}\n')
    
    
    second = solve_second(data)
    print(f'the solution for the second puzzle is: \t {second}\n')