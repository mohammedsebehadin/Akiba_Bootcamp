first_number=int(input("enter the first number"))
second_number=int(input("enter the second number"))
third_number=int(input("enter the third number"))
# for the first number
if(first_number==second_number==third_number):
    print("all three number are equal")
if(first_number>second_number):
    if(first_number>third_number):
        print("the largest number is:",first_number)
#for the second number
if(second_number>first_number):
    if(second_number>third_number):
        print('the largest number is:',second_number)
#for the third number        
if(third_number>first_number):
    if(third_number>second_number):
        print("the largest number is",third_number)
