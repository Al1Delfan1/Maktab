number = int(input("Enter an integer: "))

if number <= 0:
    print(f"{number} is not a power of 2.")
else:
    is_power_of_2 = True
    
    while number > 1:
        if number % 2 != 0:
            is_power_of_2 = False
            break
        number = number // 2
    
    if is_power_of_2:
        print("The number is a power of 2.")
    else:
        print("The number is not a power of 2.")
