password=0
def length_checker(password):
    if len(password)<5:
        return "the entered password too short "
    else:
        return True
    
def uppercase_letter(password):  
            return [char for char in password if char.isupper()]


def lowercase_letter(password):
      return [char for char in password if char.islower()]
print(lowercase_letter("ndksAKMS%"))
def digit_checker(password):
      return [char for char in password if char.isdigit()]
print(digit_checker("ndksAKMS%ndksAKMS%92309309"))
def special_checker(password):
      return [not char.isalnum() and not char.isspace() for char in password]
print ("======password policy analyaztion=====")
print(length_checker("ndksAKMS%ndksAKMS%92309309"))
print(uppercase_letter("ndksAKMS%ndksAKMS%92309309"))
print(lowercase_letter("ndksAKMS%ndksAKMS%92309309"))
print(digit_checker("ndksAKMS%ndksAKMS%92309309"))
print(special_checker("ndksAKMS%ndksAKMS%92309309"))



  

