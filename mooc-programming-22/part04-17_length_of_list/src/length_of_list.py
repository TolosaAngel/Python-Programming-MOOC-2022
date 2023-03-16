def length(list):
    return len(list)

if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = length(my_list)
    print("The length is", result)

    my_list = [1, 2, 3, 4, 5]
    result = length(my_list)
    print("The length is", result)

    result = length([1, 1, 1, 1])
    print("The length is", result)