list = []
item = int(input("New item: "))
list.append(item)

while item!=0:
    print(f"The list now: {list}")
    print(f"The list in order: {sorted(list)}")

    item = int(input("New item: "))
    list.append(item)

print("Bye!")