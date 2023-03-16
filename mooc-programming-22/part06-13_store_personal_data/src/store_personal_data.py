def store_personal_data(person: tuple):
    name, age, height = person
    
    with open("people.csv", "a") as my_file:
        my_file.write(f"{name};{age};{height}\n")

if __name__ == "__main__":
    store_personal_data(("Paul Paulson", 37, 175.5))
    store_personal_data(("Paul Paulson", 37, 175.5))