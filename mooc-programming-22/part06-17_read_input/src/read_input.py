def read_input(message: str, min: int, max: int):
    while True:
        try:
            number = int(input(message))

            if min<=number<=max:
                return number
        except ValueError:
            pass

        print(f"You must type in an integer between {min} and {max}")

if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)