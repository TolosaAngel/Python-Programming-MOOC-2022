list = []
print(f"The list is now {list}")
option = input("a(d)d, (r)emove or e(x)it: ")

while option!="x":
    if option=="d":
        list.append(len(list)+1)
        print(f"The list is now {list}")
    elif option=="r":
        list.pop()
        print(f"The list is now {list}")
    
    option = input("a(d)d, (r)emove or e(x)it: ")

print("Bye!")