from fractions import *

def fractionate(amount: int):
    my_list = []
    times = amount

    while times:
        my_list.append(Fraction(1,amount))
        times-=1

    return my_list

if __name__ == "__main__":
    for p in fractionate(3):
        print(p)

    print()

    print(fractionate(5))