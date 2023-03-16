def to_dictionary(my_list: list):
    my_dictionary = {}
    
    for tuple in my_list:
        my_dictionary[tuple[0]] = tuple[1]

    return my_dictionary

if __name__ == "__main__":
    dictionary1 = to_dictionary([('country', 'finland'), ('city', 'helsinki'), ('room','kitchen')])
    dictionary2 = to_dictionary([('name', 'ella')])
    dictionary3 = to_dictionary([('constructor', 'aston martin'), ('driver', 'vettel')])

    print(dictionary1) # {'country': 'finland', 'city': 'helsinki', 'room': 'kitchen'}
    print(dictionary2) # {'name': 'ella'}
    print(dictionary3) # {'constructor': 'aston martin', 'driver': 'vettel'}