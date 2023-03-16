from random import sample

def words(n: int, beginning: str):
    my_list = []

    with open("words.txt") as words:
        for line in words:
            line = line.replace("\n", "")

            if line.startswith(beginning):
                my_list.append(line)

    if len(my_list)<n:
        raise ValueError 
    else:
        final_list = sample(my_list, n)
        return final_list

if __name__ == "__main__":
    word_list = words(3, "ca")

    for word in word_list:
        print(word)