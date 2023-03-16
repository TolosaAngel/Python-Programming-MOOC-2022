from string import *
from random import sample, choice

def generate_strong_password(length: int, nums: bool, special_char: bool):
    characters = ascii_lowercase

    my_list = []
    my_list.append(choice(characters))

    if nums and special_char:
        characters += digits + "!?=+-()#"

        my_list.append(choice(digits))
        my_list.append(choice("!?=+-()#"))

        my_list += sample(characters, length-3)
    elif nums and not special_char:
        characters += digits

        my_list.append(choice(digits))
        
        my_list += sample(characters, length-2)
    elif not nums and special_char:
        characters += "!?=+-()#"

        my_list.append(choice("!?=+-()#"))

        my_list += sample(characters, length-2)
    else:
        my_list += sample(characters, length-1)

    password = ""

    for element in my_list: password+=element

    return password

if __name__ == "__main__":
    for i in range(10):
        print(generate_strong_password(8, True, True))