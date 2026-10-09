number = int(input("Enter five and above digits: "))
total = 0

while number > 0:
    last_digit = number % 10  # Get the last digit inside the loop
    total += last_digit       
    number = number // 10     

    print("Total:", total)
