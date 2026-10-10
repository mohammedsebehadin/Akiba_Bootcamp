even_count=0
odd_count=0
total_sum=0
number=int(input("enter the natural number"));
for natural_number in range(1,number+1):
    total_sum+=natural_number
    if(natural_number%2==0):
        even_count+=1
    else:
        odd_count+=1
print("the sum of the total:",total_sum);
print("even numbers:",even_count);
print("odd number:",odd_count);