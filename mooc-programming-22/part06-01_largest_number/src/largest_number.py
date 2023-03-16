def largest():
    max_num = 0
    c = 0

    with open("numbers.txt") as my_file:
        for line in my_file:
            if c==0:
                max_num = int(line)
                c+=1
            elif int(line)>max_num:
                max_num = int(line)
            
    return max_num

if __name__ == "__main__":
    print(largest())

