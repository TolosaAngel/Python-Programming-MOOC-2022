def find_words(search_term: str):
    match_words = []

    with open("words.txt") as words_file:
        for line in words_file:
            word = line.replace("\n", "")

            if search_term[0]=="*":
                if word.endswith(search_term[1:]):
                    match_words.append(word) 
            elif search_term[len(search_term)-1]=="*":
                if word.startswith(search_term[0:len(search_term)-1]):
                    match_words.append(word) 
            elif "." in search_term:
                add = True

                if len(word)==len(search_term):
                    for i in range(len(search_term)):
                        if search_term[i]!=".":
                            if search_term[i]!=word[i]:
                                add = False
                                break
                else:
                    add = False

                if add:
                    match_words.append(word)
            else:
                if word==search_term:
                    match_words.append(word)

    return match_words

if __name__ == "__main__":
    print(find_words("*vokes"))
    print(find_words("cat"))
    print(find_words("ca."))
    print(find_words("c.d."))
    print(find_words("reson*"))