from string import *

def change_case(orig_string: str):
    new_str = ""

    for letter in orig_string:
        if letter.isupper():
            new_str += letter.lower()
        else:
            new_str += letter.upper()

    return new_str

def split_in_half(orig_string: str):
    mid = len(orig_string)//2
    my_tuple = orig_string[0:mid], orig_string[mid:]

    return my_tuple

def remove_special_characters(orig_string: str):
    new_str = ""
    char_list = []
    char_letters = ascii_letters + digits + whitespace

    for letter in char_letters:
        char_list.append(letter)

    for letter in orig_string:
        if letter in char_list:
            new_str += letter

    return new_str