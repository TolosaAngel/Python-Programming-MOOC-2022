def most_common_character(word):
    position = 0
    c = 0

    for i in range(len(word)):
        if word.count(word[i])>c:
            c = word.count(word[i])
            position = i

    return word[position]

if __name__=="__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))