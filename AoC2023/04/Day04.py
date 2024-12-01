
day = "04"

input = f"./{day}/input.txt"
test_first = f"./{day}/test_first.txt"
test_second = f"./{day}/test_second.txt"

infile = input
data = []



with open(infile, "r") as file:
    for line in file:
        data.append(line.strip())


def check_card(card):
    win_nums = card[0]
    nums = card[1]
    winners = win_nums.intersection(nums)
    return winners


def points_on_card(winners):
    if len(winners) == 0:
        points = 0
    else:
        points = 1 * (2**(len(winners)-1))
    return points



def copy_card(card_num):
    pass


def solve_first(data):
    points = 0
    n = 0
    cards = []
    for line in data:
        winning_nums, nums = line.split("|")
        card_num, win_nums = winning_nums.split(":")
        win = set(win_nums.replace("  ", " 0").split(" ")[1:-1])
        num = set(nums.replace("  ", " 0").split(" ")[1:])
        count=1
        cards.append([win, num])
    for card in cards:
        winners = check_card(card)
        points += points_on_card(winners)
        n+=1
        print(f'{n} yields {points_on_card(winners)} Points')
    return points




def solve_second(data):
    cards = []
    copycount = []
    for line in data:
        winning_nums, nums = line.split("|")
        card_num, win_nums = winning_nums.split(":")
        win = set(win_nums.replace("  ", " 0").split(" ")[1:-1])
        num = set(nums.replace("  ", " 0").split(" ")[1:])
        count=1
        cards.append([win, num])
        copycount.append(1)
    i=0
    cardindex = i+1
    for card in cards:
        cardindex = i+1
        winners = len(check_card(card))
        
        print(f'#{i:02} - card: {cardindex} - count: {copycount[i]}')
        print(f'number of winning numbers: {winners}, number of cards: {copycount[i]}')
        print(f'you win {winners} cards')
        
        if winners == 0:
            print(f'no copys added for card {cardindex}')
        else:                
            winning_range = range(i+1,i+winners+1)
            # print("WR: ", winning_range)
            winning_index = [x for x in winning_range]
            # print("WI: ", winning_index)
            for x in winning_index:
                print(f'adding {copycount[x]} copys to {x}')
                copycount[x] += copycount[i]
        
        print(copycount, "\n")
        i+=1
    return sum(copycount)

        
        



if __name__ == "__main__":
    first = solve_first(data)
    print(f'the solution for the first puzzle is: \t {first}\n')
    
    
    second = solve_second(data)
    print(f'the solution for the second puzzle is: \t {second}\n')