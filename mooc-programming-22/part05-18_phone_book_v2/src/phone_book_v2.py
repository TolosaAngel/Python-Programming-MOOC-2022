option = int(input("command (1 search, 2 add, 3 quit): "))
my_dictionary = {}

while option!=3:
    name = input("name: ")

    if option == 1:
        if name in my_dictionary:
            for number in my_dictionary[name]:
                print(number)
        else:
            print("no number")
    else:
        number = input("number: ")

        if name in my_dictionary:
            my_dictionary[name].append(number)
        else:
            my_dictionary[name] = [number]
        
        print("ok!")
        
    option = int(input("command (1 search, 2 add, 3 quit): "))

print("quitting...")