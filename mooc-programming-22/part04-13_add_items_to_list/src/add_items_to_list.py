list = []
items = int(input("How many items: "))
i = 1

while i<=items:
    item = int(input(f"Item {i}: "))
    list.append(item)
    i+=1

print(list)