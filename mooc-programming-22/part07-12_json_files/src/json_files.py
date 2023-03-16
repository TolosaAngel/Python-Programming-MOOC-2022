from json import loads

def print_persons(filename: str):
    with open(filename) as my_file:
        data = my_file.read()

    my_list = loads(data)

    for person in my_list:
        print(person["name"], end=" ") 
        print(person["age"], end=" ") 
        
        if len(person["hobbies"])>0:
            print("years (", end="")

            for hobbie_pos in range(len(person["hobbies"])):
                print(person["hobbies"][hobbie_pos], end="")

                if hobbie_pos+1!=len(person["hobbies"]):
                    print(", ", end="")
                else:   
                    print(")")
        else:
            print("years ()")
        

if __name__ == "__main__":
    print_persons("file4.json")