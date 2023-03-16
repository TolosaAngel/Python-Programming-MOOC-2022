text = input("Write text: ").strip()
word_from_input = text.split(" ")

correct_words = []

with open("wordlist.txt") as word_list:
    for word in word_list:
        correct_words.append(word.replace("\n", ""))

ans = ""

for word in word_from_input:
    if word.lower() in correct_words:
        ans += word + " "
    else:
        ans += "*"+word+"* "

print(ans)