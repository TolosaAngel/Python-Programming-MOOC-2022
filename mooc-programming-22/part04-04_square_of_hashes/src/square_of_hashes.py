def line(number, word):
    if word=="":
        character = "*"
    else:
        character = word[0]

    print(character*number) 

def square_of_hashes(size):
    send_size = size

    while size>0 :
        line(send_size, "#")
        size-=1

if __name__ == "__main__":
    square_of_hashes(5)
    print()
    square_of_hashes(3)
