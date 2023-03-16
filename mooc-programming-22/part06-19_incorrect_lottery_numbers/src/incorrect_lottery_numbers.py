def filter_incorrect():
    open('correct_numbers.csv', 'w').close()

    with open("lottery_numbers.csv") as lottery_nums:
        for line in lottery_nums:
            line = line.replace("\n", "")
            data = line.split(";")
            digits = data[1].split(",")

            filter = True

            if data[0][data[0].find(" ")+1:].isdigit() and len(digits)==7:
                for i in range(0,len(digits)):
                    if digits[i].isdigit():      
                        for j in range(i+1,len(digits)):
                            if int(digits[i])<1 or int(digits[i])>39 or digits[i]==digits[j]:
                                filter = False
                    else:
                        filter = False
            else:
                filter = False

            if filter:
                with open("correct_numbers.csv", "a") as correct_numbers:
                    correct_numbers.write(f"{line}\n")

if __name__ == "__main__":
    filter_incorrect()