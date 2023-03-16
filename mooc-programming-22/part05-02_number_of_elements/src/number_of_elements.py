def count_matching_elements(my_matrix: list, element: int):
    c = 0

    for list in my_matrix:
        for i in list:
            if i==element:
                c+=1

    return c

if __name__=="__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))