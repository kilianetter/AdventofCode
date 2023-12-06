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

test_2 = {
"time": [71530],
"dist": [940200]
}


data = {
"time": [59, 79, 65, 75],
"dist": [597, 1234, 1032, 1328]
}

data_2 = {
"time": [59796575],
"dist": [597123410321328]
}


def count_ways(record_time, record_dist):
    count = 0
    for speed in  range(0,record_time):
        # press_time = 1
        travel_time = record_time - speed 
        dist = travel_time * speed

        if dist > record_dist:
            count += 1
    return count


def solve_first(data):
    records = zip(data["time"],data["dist"])
    result = 0
    for  record_time, record_dist in records:
        cntr = count_ways(record_time, record_dist)
        print(f'there are {cntr} ways to beat the record\n')

        if result != 0:
            result *= cntr
        else:
            result += cntr
    return result
    




def solve_second(data):
    records = (*data["time"],*data["dist"])
    record_time, record_dist = records

    result = count_ways(record_time, record_dist)
    print(f'there are {result} ways to beat the record\n')
    
    return result





if __name__ == "__main__":
    first = solve_first(data)
    print(f'the solution for the first puzzle is: \t {first}\n')
    
    
    second = solve_second(data_2)
    print(f'the solution for the second puzzle is: \t {second}\n')