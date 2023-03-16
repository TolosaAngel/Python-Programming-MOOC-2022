def mean(list):
    return sum(list)/len(list)

if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print("mean value is", result)

    my_list = [1, 2, 3, 4, 5]
    result = mean(my_list)
    print("mean value is", result)