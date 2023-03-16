from copy import deepcopy

def invert(dictionary: dict):
    new_dictionary = deepcopy(dictionary)
    dictionary.clear()

    for key, value in new_dictionary.items():
        dictionary[value] = key

if __name__=="__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)