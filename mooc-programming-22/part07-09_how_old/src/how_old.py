from datetime import *

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

date_of_birth = datetime(year, month, day)
new_millennium = datetime(1999,12,31)

result = (new_millennium-date_of_birth).days

if result<0:
    print("You weren't born yet on the eve of the new millennium.")
else:    
    print(f"You were {result} days old on the eve of the new millennium.")