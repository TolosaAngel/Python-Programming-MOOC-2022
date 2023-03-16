from datetime import *

filename = input("Filename: ")

str_start_date = input("Starting date: ")
list_start_date = str_start_date.split(".")
dt_start_date = datetime( int(list_start_date[2]), int(list_start_date[1]), int(list_start_date[0]) )

days = int(input("How many days: "))

print("Please type in screen time in minutes on each day (TV computer mobile):")

today = dt_start_date
left_days = days
total_time = 0
days_and_time = []

while left_days:
    format_today = today.strftime("%d.%m.%Y")

    screen_time = input(f"Screen time {format_today}: ")
    screen_time = screen_time.replace(" ", "/")

    num_screen_time = screen_time.split("/")

    for num in num_screen_time:
        total_time += int(num)

    days_and_time.append(f"{format_today}: {screen_time}\n")

    left_days-=1
    today += timedelta(days=1)

    if left_days==0:
        print(f"Data stored in file {filename}")

with open(filename, "w") as my_file:
    dt_start_date = dt_start_date.strftime("%d.%m.%Y")

    my_file.write(f"Time period: {dt_start_date}-{format_today}\nTotal minutes: {total_time}\nAverage minutes: {total_time/days}\n")    

    for entry in days_and_time:
        my_file.write(entry)