total_number=0
multiplication=1
largest=-99999999
smallest=99999999
for i in range(3):
    number=int(input(f"enter the number {i+1}"))
    total_number+=number;
    multiplication*=number
    if(number>largest):
        largest=number
    if(number<smallest):
        smallest=number
sub=largest-smallest
print("the sum of numbers :",total_number)
print("the subtraction of numbers:",sub)
print("the multiplication of numbers",multiplication)

