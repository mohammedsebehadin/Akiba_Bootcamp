user_input = input("Enter the letter/number: ")
left = 0
right = len(user_input) - 1
isPalindrome = True

while left < right:
    if user_input[left] != user_input[right]:
        isPalindrome = False
        break
    left += 1
    right -= 1

    if isPalindrome:
        print("palindrome")
    else:
        print("not palindrome")
