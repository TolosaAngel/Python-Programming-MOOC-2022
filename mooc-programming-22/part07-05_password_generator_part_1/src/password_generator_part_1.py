from string import ascii_lowercase
from random import sample

def generate_password(length: int):
    my_list = sample(ascii_lowercase, length)
    
    password = ""

    for element in my_list: password+=element

    return password

if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8))