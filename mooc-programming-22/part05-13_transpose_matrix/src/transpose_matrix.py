from copy import copy, deepcopy

def transpose(matrix: list):
    new_matrix = deepcopy(matrix)

    for row in range(len(matrix)):
        for column in range(len(matrix)):
            matrix[column][row] = new_matrix[row][column]

if __name__=="__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(matrix)
    print()
    transpose(matrix)
    print(matrix)