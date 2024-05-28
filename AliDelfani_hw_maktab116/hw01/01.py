number = int(input("Enter a number: "))

if number <= 1:
    print(f"{number} is not a perfect number.")
else:    
    divisors = [1]  
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            divisors.append(i)
            if i != number // i: 
                divisors.append(number // i)
    
    sum_of_divisors = sum(divisors)
    
    if sum_of_divisors == number:
        print(f"{number} is a perfect number.")
    else:
        print(f"{number} is not a perfect number.")
