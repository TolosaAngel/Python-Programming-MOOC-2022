class NumberStats:
    def __init__(self):
        self.numbers = 0
        self.counter = 0

    def add_number(self, number:int):
        self.counter += 1 
        self.numbers += number

    def count_numbers(self):
        return self.counter

    def get_sum(self):
        return self.numbers

    def average(self):
        if self.counter==0: return 1
        else: return self.numbers/self.counter

all_numbers = NumberStats()
even_numbers = NumberStats()
odd_numbers = NumberStats()

number = int(input("Please type in integer numbers:\n"))

while number!=-1:
    all_numbers.add_number(number)

    if number%2==0: even_numbers.add_number(number)
    else: odd_numbers.add_number(number)
    
    number = int(input())

print(f"Sum of numbers: {all_numbers.get_sum()}")
print(f"Mean of numbers: {all_numbers.average()}")
print(f"Sum of even numbers: {even_numbers.get_sum()}")
print(f"Sum of odd numbers: {odd_numbers.get_sum()}")