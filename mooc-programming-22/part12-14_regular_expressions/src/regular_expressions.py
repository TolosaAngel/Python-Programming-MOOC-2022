import re

def is_dotw(my_string: str):
    return bool(re.search("Mon|Tue|Wed|Thu|Fri|Sat|Sun", my_string))

def all_vowels(my_string: str):
    if re.search("[aeiou]",my_string):
        if len(my_string)==len("".join([letter for letter in my_string if letter in "aeiou"])):
            return True

    return False

def time_of_day(my_string: str):
    return bool(re.search("^(([0-1]\d)|(2[0-3]))(:[0-5]\d){2}$",my_string))

if __name__ == "__main__":
    print(time_of_day("12:43:01"))
    print(time_of_day("AB:01:CD"))
    print(time_of_day("17:59:59"))
    print(time_of_day("33:66:77"))