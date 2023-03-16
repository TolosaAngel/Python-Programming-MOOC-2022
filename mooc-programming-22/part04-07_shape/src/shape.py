def line(number, word):
    if word=="":
        character = "*"
    else:
        character = word[0]

    print(character*number) 

def triangle(size, character):
    i = 0

    while i<=size:
        line(i, character)
        i+=1

def square(width, size, character):
    while size>0:
        line(width, character)
        size-=1

def shape(width_t, t, width_r, r):
    triangle(width_t, t)
    square(width_t, width_r, r)

if __name__ == "__main__":
    shape(5, "x", 2, "o")
    print()
    shape(5, "X", 3, "*")
    print()
    shape(2, "o", 4, "+")
    print()
    shape(3, ".", 0, ",")