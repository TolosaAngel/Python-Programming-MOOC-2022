def no_vowels(word):
    new_word = word.replace("a","")
    new_word = new_word.replace("e","")
    new_word = new_word.replace("i","")
    new_word = new_word.replace("o","")
    new_word = new_word.replace("u","")

    return new_word

if __name__=="__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))