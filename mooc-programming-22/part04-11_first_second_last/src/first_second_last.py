def first_word(sentence):
    if sentence.find(" ") == -1:
        return sentence
    else:
        return sentence[:sentence.find(" ")]

def second_word(sentence):
    position = sentence.find(" ")
    sentence = sentence[position+1:]
    return first_word(sentence)

def last_word(sentence):
    sentence = sentence[::-1]
    sentence = first_word(sentence)
    sentence = sentence[::-1]
    return sentence

if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))

    sentence = "it was a dark and stormy python"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))

    sentence = "it was"
    print(first_word(sentence))
    print(second_word(sentence)) 
    print(last_word(sentence))