def same_chars(word, number1, number2):
    if number1>number2:
        if len(word)>number1 and word[number1]==word[number2]:
            return True
    elif number2>number1:
        if len(word)>number2 and word[number1]==word[number2]:
            return True
    
    return False

if __name__ == "__main__":
    print(same_chars("coder", 1, 2))
    print(same_chars("programmer", 6, 7)) 
    print(same_chars("programmer", 0, 4)) 
    print(same_chars("programmer", 0, 12)) 