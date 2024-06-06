def is_power_of_base(number, base):
    if number < base:
        return False
    elif number == base:
        return True
    else:
        while number % base == 0:
            number = number / base
        return number == 1

number = int(input("Enter the number: "))
base = int(input("Enter the base: "))

output = is_power_of_base(number, base)
print(output)
