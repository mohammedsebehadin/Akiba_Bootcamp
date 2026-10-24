numbers = [92, 8, 1, 92, 0, 10, 2]


def validate_number(number):
    if number <= 0:
        raise ValueError("the number must be positive")


def is_prime(number):

    if number <= 1:
        return "it is not prime number"

    for divisor in range(2, int(number**0.5) + 1):
        if number % divisor == 0:
            return "it is not prime number"

        return "it is prime number"


def get_divisor(number):
    # Fixed validation
    if number <= 0:
        return []  

    divisors = []
    for divisor in range(1, number + 1):
        if number % divisor == 0:
            divisors.append(divisor)
            return divisors


def sum_of_digits(number):
    if number < 0:
        return 0

    total = 0
    
    for digit in str(number):
        total += int(digit)
        return total


def reverse_number(number):
    reversed_num = int(str(number)[::-1])
    return reversed_num


def even_odd(number):
    
    if number % 2 == 0:
        return "even"
    else:
        return "odd"


def analyzer_of_number(numbers_list):
    print("===============================")
    print("        NUMBER ANALYZER        ")
    print("===============================")

    
    for number in numbers_list:
        print(f"\nAnalyzing Number: {number}")
        print(f"  - Type: {even_odd(number)}")
        print(f"  - Primality: {is_prime(number)}")
        print(f"  - Divisors: {get_divisor(number)}")
        print(f"  - Sum of Digits: {sum_of_digits(number)}")
        print(f"  - Reversed: {reverse_number(number)}")
        print("-" * 31)


        
analyzer_of_number(numbers)
