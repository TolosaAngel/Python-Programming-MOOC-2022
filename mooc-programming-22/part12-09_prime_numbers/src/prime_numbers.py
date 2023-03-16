def prime_numbers():
    actual_number = 0

    while True:
        numbers_list = [int(number) for number in range(1,actual_number)]
        divisors_list = [int(number) for number in numbers_list if actual_number%number==0]

        if len(divisors_list)==1 and divisors_list[0]==1:
            yield actual_number
        
        actual_number += 1

if __name__ == "__main__":
    numbers = prime_numbers()
    
    for i in range(8):
        print(next(numbers))