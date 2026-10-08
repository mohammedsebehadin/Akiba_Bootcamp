# this request from the system to enter the number
number=int(input("enter the number"))
if(number<=1):
   print("the number must greater than one okay!")
else:
  for divisor in  range(2,int(number**0.5+1)):
     if(number%divisor==0):
        print("it is not prime number")
        break
     else:
        print("it is prime number")