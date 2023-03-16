option = int(input("command (1 search, 2 add, 3 quit): "))
my_dictionary = {}

while option!=3:
    name = input("name: ")

    if option == 1:
        if name in my_dictionary:
            print(my_dictionary[name])
        else:
            print("no number")
    else:
        number = input("number: ")
        my_dictionary[name] = number
        print("ok!")


    option = int(input("command (1 search, 2 add, 3 quit): "))

print("quitting...")