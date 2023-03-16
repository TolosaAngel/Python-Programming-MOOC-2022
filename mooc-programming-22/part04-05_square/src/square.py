def line(number, word):
    if word=="":
        character = "*"
    else:
        character = word[0]

    print(character*number) 

def square(size, character):
    send_size = size

    while size>0:
        line(send_size, character)
        size-=1

if __name__ == "__main__":
    square(5, "x")
    print()
    square(5, "*")
    print()
    square(3, "o")