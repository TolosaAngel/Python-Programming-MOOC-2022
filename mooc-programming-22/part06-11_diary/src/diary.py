print("1 - add an entry, 2 - read entries, 0 - quit")
option = int(input("Function: "))

while option!=0:
    if option==1:
        entry = input("Diary entry: ")

        with open("diary.txt", "a") as my_file:
            my_file.write(f"{entry}\n")

        print("Diary saved\n")

    if option==2:
        print("Entries:")

        with open("diary.txt") as my_file:
            for line in my_file:
                line = line.replace("\n", "")
                print(line)

    print("1 - add an entry, 2 - read entries, 0 - quit")
    option = int(input("Function: "))

print("Bye now!")