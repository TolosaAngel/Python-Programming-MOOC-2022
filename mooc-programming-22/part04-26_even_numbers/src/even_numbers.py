def even_numbers(list):
    new_list = []

    for i in list:
        if i%2==0:
            new_list.append(i)

    return new_list

if __name__=="__main__":
    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)
    
    new_list = even_numbers(list((1, 3, 5, 7, 9, 2, 4, 6, 8, 10)))
    print("original", list((1, 3, 5, 7, 9, 2, 4, 6, 8, 10)))
    print("new", new_list)