def line(number, word):
    if word=="":
        character = "*"
    else:
        character = word[0]

    print(character*number)  

def box_of_hashes(height):
    while height>0:
        line(10, "#")
        height-=1

if __name__ == "__main__":
    box_of_hashes(5)
    print()
    box_of_hashes(2)