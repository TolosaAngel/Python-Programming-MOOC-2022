def greatest_number(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    elif c>=a and c>=b:
        return c
    
    if a==b:
        if a>c:
            return a
        else:
            return c

    if a==c:
        if a>b:
            return a
        else:
            return b

    if b==c:
        if b>a:
            return b
        else:
            return a

if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)
    print(greatest_number(3, 4, 1)) 
    print(greatest_number(99, -4, 7)) 
    print(greatest_number(0, 0, 0)) 
    print(greatest_number(1, 1, -100))