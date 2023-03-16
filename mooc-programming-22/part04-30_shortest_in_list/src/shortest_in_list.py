def shortest(list):
    short_length = len(list[0])
    short_str = list[0]

    for i in list:
        if len(i)<short_length:
            short_length = len(i)
            short_str = i

    return short_str

if __name__=="__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = shortest(my_list)
    print(result)

    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = shortest(my_list)
    print(result)