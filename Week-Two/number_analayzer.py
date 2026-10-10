even_count=0
odd_count=0
total_sum=0
largest=-999999999 #extreme small number 
smallest=999999999

for i in range(10):
    number=int(input(f"enter the number {i+1}"))
    print("the number:",number)
    total_sum+=number

    # 1. Check Even/Odd
    if(number%2==0):
        even_count+=1
    else:
        odd_count+=1

        
        if number>largest:
            largest=number

            
            if number<smallest:
                smallest=number

                
avg=total_sum/10
print("\n ----final analysis----")
print("total sum",total_sum)
print("average",avg)
print("even count",even_count)
print("odd count",odd_count)
print("largest number",largest)
print("smallest number",smallest)
