def distinct_numbers(list):
    new_list = []

    for i in list:
        if not (i in new_list):
            new_list.append(i)

    new_list.sort()

    return new_list

if __name__=="__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list))