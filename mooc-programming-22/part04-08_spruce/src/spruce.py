def spruce(size):
    print("a spruce!")

    row = "*"
    original_size = size

    while size>0:
        print(" " * (size-1) + row)
        row += "**"
        size -= 1  

    print(" " * (original_size-1) + "*")

if __name__ == "__main__":
    spruce(5)
    print()
    spruce(3)