def line(number, word):
    if word=="":
        character = "*"
    else:
        character = word[0]

    print(character*number) 

def triangle(size):
    i = 0

    while i<=size:
        line(i, "#")
        i+=1

if __name__ == "__main__":
    triangle(5)
    print()
    triangle(6)
    print()
    triangle(3)
