ATM_PIN=1386;
for attempt in range(1,4):
    the_guessed_number=int(input("enter the pin four digits"))
    if the_guessed_number==ATM_PIN:
        print("PIN correct " \
        "Welcome to AKIBA HUB")
        break
    elif attempt<3:
        print("incorrect.u have two attempt")
    else:
        print("u have finished ur attempt")