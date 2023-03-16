def histogram(word):
    my_dictionary = {}

    for letter in range(len(word)):
        if word[letter] in my_dictionary:
            my_dictionary[word[letter]] += "*"
        else:
            my_dictionary[word[letter]] = "*"

    for key, items in my_dictionary.items():
        print(key + " " + items)

if __name__ == "__main__":
    histogram("abba")
    print()
    histogram("statistically")