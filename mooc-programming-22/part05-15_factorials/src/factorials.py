def factorials(n: int):
    my_dictionary = {}
    
    for num in range(1, n+1):
        if num==1:
            my_dictionary[1] = 1
        else:
            my_dictionary[num] = my_dictionary[num-1]*num

    return my_dictionary

if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])