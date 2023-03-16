def read_fruits():
    my_dictionary = {} 

    with open("fruits.csv") as my_file:
        for line in my_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            my_dictionary[parts[0]] = float(parts[1])

    return my_dictionary

if __name__ == "__main__":
    print(read_fruits())
