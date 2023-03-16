def column_correct(sudoku: list, column_no: int):
    my_list = []

    for i in range(len(sudoku)):
        my_list.append(sudoku[i][column_no])

    for i in range(len(my_list)):
        if 0 <= i+1 <= 9:
            if i+1 in my_list:
                my_list.remove(i+1)

            if i+1 in my_list:
                return False
        else:
            return False

    return True

if __name__=="__main__":
    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(column_correct(sudoku, 0))
    print(column_correct(sudoku, 1))