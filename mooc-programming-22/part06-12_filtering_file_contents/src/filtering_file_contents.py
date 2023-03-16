def filter_solutions():
    with open("solutions.csv") as solutions_file:
        correct_fo = "w"
        incorrect_fo = "w"

        for line in solutions_file:
            data = line.split(";")

            result = False

            if "+" in data[1]:
                operation = data[1].split("+")
                result = int(operation[0])+int(operation[1])==int(data[2])
            else:
                operation = data[1].split("-")
                result = int(operation[0])-int(operation[1])==int(data[2])

            if result:
                with open("correct.csv", correct_fo) as correct_file:
                    correct_file.write(line)
                    correct_fo = "a"
            else:
                with open("incorrect.csv", incorrect_fo) as incorrect_file:
                    incorrect_file.write(line)
                    incorrect_fo = "a"

if __name__ == "__main__":
    filter_solutions()
    filter_solutions()
    filter_solutions()