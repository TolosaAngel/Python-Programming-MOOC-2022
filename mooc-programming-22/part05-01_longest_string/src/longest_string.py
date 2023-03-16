def longest(strings: list):
    max_string = 1

    for i in range(len(strings)):
        if len(strings[i]) > len(strings[max_string]):
            max_string = i

    return strings[max_string]

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))