print("1 - Add word, 2 - Search, 3 - Quit")
func = int(input("Function: "))

while func!=3:
    if func==1:
        word_fin = input("The word in Finnish: ")
        word_eng = input("The word in English: ")

        with open("dictionary.txt", "a") as dictionary:
            dictionary.write(f"{word_fin} - {word_eng}\n")

        print("Dictionary entry added")
    else:
        search_term = input("Search term: ")

        with open("dictionary.txt") as dictionary:
            for line in dictionary:
                line = line.replace("\n", "")
                
                if search_term in line:
                    print(line)

    print("1 - Add word, 2 - Search, 3 - Quit")
    func = int(input("Function: "))

print("Bye!")