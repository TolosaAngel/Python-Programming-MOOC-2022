def dict_of_numbers():
    numbers = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
                6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
                11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
                15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
                19 : 'nineteen'}

    for num in range(20,100):
        num_copy = str(num)

        if 20<=num<30: numbers[num] = "twenty"
        if 30<=num<40: numbers[num] = "thirty"
        if 40<=num<50: numbers[num] = "forty"
        if 50<=num<60: numbers[num] = "fifty"
        if 60<=num<70: numbers[num] = "sixty"
        if 70<=num<80: numbers[num] = "seventy"
        if 80<=num<90: numbers[num] = "eighty"
        if 90<=num<100: numbers[num] = "ninety"

        if num%10!=0:
            numbers[num] += "-" + numbers[int(num_copy[1])]

    return numbers
    
if __name__ == "__main__":
    print(dict_of_numbers())