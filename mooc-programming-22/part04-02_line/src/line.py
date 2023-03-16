def line(number, word):
    if word=="":
        character = "*"
    else:
        character = word[0]

    print(character*number)    

if __name__ == "__main__":
    line(5, "x")
    line(7, "%")
    line(10, "LOL")
    line(3, "")