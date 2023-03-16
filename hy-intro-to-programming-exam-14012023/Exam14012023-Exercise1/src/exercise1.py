result = 0
print(result)

user_input = input("Type in a calculation or quit: ")

while user_input!="quit":
    operation = user_input[0]
    num = int(user_input[1:])

    if operation=='+':
        result += num
    else:
        result -= num

    print(result)
    user_input = input("Type in a calculation or quit: ")