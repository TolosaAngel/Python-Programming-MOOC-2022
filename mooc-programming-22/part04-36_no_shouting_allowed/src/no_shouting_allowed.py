def no_shouting(list):
    new_list = []

    for i in list:
        if not(i.isupper()):
            new_list.append(i)

    return new_list

if __name__=="__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)