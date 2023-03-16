def block_correct(sudoku: list, row_no: int, column_no: int):
    my_list = []

    for row in range(row_no, row_no+3):
        for column in range(column_no, column_no+3):
            if 0 <= sudoku[row][column] <= 9 :
                if sudoku[row][column] in my_list and sudoku[row][column] != 0:
                    return False
                else:
                    my_list.append(sudoku[row][column])
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

    print(block_correct(sudoku, 0, 0))
    print(block_correct(sudoku, 1, 2))