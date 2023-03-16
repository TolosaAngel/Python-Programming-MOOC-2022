def range_of_list(list):
    return max(list)-min(list)

if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = range_of_list(my_list)
    print("The range of the list is", result)

    my_list = [1, 2, 3, 4, 5]
    result = range_of_list(my_list)
    print("The range of the list is", result)