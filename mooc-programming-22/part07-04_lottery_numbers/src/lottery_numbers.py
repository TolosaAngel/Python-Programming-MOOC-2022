from random import sample

def lottery_numbers(amount: int, lower: int, upper: int):
    my_list = sample(list(range(lower, upper)), amount)
    my_list.sort()
    
    return my_list

if __name__ == "__main__":
    for number in lottery_numbers(7, 1, 40):
        print(number)