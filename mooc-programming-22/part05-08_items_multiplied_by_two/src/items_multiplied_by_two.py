def double_items(numbers: list):
    copy_list = numbers[:]

    for i in range(len(copy_list)):
        copy_list[i] *= 2

    return copy_list

if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)