def most_common_words(filename: str, lower_limit: int):
    with open(filename) as my_file:
        file_content = my_file.read()
        file_content = file_content.split()

        my_dict = {}

        for word in file_content:
            word = "".join([letter for letter in word if letter not in "!?:,."])

            if word not in my_dict:
                my_dict[word] = 0
            
            my_dict[word] += 1

    return {word: my_dict[word] for word in my_dict if my_dict[word]>=lower_limit}

if __name__ == "__main__":
    print(most_common_words("comprehensions.txt", 3))