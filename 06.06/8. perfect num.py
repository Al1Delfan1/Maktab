def is_perfect_number(number):
    if number <= 0:
        return False
    
    divisor_sum = 0
    for i in range(1, number):
        if number % i == 0:
            divisor_sum += i
    if divisor_sum == number:
        return True

number = 6

output = is_perfect_number(number)
print(output)
