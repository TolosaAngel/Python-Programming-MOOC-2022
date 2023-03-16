from difflib import get_close_matches

def word_list():
    word_list = []

    with open("wordlist.txt") as list_of_words:
        for word in list_of_words:
            word = word.replace("\n", "")
            word_list.append(word)

    return word_list

my_list = word_list()

text = input("Write text: ").strip()
word_from_input = text.split(" ")

correct_words = []
incorrect_words = []

with open("wordlist.txt") as word_list:
    for word in word_list:
        correct_words.append(word.replace("\n", ""))

ans = str()

for word in word_from_input:
    if word.lower() in correct_words:
        ans += word + " "
    else:
        incorrect_words.append(word.lower())
        ans += "*"+word+"* "

print(ans)
print("suggestions:")

for word in incorrect_words:
    similar_words = str()
    similar_words_list = get_close_matches(word, my_list)

    for similar_word in similar_words_list:
        similar_words += similar_word + ", "

    similar_words = similar_words[:-2]

    print(f"{word}: {similar_words}")