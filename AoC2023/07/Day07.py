import math

day = "07"

input = f"./{day}/input.txt"
test_first = f"./{day}/test_first.txt"
test_second = f"./{day}/test_second.txt"

infile = test_first
data = []

with open(infile, "r") as file:
    for line in file:
        data.append(line.strip())

def compare_hands(hand1, hand2):
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    print(f'Hands: {hand1} - {hand2}')
    def count_values(cards):
        count = {}
        for card in cards:
            count[card] = count.get(card, 0) + 1
        return count

    def has_n_of_a_kind(count_dict, n):
        print("highcard:", cards)

        return any(count == n for count in count_dict.values())

    def has_two_pairs(count_dict):
        return sum(count == 2 for count in count_dict.values()) == 2

    def is_full_house(count_dict):
        return has_n_of_a_kind(count_dict, 3) and has_n_of_a_kind(count_dict, 2)

    def get_high_card_value(cards):
        print("highcard:", cards)
        return max(values[card] for card in cards)

    def get_hand_strength(hand):
        card_values = [card[-1] for card in hand]
        count_dict = count_values(card_values)
        print("count_dict: ", count_dict)

        if is_full_house(count_dict):
            return 6, max(values[card] for card, count in count_dict.items() if count == 3)  # Full House
        elif has_n_of_a_kind(count_dict, 4):
            return 5, max(values[card] for card, count in count_dict.items() if count == 4)  # Four of a Kind
        elif has_n_of_a_kind(count_dict, 3) and has_n_of_a_kind(count_dict, 2):
            return 4, max(values[card] for card, count in count_dict.items() if count == 3)  # Three of a Kind
        elif has_two_pairs(count_dict):
            return 3, max(values[card] for card, count in count_dict.items() if count == 2)  # Two Pairs
        elif has_n_of_a_kind(count_dict, 2):
            return 2, max(values[card] for card, count in count_dict.items() if count == 2)  # One Pair
        else:
            return 1, get_high_card_value(card_values)  # High Card

    strength1, value1 = get_hand_strength(hand1)
    strength2, value2 = get_hand_strength(hand2)

    if strength1 > strength2 or (strength1 == strength2 and values[hand1[0]] > values[hand2[0]]):
        return "Hand 1 wins!"
    elif strength1 < strength2 or (strength1 == strength2 and values[hand1[0]] < values[hand2[0]]):
        return "Hand 2 wins!"
    else:
        # Hands have the same strength, compare individual cards
        for card1, card2 in zip(hand1, hand2):
            if values[card1[0]] > values[card2[0]]:
                return False # do not swap
            elif values[card1[0]] < values[card2[0]]:
                return True # swap
        print("FUUUUUUUU")
        return None

def bubblesort(arr):
    n = len(arr)
    # Traverse through all elements in the list
    for i in range(n):
        # Last i elements are already in place, so we don't need to check them
        for j in range(0, n-i-1):
            # Swap if the element found is greater according to the compare function
            if compare_hands(arr[j], arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr






def solve_first(data):
    hands = [(line.split(" ")[0], line.split(" ")[1], 0) for line in data]
    result = compare_hands("32T3K", "T55J5")
    
    # hands_srtd = bubblesort(hands)
    # result = [i*hand[2] for i, hand in enumerate(hands_srtd)]


    print(result)
    return None
    




def solve_second(data):

    
    return None





if __name__ == "__main__":
    first = solve_first(data)
    print(f'the solution for the first puzzle is: \t {first}\n')
    
    
    second = solve_second(data)
    print(f'the solution for the second puzzle is: \t {second}\n')