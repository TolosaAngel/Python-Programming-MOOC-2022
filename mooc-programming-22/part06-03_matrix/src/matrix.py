def row_sums():
    sums = []

    with open("matrix.txt") as my_file:
        for line in my_file:
            sum_of_values = 0
            data = line.split(",")

            for value in data:
                sum_of_values += int(value)

            sums.append(sum_of_values)

    return sums

def matrix_sum():
    result = 0
    sums = row_sums()

    for element in sums:
        result += element

    return result

def matrix_max():
    first_element = True
    max_element = 0

    with open("matrix.txt") as my_file:
        for line in my_file:
            data = line.split(",")

            for value in data:
                if first_element:
                    max_element = int(value)
                    first_element = False
                elif int(value)>max_element:
                    max_element = int(value)
        
        return max_element 

if __name__ == "__main__":
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())
