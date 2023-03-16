def row_correct(sudoku: list, row_no: int):
    my_list = sorted(sudoku[row_no])

    for i in range(len(my_list)):
        if 0 <= i+1 <= 9:
            if i+1 in my_list:
                my_list.remove(i+1)

            if i+1 in my_list:
                return False
        else:
            return False

    return True  

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

def sudoku_grid_correct(sudoku: list):
    for i in range(len(sudoku)): 
        if row_correct(sudoku, i)==False:
            return False

    for i in range(len(sudoku)): 
        if column_correct(sudoku, i)==False:
            return False

    for row in range(0, len(sudoku), 3):
        for column in range(0, len(sudoku), 3):
            if block_correct(sudoku, row, column)==False:
                return False    

    return True

if __name__=="__main__":
    sudoku1 = [
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

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
        [2, 6, 7, 8, 3, 9, 5, 0, 4],
        [9, 0, 3, 5, 1, 0, 6, 0, 0],
        [0, 5, 1, 6, 0, 0, 8, 3, 9],
        [5, 1, 9, 0, 4, 6, 3, 2, 8],
        [8, 0, 2, 1, 0, 5, 7, 0, 6],
        [6, 7, 4, 3, 2, 0, 0, 0, 5],
        [0, 0, 0, 4, 5, 7, 2, 6, 3],
        [3, 2, 0, 0, 8, 0, 0, 5, 7],
        [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku2))