list = []
c = 0

while True:
    word = input("Word: ")
    
    if word in list:
        break
    else:
        c+=1

    list.append(word)

print(f"You typed in {c} different words")