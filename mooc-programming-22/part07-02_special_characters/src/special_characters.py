from string import *

def separate_characters(my_string: str):
    f_string = ""
    s_string = ""
    t_string = ""
    
    for letter in my_string:
        if letter in ascii_letters:
            f_string += letter
        elif letter in punctuation:
            s_string += letter
        else:
            t_string += letter

    return f_string,s_string,t_string

if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])