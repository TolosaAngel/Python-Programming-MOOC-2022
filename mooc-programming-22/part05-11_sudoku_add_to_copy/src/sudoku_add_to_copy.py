from copy import copy, deepcopy

def print_sudoku(sudoku: list):
    c = 0
    c2 = 0

    for row in range(len(sudoku)):
        for column in range(len(sudoku)):
            if sudoku[row][column]==0:
                print("_ ", end="")
            else:
                print(f"{sudoku[row][column]} ", end="")

            c+=1

            if c==3:
                print(" ", end="")
                c = 0

        print()
        c2+=1

        if c2==3:
            print()
            c2 = 0

def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no] = number

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    grid_copy = deepcopy(sudoku)

    add_number(grid_copy, row_no, column_no, number)

    return grid_copy

if __name__=="__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)