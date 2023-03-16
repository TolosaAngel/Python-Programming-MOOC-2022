def longest_series_of_neighbours(list):
    long_serie = 1
    longest = 1

    for i in range(len(list)-1):
        if (list[i]==(list[i+1]+1) or list[i]==(list[i+1]-1)):
            long_serie+=1

            if long_serie>longest:
                longest = long_serie 
        else:
            if long_serie>longest:
                longest = long_serie 

            long_serie = 1

    return longest


if __name__=="__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))